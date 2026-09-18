# 9.Napisz program, który przyjmuje listę adresów URL i współbieżnie sprawdza status HTTP
# każdego z nich. Użyj biblioteki aiohttp. Wskazówka: musisz ją zainstalować (pip install
# aiohttp) i użyć aiohttp.ClientSession. Dla każdego URL wypisz jego status (np.
# "
# https://google.com - Status: 200").

import aiohttp
import asyncio

async def sprawdz_status(session, url):
    async with session.get(url) as response:
        print(f"{url} - Status {response.status}")


async def main():
    urls = [
        "https://google.com",
        "https://youtube.com",
        "https://github.com"
    ]

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            sprawdz_status(session, urls[0]),
            sprawdz_status(session, urls[1]),
            sprawdz_status(session, urls[2])
        )


asyncio.run(main())