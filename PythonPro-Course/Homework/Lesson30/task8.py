# 8. GIL w praktyce Zaimplementuj CPU-bound funkcję wykonującą intensywne obliczenia. 
# Zmierz czas: dwukrotnego wykonania sekwencyjnego, dwukrotnego wykonania w dwóch wątkach, dwukrotnego wykonania w dwóch procesach. 
# Porównaj wyniki i wyjaśnij wpływ GIL.




import threading
import multiprocessing
import time


def cpu_bound():
    suma = sum(i * i for i in range(20_000_000))
    return suma


if __name__ == "__main__":



    start = time.time()

    cpu_bound()
    cpu_bound()

    koniec = time.time()

    print(f"Sekwencyjnie: {koniec - start:.2f} s")




    start = time.time()

    watek1 = threading.Thread(target=cpu_bound)
    watek2 = threading.Thread(target=cpu_bound)

    watek1.start()
    watek2.start()

    watek1.join()
    watek2.join()

    koniec = time.time()

    print(f"Dwa wątki: {koniec - start:.2f} s")




    start = time.time()

    proces1 = multiprocessing.Process(target=cpu_bound)
    proces2 = multiprocessing.Process(target=cpu_bound)

    proces1.start()
    proces2.start()

    proces1.join()
    proces2.join()

    koniec = time.time()

    print(f"Dwa procesy: {koniec - start:.2f} s")