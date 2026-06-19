# Zadanie 10 – Aplikacja do rejestracji na wydarzenie
    
#     Stwórz kompletną mini-aplikację.
    
#     a. Zdefiniuj model SQLAlchemy Registration z polami id, name (string), email (string, unikalny).
    
#     b. Stwórz ścieżkę /register, która będzie obsługiwać metody GET i POST (poszukaj w dokumentacji Flaska,
#        jak to zrobić - methods=['GET', 'POST']).
    
#     c. Stwórz szablon register.html z formularzem HTML (<form>) zawierającym pola na imię i email oraz 
#        przycisk "Zarejestruj". Formularz powinien wysyłać dane metodą POST.
    
#     d. W funkcji dla ścieżki /register, sprawdź, czy żądanie jest typu POST. Jeśli tak, pobierz dane z formularza, 
#        stwórz nowy obiekt Registration, zapisz go w bazie danych i przekieruj użytkownika na stronę z podziękowaniem. 
#        Jeśli żądanie jest typu GET, po prostu wyświetl formularz.
    


from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'dev-secret'  # dla flash (opcjonalnie)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# a) Model Registration
class Registration(db.Model):
    __tablename__ = 'registrations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
# b) Ścieżka /register (GET i POST)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # d) Pobierz dane z formularza
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        # Prosta walidacja minimalna
        if not name or not email:
            flash('Uzupełnij imię i email.', 'error')
            return render_template('register.html', name=name, email=email)
        # Sprawdź czy email już istnieje (unikalny)
        exists = Registration.query.filter_by(email=email).first()
        if exists:
            flash('Ten email jest już zarejestrowany.', 'error')
            return render_template('register.html', name=name, email=email)
        # Utwórz i zapisz rekord
        reg = Registration(name=name, email=email)
        db.session.add(reg)
        db.session.commit()
        # Przekierowanie na stronę z podziękowaniem
        return redirect(url_for('thanks', name=name))
    # GET: wyświetl formularz
    return render_template('register.html')
# Prosta strona z podziękowaniem
@app.route('/thanks')
def thanks():
    name = request.args.get('name') or 'Uczestniku'
    return render_template('thanks.html', name=name)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
