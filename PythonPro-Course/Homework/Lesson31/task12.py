# Uruchom 5 zadań, z których każde śpi przez losowy czas (od 1 do 10 sekund), a następnie
# zwraca swój czas uśpienia. Napisz program, który zakończy działanie i wypisze wynik
# pierwszego zakończonego zadania, nie czekając na pozostałe. Wskazówka: użyj
# asyncio.wait() z argumentem return_when=asyncio.FIRST_COMPLETED.


import asyncio
import random

async def losowy_czas():
    czas = random.uniform(1, 10)
    await asyncio.sleep(czas)
    return czas

async def main():
    zadania = [
        asyncio.create_task(losowy_czas())
        for _ in range(5)
    ]

    zakonczone, pozostale = await asyncio.wait(
        zadania,
        return_when=asyncio.FIRST_COMPLETED
    )

    for zadanie in zakonczone:
        print(f"Pierwsze zadanie zakończyło się po: {zadanie.result():.2f} s")

    for zadanie in pozostale:
        zadanie.cancel()


asyncio.run(main())