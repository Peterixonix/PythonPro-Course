# 2. :pencil2: **Asynchroniczny licznik:** Napisz korutynę `licznik(n)`, która co 
# sekundę wypisuje liczby od 1 do n używając `await asyncio.sleep(1)`.

import asyncio
import time


async def licznik(n):
    for i in range(1, n + 1):
        print(i)
        await asyncio.sleep(1)

asyncio.run(licznik(5))