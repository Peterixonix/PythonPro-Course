# 10. Pula procesów do zadań CPU
# Wygeneruj 100 losowych liczb i za pomocą multiprocessing.Pool sprawdź równolegle, które z nich są pierwsze. 
# Następnie zmodyfikuj zadanie tak, aby pula procesów wykonywała inne kosztowne obliczenie CPU-bound. 
# Porównaj podejście z użyciem wątków i procesów.


import multiprocessing
import random
import time
from concurrent.futures import ThreadPoolExecutor


def czy_pierwsza(liczba):
    if liczba < 2:
        return False

    for i in range(2, int(liczba ** 0.5) + 1):
        if liczba % i == 0:
            return False

    return True


def kosztowne_obliczenie(liczba):
    suma = 0

    for i in range(5_000_000):
        suma += i * liczba

    return suma


if __name__ == "__main__":

    # 100 losowych liczb
    liczby = [random.randint(1, 1000) for _ in range(100)]

    # Sprawdzanie liczb pierwszych za pomocą multiprocessing.Pool
    with multiprocessing.Pool() as pool:
        wyniki = pool.map(czy_pierwsza, liczby)

    ile_pierwszych = sum(wyniki)

    print(f"Liczby: {liczby}")
    print(f"Znaleziono liczb pierwszych: {ile_pierwszych}")


    # CPU-bound - wątki
    dane = [1, 2, 3, 4]

    start = time.time()

    with ThreadPoolExecutor() as executor:
        wyniki_watki = list(
            executor.map(kosztowne_obliczenie, dane)
        )

    czas_watki = time.time() - start

    print(f"Wątki: {czas_watki:.2f} s")


    # CPU-bound - procesy
    start = time.time()

    with multiprocessing.Pool() as pool:
        wyniki_procesy = pool.map(
            kosztowne_obliczenie,
            dane
        )

    czas_procesy = time.time() - start

    print(f"Procesy: {czas_procesy:.2f} s")


    # Porównanie
    print(f"Czas wątków: {czas_watki:.2f} s")
    print(f"Czas procesów: {czas_procesy:.2f} s")