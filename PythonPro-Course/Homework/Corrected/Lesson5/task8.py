imiona = ["Anna", "Jan", "Piotr", "Kasia"]

imiona_norm = [i.strip().lower() for i in imiona]

uzytkownik_imie = input("Podaj imię: ").strip().lower()

for imie_norm in imiona_norm:
    if imie_norm == uzytkownik_imie:
        print("Imię znajduje się na liście")
        break
else:
    print("Imię nie znajduje się na liście")
