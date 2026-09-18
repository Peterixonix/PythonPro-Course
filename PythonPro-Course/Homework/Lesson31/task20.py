# 20. Napisz korutynę, która śpi przez losowy czas od 1 do 5 sekund. Uruchom ją, ale z
# ograniczeniem czasowym na 3 sekundy. Jeśli korutyna nie zakończy się w tym czasie,
# program powinien rzucić wyjątek asyncio.TimeoutError. Obsłuż ten wyjątek i wypisz
# odpowiedni komunikat. Wskazówka: użyj asyncio.wait_for().


import asyncio
import random


async def losowe_zadanie():
    czas = random.uniform(1, 5)
    print(f"Wylosowany czas: {czas:.2f} s")

    await asyncio.sleep(czas)

    print("Zadanie zakończone.")


async def main():
    try:
        await asyncio.wait_for(
            losowe_zadanie(),
            timeout=3
        )

    except asyncio.TimeoutError:
        print("Przekroczono limit czasu 3 sekund.")


asyncio.run(main())