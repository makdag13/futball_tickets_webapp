from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Veritabanı bağlantısı
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Veritabanı başlatma
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Kullanıcılar tablosu
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

    # İletişim bilgileri tablosu
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            user_id INTEGER,
            address TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    # Bilet bilgileri tablosu
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            user_id INTEGER,
            mecz TEXT NOT NULL,
            seat_number INTEGER NOT NULL,
            ticket_type TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer-info', methods=['GET'])
def customer_info():
    return render_template('customer_info.html')

@app.route('/kontakt', methods=['GET'])
def kontakt():
    return render_template('kontakt.html')

@app.route('/o-nas', methods=['GET'])
def o_nas():
    return render_template('o_nas.html')

@app.route('/products', methods=['GET'])
def products():
    return render_template('products.html')

@app.route('/submit-kontakt', methods=['POST'])
def submit_kontakt():
    name = request.form.get('name')
    email = request.form.get('email')
    suggestion = request.form.get('suggestion')

    if not name or not email or not suggestion:
        return render_template('error.html', message="Lütfen tüm alanları doldurun.")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO suggestions (name, email, suggestion) VALUES (?, ?, ?)',
                   (name, email, suggestion))
    conn.commit()
    conn.close()

    return render_template('success.html', message="Teşekkürler! Öneriniz alınmıştır.")

@app.route('/submit-personal-info', methods=['POST'])
def submit_personal_info():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    age = request.form.get('age')

    if not first_name or not last_name or not age:
        return render_template('error.html', message="Tüm alanlar doldurulmalıdır.")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (first_name, last_name, age) VALUES (?, ?, ?)',
                   (first_name, last_name, age))
    conn.commit()
    conn.close()

    return redirect(url_for('address'))

@app.route('/address')
def address():
    return render_template('address.html')

@app.route('/submit-address', methods=['POST'])
def submit_address():
    address = request.form.get('address')
    phone = request.form.get('phone')
    email = request.form.get('email')

    if not address or not phone or not email:
        return render_template('error.html', message="Adres, telefon numarası ve e-posta girilmelidir.")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM users ORDER BY id DESC LIMIT 1')
    user = cursor.fetchone()

    if user is None:
        conn.close()
        return render_template('error.html', message="Kullanıcı bilgisi bulunamadı.")

    user_id = user['id']
    cursor.execute('INSERT INTO contacts (user_id, address, email, phone) VALUES (?, ?, ?, ?)',
                   (user_id, address, email, phone))

    conn.commit()
    conn.close()

    return redirect(url_for('mecz_page'))

@app.route('/mecz')
def mecz_page():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Dolu koltukları al
    cursor.execute('SELECT seat_number, ticket_type FROM tickets')
    seats = cursor.fetchall()
    taken_seats = [f"{seat['seat_number']}{seat['ticket_type']}" for seat in seats]

    conn.close()
    return render_template('mecz.html', taken_seats=taken_seats)

@app.route('/submit-mecz', methods=['POST'])
def submit_mecz():
    mecz = request.form.get('mecz')
    seat_number = request.form.get('seat_number')
    ticket_type = request.form.get('ticket_type')

    if not mecz or not seat_number or not ticket_type:
        return render_template('error.html', message="Tüm alanlar doldurulmalıdır.")

    conn = get_db_connection()
    cursor = conn.cursor()

    # Koltuğun daha önce seçilip seçilmediğini kontrol et
    cursor.execute('''
        SELECT * FROM tickets WHERE seat_number = ? AND ticket_type = ?
    ''', (seat_number, ticket_type))
    existing_seat = cursor.fetchone()

    if existing_seat:
        conn.close()
        return render_template('ticket_error.html')

    cursor.execute('SELECT id FROM users ORDER BY id DESC LIMIT 1')
    user = cursor.fetchone()

    if user is None:
        conn.close()
        return render_template('error.html', message="Kullanıcı bilgisi bulunamadı.")

    user_id = user['id']
    cursor.execute('INSERT INTO tickets (user_id, mecz, seat_number, ticket_type) VALUES (?, ?, ?, ?)',
                   (user_id, mecz, seat_number, ticket_type))

    # Kullanıcının email bilgisi
    cursor.execute('SELECT email FROM contacts WHERE user_id = ?', (user_id,))
    contact = cursor.fetchone()

    if contact is None:
        conn.close()
        return render_template('error.html', message="İletişim bilgileri bulunamadı.")

    email = contact['email']

    conn.commit()
    conn.close()

    # E-posta gönderimi
    send_confirmation_email(to_email=email, mecz=mecz, seat_number=seat_number, ticket_type=ticket_type)

    return render_template('success.html')

def send_confirmation_email(to_email, mecz, seat_number, ticket_type):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "mustafaakdg13@gmail.com"
    sender_password = "your_gmail_app_password"

    subject = "Potwierdzenie biletu"
    body = f"""
    Cześć,

    Poniżej znajduje się potwierdzenie zakupu biletu na mecz:

    Mecz: {mecz}
    Numer miejsca: {seat_number}
    Katagoria biletu: {ticket_type}

    Dziękujemy za wybór oficjalnego sklepu Legia Warszawa!

    Z poważaniem,
    Oficjalny Sklep Legia Warszawa
    """

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message.as_string())
    except Exception as e:
        print(f"E-posta gönderiminde hata oluştu: {e}")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
