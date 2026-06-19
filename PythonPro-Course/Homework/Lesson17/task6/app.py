# Zadanie 6 – Słownik w szablonie
    
#     Stwórz w app.py słownik opisujący książkę, np. {'title': 'Hobbit', 'author': 'J.R.R. Tolkien', 'year': 1937}.
# Stwórz ścieżkę /book i szablon book.html. Przekaż słownik do szablonu i wyświetl jego zawartość w czytelny sposób, 
# np. używając nagłówków i paragrafów.




from flask import Flask, render_template


# app = Flask(__name__)


# dane1 = {'title': 'Hobbit', 'author': 'J.R.R. Tolkien', 'year': 1937}

# @app.route('/book')
# def dane():
#     return render_template("book.html", book=dane1['title'], book2=dane1['author'], book3=dane1['year'])
    
# if __name__ == "__main__":
#     app.run(debug=True)




app = Flask(__name__)


dane1 = {'title': 'Hobbit', 'author': 'J.R.R. Tolkien', 'year': 1937}

@app.route('/book')
def dane():
    return render_template("book.html", book=dane1['title'], book2=dane1['author'], book3=dane1['year'])
    
if __name__ == "__main__":
    app.run(debug=True)