# Napisz program, który prosi użytkownika o wpisanie dowolnego tekstu.
# Następnie, używając konwersji na bool , sprawdź, czy wpisany tekst jest "prawdziwy"
# (niepusty) i wyświetl odpowiedni komunikat.


tekst = input("Wpisz dowolny tekst: ")


if bool(tekst):
    print("Tekst jest prawdziwy (niepusty).")
else:
    print("Tekst jest fałszywy (pusty).")
