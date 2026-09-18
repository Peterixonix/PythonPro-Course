# 9. Pula wątków do zadań I/O Napisz program, 
# który symuluje 20 zapytań do API AI przez time.sleep(random.uniform(0.5, 2.0)). 
# Wykorzystaj ThreadPoolExecutor do równoległego wykonania zadań. 
# Zmierz czas i porównaj go z wykonaniem sekwencyjnym.



import time
import random
from concurrent.futures import ThreadPoolExecutor


def zapytanie_api(numer):
    time.sleep(random.uniform(0.5, 2.0))
    return numer




start = time.time()

for i in range(20):
    zapytanie_api(i)

koniec = time.time()

czas_sekwencyjny = koniec - start

print(f"Sekwencyjnie: {czas_sekwencyjny:.2f} s")



start = time.time()

with ThreadPoolExecutor() as executor:
    wyniki = executor.map(zapytanie_api, range(20))

    list(wyniki)

koniec = time.time()

czas_watki = koniec - start

print(f"ThreadPoolExecutor: {czas_watki:.2f} s")


# Porównanie

print(f"Czas sekwencyjny: {czas_sekwencyjny:.2f} s")
print(f"Czas z ThreadPoolExecutor: {czas_watki:.2f} s")