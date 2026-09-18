# 11. Napisz korutynę dlugie_obliczenia(), która po losowym czasie (od 2 do 5 sekund) zwraca
# losową liczbę całkowitą (od 1 do 100). Uruchom 10 takich zadań współbieżnie i po
# zakończeniu wszystkich oblicz i wypisz sumę ich wyników.

import asyncio
import random

async def dlugie_obliczenia():
    await asyncio.sleep(random.uniform(2, 5))
    return random.randint(1, 100)


async def main():
    wyniki = await asyncio.gather(
        dlugie_obliczenia(),
        dlugie_obliczenia(),
        dlugie_obliczenia(),
        dlugie_obliczenia(),
        dlugie_obliczenia(),
        dlugie_obliczenia(),
        dlugie_obliczenia(),
        dlugie_obliczenia(),
        dlugie_obliczenia(),
        dlugie_obliczenia()
    )

    print(f"Wyniki: {wyniki}")
    print(f"Suma wyników: {sum(wyniki)}")

asyncio.run(main())
