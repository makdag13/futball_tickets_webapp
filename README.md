Legia Warszawa Sklep Online - Readme
Opis Projektu
Cel Biznesowy
Projekt Legia Warszawa Sklep Online to aplikacja internetowa przeznaczona do zarządzania sprzedażą produktów związanych z klubem piłkarskim Legia Warszawa. Głównym celem projektu jest umożliwienie użytkownikom zakupu oficjalnych produktów klubu, składania zamówień na bilety na mecze, oraz kontaktowanie się z zespołem Legii Warszawa poprzez formularz kontaktowy.

Rozwiązania
Projekt ten zapewnia użytkownikom możliwość przeglądania dostępnych produktów, takich jak koszulki, czapki i szaliki związane z Legią Warszawa. Użytkownicy mogą również wypełniać formularz kontaktowy, gdzie mogą przesyłać swoje sugestie lub pytania do klubu. Dodatkowo, aplikacja umożliwia składanie zamówień, w tym rezerwację biletów na mecze oraz składanie zamówień na produkty. Wszystkie dane są przechowywane w bazie danych SQLite.

Struktura Techniczna
Technologie Użyte
Backend:

Python 3.13
Flask – framework webowy dla Python
SQLite – baza danych do przechowywania danych aplikacji
Frontend:

HTML/CSS – szablony stron internetowych
JavaScript – interaktywność w aplikacji
Schemat Bazy Danych
Projekt korzysta z bazy danych SQLite, która zawiera następujące tabele:

users:

id: klucz główny, autoinkrementowany
first_name: imię użytkownika
last_name: nazwisko użytkownika
age: wiek użytkownika
email: adres e-mail użytkownika
contacts:

user_id: ID użytkownika
address: adres użytkownika
phone: numer telefonu użytkownika
tickets:

user_id: ID użytkownika
mecz: mecz, na który użytkownik rezerwuje bilet
seat_number: numer miejsca na stadionie
ticket_type: typ biletu (np. VIP, normalny)
suggestions:

id: klucz główny, autoinkrementowany
name: imię i nazwisko użytkownika
email: adres e-mail użytkownika
suggestion: treść sugestii przesłanej przez użytkownika
Główne Funkcje
Strona Główna: Użytkownicy mogą przeglądać główną stronę sklepu, zawierającą informacje o produktach i aktualnościach.
Produkty: Użytkownicy mogą przeglądać dostępne produkty Legii Warszawa, takie jak koszulki, czapki, i szaliki.
Zamówienia: Użytkownicy mogą składać zamówienia na produkty lub bilety na mecze, a także wypełniać formularze kontaktowe.
Formularz Kontaktowy: Użytkownicy mogą przesyłać sugestie i pytania do zespołu Legii Warszawa.
Płatności
Projekt obecnie nie obsługuje płatności online. Zamówienia są rejestrowane w systemie, ale nie są jeszcze powiązane z zewnętrznymi systemami płatności.

Logowanie Google/Facebook
Projekt nie zawiera jeszcze logowania przez Google lub Facebook, ale jest to przyszłe rozszerzenie, które może zostać dodane do aplikacji w celu poprawy doświadczenia użytkowników.

Zrzuty ekranu

Problemy W Implementacji
Podczas implementacji napotkano kilka problemów, które wymagały rozwiązania:

Zarządzanie sesją użytkownika: Brakowało mechanizmu do zarządzania sesją użytkownika, co wymagało dodania logiki związanej z identyfikacją użytkowników.
Formularze i walidacja danych: Wdrożenie walidacji danych na froncie i backendzie było kluczowe, aby zapobiec błędnym danym przesyłanym do bazy danych.
Brak integracji z płatnościami: Projekt obecnie nie obsługuje płatności online. Wymagało to dodatkowych prac związanych z planowaniem i wdrażaniem API do obsługi płatności.
Rozwiązania
Aby rozwiązać problemy, zaktualizowano kod aplikacji o nowe funkcje, takie jak walidacja formularzy i zarządzanie sesją użytkownika. Dodatkowo, zaktualizowano strukturę bazy danych i dodano odpowiednie kontrole błędów w systemie.



Rozwój i przyszłe rozszerzenia
W przyszłości planowane jest dodanie:

Logowania przez Google i Facebook
Integracji z płatnościami online
Ulepszania UX i funkcjonalności strony
Projekt ten jest nadal w fazie rozwoju i wymaga dodatkowych prac, aby spełnić oczekiwania użytkowników i rozszerzyć dostępne funkcje.
