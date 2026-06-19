# Zadanie 3 – Przekaż listę do szablonu
# W pliku app.py stwórz listę swoich ulubionych filmów. Następnie stwórz nową ścieżkę
# /movies i szablon movies.html. Przekaż listę filmów do szablonu i wyświetl ją jako listę
# nieuporządkowaną () w HTML.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/movies')
def movie():
    movie = ["Strażnicy galaktyki", "Avengers: Koniec gry", "Jurassic World", "Król lew",
             "Zielona mila", "Skazany na Shawshank", "Piraci z karaibów: Klątwa czarnej perły"]
    return render_template('movies.html', title = "Filmy", users=movie)

if __name__ == '__main__':
    app.run(debug=True)