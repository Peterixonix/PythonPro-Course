# 8.Napisz korutynę ping(host), która symuluje pingowanie serwera przez
# asyncio.sleep(random.uniform(0.1, 1.0)) i zwraca f"Host {host} odpowiada". Uruchom ją dla
# 5 różnych hostów współbieżnie.


import asyncio
import random
import time

async def ping(host):
    await asyncio.sleep(random.uniform(0.1, 1.0))
    return f"Host {host} odpowiada"

async def main():
    start = time.time()

    wynik1, wynik2, wynik3, wynik4, wynik5 = await asyncio.gather(
        ping("google.com"),
        ping("facebook.com"),
        ping("youtube.com"),
        ping("gmail.com"),
        ping("github.com")
    )
    print(wynik1)
    print(wynik2)
    print(wynik3)
    print(wynik4)
    print(wynik5)

    koniec = time.time()

    print(f"Czas oczekiwania: {koniec - start:.2f}")

asyncio.run(main())