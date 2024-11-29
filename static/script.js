// Sepete ürün eklemek için
let cart = [];
let totalPrice = 0;

document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', function() {
        const name = this.getAttribute('data-name');
        const price = parseFloat(this.getAttribute('data-price'));

        // Sepete ürün ekleme
        cart.push({ name, price });
        totalPrice += price;

        // Sepet ve toplam fiyat güncelleniyor
        updateCart();
    });
});

// Sepeti ve toplam fiyatı güncelleme
function updateCart() {
    const cartItems = document.getElementById('cart-items');
    cartItems.innerHTML = ''; // Sepeti temizle
    cart.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name} - ${item.price} PLN`;
        cartItems.appendChild(li);
    });

    const totalPriceElement = document.getElementById('total-price');
    totalPriceElement.textContent = totalPrice.toFixed(2);

    // Ödeme butonunu aktif hale getir
    const checkoutButton = document.getElementById('checkout-button');
    checkoutButton.disabled = totalPrice === 0;
}

// Ödeme butonuna tıklandığında, kullanıcıyı ödeme sayfasına yönlendir
document.getElementById('checkout-button').addEventListener('click', function() {
    window.location.href = '/checkout'; // Ödeme sayfasına yönlendir
});
