# 10. Napisz korutynę odliczanie(nazwa, start), która co sekundę drukuje komunikat "{nazwa}:
# zostało {pozostało} sekund". Uruchom trzy takie odliczania współbieżnie, każde z inną
# nazwą i innym czasem początkowym (np. 5s, 3s, 7s).


import asyncio

async def odliczanie(nazwa, start):
    for pozostało in range(start, 0, -1):
        print(f"{nazwa}: zostało {pozostało} s")
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(
        odliczanie("Pierwsze", 5),
        odliczanie("Drugie", 3),
        odliczanie("Trzecie", 7)
    )


asyncio.run(main())