# 6. Komunikacja między procesami
# Stwórz proces, który pobiera od użytkownika imię za pomocą input(), 
# a następnie przekazuje je do procesu nadrzędnego przez multiprocessing.Queue. 
# Proces nadrzędny powinien wyświetlić "Witaj, [imię]!".

import multiprocessing
import sys


def pobierz_imie(kolejka):
    sys.stdin = open(0)

    imie = input("Podaj swoje imię: ")
    kolejka.put(imie)


if __name__ == "__main__":
    kolejka = multiprocessing.Queue()

    proces = multiprocessing.Process(
        target=pobierz_imie,
        args=(kolejka,)
    )

    proces.start()
    proces.join()

    imie = kolejka.get()

    print(f"Witaj, {imie}!")