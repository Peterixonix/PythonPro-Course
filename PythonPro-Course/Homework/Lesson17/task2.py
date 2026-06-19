# Zadanie 2 – Prosty kalkulator
# Utwórz ścieżkę /add/<int:num1>/<int:num2>. Funkcja przypisana do tej ścieżki powinna
# przyjąć dwie liczby jako argumenty, zsumować je i zwrócić wynik w formacie "Wynik to:
# [suma]".

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Witaj na Stronie Głównej dodaj do ścieżki 'add/num1/num2'."
    


@app.route("/add/<int:num1>/<int:num2>")
def suma_liczb(num1: int, num2: int):
    return f"{num1} + {num2} = {num1 + num2}"

    
if __name__ == '__main__':
   app.run(debug = True)