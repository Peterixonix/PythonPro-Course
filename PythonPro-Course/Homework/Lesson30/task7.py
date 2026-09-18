# 7. Producent i konsument
# Zaimplementuj producenta i konsumenta wykorzystujących queue.Queue. 
# Producent co sekundę dodaje losową liczbę, a konsument co 1,5 sekundy ją pobiera i wyświetla. 
# Program powinien działać przez 10 sekund.



import threading
import queue
import time
import random


kolejka = queue.Queue()
koniec = False


def producent():
    global koniec

    while not koniec:
        liczba = random.randint(1, 100)
        kolejka.put(liczba)
        print(f"Producent dodał: {liczba}")

        time.sleep(1)


def konsument():
    global koniec

    while not koniec:
        if not kolejka.empty():
            liczba = kolejka.get()
            print(f"Konsument pobrał: {liczba}")

        time.sleep(1.5)


watek_producent = threading.Thread(target=producent)
watek_konsument = threading.Thread(target=konsument)

watek_producent.start()
watek_konsument.start()

time.sleep(10)

koniec = True

watek_producent.join()
watek_konsument.join()

print("Koniec programu.")