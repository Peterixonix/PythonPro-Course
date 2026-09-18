# 3. Wątki vs wykonanie sekwencyjne
# Napisz funkcję pobierz_dane(id_danych), która symuluje pobieranie danych przez time.sleep(2). 
# Uruchom ją dla 3 danych sekwencyjnie, a następnie równolegle w 3 wątkach. Zmierz i porównaj czasy.

import threading
import time


# Pobieranie sekwencyjne
def pobierz_dane_sekw(id_danych):
    print(f"Pobieranie danych {id_danych}...")
    time.sleep(2)
    print(f"Pobrano dane {id_danych}")


start_time = time.time()

for i in range(1, 4):
    pobierz_dane_sekw(i)

czas_sekwencyjny = time.time() - start_time

print(f"Sekwencyjnie: {czas_sekwencyjny:.2f} s")


# Pobieranie równoległe
def pobierz_dane_row(id_danych):
    print(f"Pobieranie danych {id_danych}...")
    time.sleep(2)
    print(f"Pobrano dane {id_danych}")


start_time = time.time()
watki = []

for i in range(1, 4):
    thread = threading.Thread(
        target=pobierz_dane_row,
        args=(i,)
    )
    watki.append(thread)
    thread.start()

for thread in watki:
    thread.join()

czas_rownolegly = time.time() - start_time

print(f"Równolegle: {czas_rownolegly:.2f} s")


# Porównanie czasów
print(f"Czas sekwencyjny: {czas_sekwencyjny:.2f} s")
print(f"Czas równoległy: {czas_rownolegly:.2f} s")