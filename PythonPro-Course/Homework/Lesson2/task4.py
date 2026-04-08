imie = input("Podaj swoje imię: ")

pierwsza_wielka = imie[0].upper()
pierwsza_mala = imie[0].lower()

print(f"Pierwsza litera wielka: {pierwsza_wielka} -> kod: {ord(pierwsza_wielka)}")
print(f"Pierwsza litera mała:   {pierwsza_mala} -> kod: {ord(pierwsza_mala)}")
