# 17.Stwórz łańcuch zależnych od siebie korutyn:
# 1. 
# pobierz_id_uzytkownika(nazwa_uzytkownika) -> zwraca ID po 1s.
# 2. 
# pobierz_posty(id_uzytkownika) -> zwraca listę ID postów po 1s.
# 3. pobierz_komentarze(id_postu) -> zwraca listę komentarzy po 1s.
# Napisz main, które dla nazwy użytkownika pobierze jego ID, następnie listę jego
# postów, a na końcu pobierze komentarze dla wszystkich jego postów współbieżnie.
# Zmierz czas wykonania.


import asyncio
import time


async def pobierz_id_uzytkownika(nazwa_uzytkownika):
    await asyncio.sleep(1)
    return 1


async def pobierz_posty(id_uzytkownika):
    await asyncio.sleep(1)
    return [101, 102, 103]


async def pobierz_komentarze(id_postu):
    await asyncio.sleep(1)
    return [
        f"Komentarz 1 do posta {id_postu}",
        f"Komentarz 2 do posta {id_postu}"
    ]


async def main():
    start = time.time()

    id_uzytkownika = await pobierz_id_uzytkownika("Piotr")
    print(f"ID użytkownika: {id_uzytkownika}")

    posty = await pobierz_posty(id_uzytkownika)
    print(f"Posty: {posty}")

    komentarze = await asyncio.gather(
        pobierz_komentarze(posty[0]),
        pobierz_komentarze(posty[1]),
        pobierz_komentarze(posty[2])
    )

    print(f"Komentarze: {komentarze}")

    koniec = time.time()
    print(f"Czas wykonania: {koniec - start:.2f} s")


asyncio.run(main())