# 5. Procesy i przekazywanie argumentów. 
# Stwórz funkcję potega(liczba, pot). 
# Uruchom ją w osobnym procesie z argumentami 5 i 3. 
# Proces powinien obliczyć i wyświetlić wynik.


import multiprocessing


def potega(liczba, pot):
    wynik = liczba ** pot
    print(f"Wynik: {wynik}")


if __name__ == "__main__":
    proces = multiprocessing.Process(
        target=potega,
        args=(5, 3)
    )

    proces.start()
    proces.join()