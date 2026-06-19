# Zadanie 8 – Model produktu w SQLAlchemy
    
#     Zdefiniuj model SQLAlchemy o nazwie Product. Powinien on zawierać pola: id (klucz główny, integer),
# name (string, nie może być pusty) oraz price (float, nie może być pusty). Następnie w interaktywnej konsoli 
# Pythona dodaj kilka przykładowych produktów do bazy danych.
# Zadanie 9 – Wyświetlanie produktów
    
# Stwórz ścieżkę /products i szablon products.html. W funkcji pobierz wszystkie produkty z bazy danych 
# (stworzone w zadaniu 8) i przekaż je do szablonu. Wyświetl produkty w tabeli HTML, która będzie 
# miała kolumny "Nazwa" i "Cena".

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Product(db.Model):
    __tablename__ = 'shop'
    id_shop = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
@app.route('/products')
def products():
    all_products = Product.query.all()
    return render_template("products.html", products=all_products)
def dane():
    if Product.query.first() is None:
        demo = [
            Product(name="Kawa ziarnista 1 kg", price=49.99),
            Product(name="Herbata zielona 100 g", price=14.50),
            Product(name="Czekolada gorzka 70%", price=7.99),
        ]
        db.session.add_all(demo)
        db.session.commit()
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        dane()
    app.run(debug=True)