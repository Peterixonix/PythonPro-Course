# 4. Race condition i Lock
# Stwórz globalną listę. Uruchom 2 wątki, z których każdy dodaje do niej 100 000 elementów.
# Sprawdź wynik, uruchamiając program kilka razy.
# Następnie zabezpiecz operację za pomocą threading.Lock i porównaj rezultaty.

import threading


# Bez Lock

lista = []


def dodaj_elementy():
    for _ in range(100000):
        lista.append(1)


watki = []

for _ in range(2):
    thread = threading.Thread(target=dodaj_elementy)
    watki.append(thread)
    thread.start()

for thread in watki:
    thread.join()

wynik_bez_lock = len(lista)

print(f"Bez Lock: {wynik_bez_lock}")


# Z Lock

lista = []
lock = threading.Lock()


def dodaj_elementy_lock():
    for _ in range(100000):
        lock.acquire()
        try:
            lista.append(1)
        finally:
            lock.release()


watki = []

for _ in range(2):
    thread = threading.Thread(target=dodaj_elementy_lock)
    watki.append(thread)
    thread.start()

for thread in watki:
    thread.join()

wynik_z_lock = len(lista)

print(f"Z Lock: {wynik_z_lock}")


# Porównanie rezultatów

print(f"Wynik bez Lock: {wynik_bez_lock}")
print(f"Wynik z Lock: {wynik_z_lock}")