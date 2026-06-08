while True:
    wartosc_1 = int(input("Podaj pierwszą wartość (1 dla True, 0 dla False): "))
    wartosc_2 = int(input("Podaj drugą wartość (1 dla True, 0 dla False): "))

    if wartosc_1 not in (0, 1) or wartosc_2 not in (0, 1):
        print("Nieprawidłowa wartość. Podaj jeszcze raz (1 dla True, 0 dla False)")
        continue

    a = bool(wartosc_1)
    b = bool(wartosc_2)

    print("AND:", a and b)
    print("OR:", a or b)
    break






