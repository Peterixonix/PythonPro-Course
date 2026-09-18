# 1. :pencil2: **Pierwsza korutyna:** 
# Napisz korutynę, która po uruchomieniu wypisze "Gotowy do nauki!". Uruchom ją.


import asyncio


async def nauka():
    print("Gotowy do nauki!")


asyncio.run(nauka())