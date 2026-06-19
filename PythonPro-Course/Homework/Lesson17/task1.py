# Stwórz nową ścieżkę /me w swojej aplikacji. Kiedy użytkownik wejdzie na ten adres, funkcja
# powinna zwrócić Twoje imię i nazwisko.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def idex():
    return "Witaj na Stronie Głównej dodaj do ścieżki 'me'"

@app.route("/me")
def dane():
    return "Piotr Pietruliński"

if __name__ == "__main__":
    app.run(debug=True)