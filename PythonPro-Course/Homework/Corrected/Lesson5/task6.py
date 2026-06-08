sekret = 42

while True:
    liczba = int(input("Podaj liczbę: "))
    if liczba == sekret:
        print("Gratulacje")
        break
    else:
        print("Nie trafiono, spróbuj ponownie.")
