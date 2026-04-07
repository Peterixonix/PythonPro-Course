imię = input("Jak masz na imię:")
print(imię)
wiek = input("Ile masz lat:")
print(wiek)
if int(wiek) == 18:
    print(f"{wiek} to dobry wiek, by zacząć naukę")
elif int(wiek) < 18:
    print(f"To jeszcze nie twój czas.")
else:
    print(f"{wiek} lat to trochę późno ale nigdy nie jes za późno na naukę")
    
praca = input("Jaką pracę wykonujesz Fizyczną, Biurową czy nie pracujesz:")
if praca == "Fizyczną":
    print("To zapewne masz dobrą kondycję, ale nie martw się tu nie trzeba będzie. ")
elif praca == "Briurową":
    print("To będzie troche podobieństwa do tego co będziemy robić.")
else:
    print("Nie martw się u nas zbobędziesz upragniony zawód.")