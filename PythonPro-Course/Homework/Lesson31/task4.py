# 4. Zmodyfikuj kod z poprzedniego zadania. Uruchom obie korutyny współbieżnie, używając
# asyncio.gather(). Zmierz i porównaj czas wykonania.


import asyncio
import time


async def first_task():
    print("Przygotowuje pierwsze zadanie")
    await asyncio.sleep(2)
    print("Zadanie 1 zakończone")


async def second_task():
    print("Przygotowuje drugie zadanie")
    await asyncio.sleep(1)
    print("Zadanie 2 zakończone")


async def main():
    start = time.time()

    await asyncio.gather(
        first_task(),
        second_task()
    )

    koniec = time.time()

    print(f"Czas wykonania: {koniec - start:.2f} s")


asyncio.run(main())