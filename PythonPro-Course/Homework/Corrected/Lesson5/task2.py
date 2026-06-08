# Napisz program, który oblicza cenę biletu. Cena bazowa to 100 PLN.
# Jeśli użytkownik jest studentem ( tak/nie ) LUB ma mniej niż 18 lat, przysługuje mu 50%
# zniżki. Użyj operatorów or i and .



cena_biletu = 100
wiek = int(input("Ile masz lat?: "))
jestes_studentem = input("Czy jesteś studentem? (tak/nie): ")

if jestes_studentem.lower().strip() == "tak" or wiek < 18:
    print(cena_biletu / 2)
else:
    print(cena_biletu)





