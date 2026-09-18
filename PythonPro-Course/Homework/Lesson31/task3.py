# 3.Stwórz dwie korutyny: zadanie1 śpi przez 2 sekundy i drukuje "Zadanie 1 zakończone", a
# zadanie2 śpi przez 1 sekundę i drukuje "Zadanie 2 zakończone". W głównej korutynie main
# uruchom je sekwencyjnie (używając await na każdej z nich po kolei) i zmierz czas
# wykonania.



import asyncio
import time


async def first_task():
    print("Przygotowuje pierwsze zadanie")
    await asyncio.sleep(2)
    print("Zadanie 1 zakończone")



async def second_task():
    print("Przygotowuje drugie zadanie")
    await asyncio.sleep(1)
    print("Zadanie 2 zakończenie")


async def main():
    start=time.time()

    await first_task()
    await second_task()

    koniec = time.time()

    print(f"Czas wykonywania: {koniec - start:.2} s")


asyncio.run(main())