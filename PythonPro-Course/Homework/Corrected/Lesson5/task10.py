kursy = {
    "USD": 4.0,
    "EUR": 4.3,}

while True:
    odpowiedz = input("Podaj kwotę i walutę w formacie 'kwota waluta': ").strip()
    czesci = odpowiedz.split()
    if len(czesci) != 2:
        print("Niepoprawny format. Użyj: kwota waluta (np. 100 USD)")
        continue

    kwota_txt, waluta_txt = czesci
    try:
        kwota = float(kwota_txt.replace(",", "."))
    except ValueError:
        print("Niepoprawna kwota. Podaj liczbę (np. 123.45).")
        continue

    waluta = waluta_txt.upper()

    if waluta == "USD":
        kurs = kursy["USD"]
    elif waluta == "EUR":
        kurs = kursy["EUR"]

    else:
        print("Niepoprawna waluta. Dostępne:", ", ".join(kursy.keys()))
        continue

    pln = kwota / kurs
    print(f"{kwota:.2f} {waluta} to {pln:.2f} PLN")

    koniec = input("Czy chcesz zakończyć? (tak/nie): ").strip().lower()
    if koniec == "tak":
        break
