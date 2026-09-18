# 15. Napisz program, w którym 5 korutyn współbieżnie generuje jakieś dane tekstowe (np. "Log
# z korutyny X"). Wszystkie powinny zapisywać swoje logi do jednego pliku. Zapewnij, aby
# dostęp do pliku był zsynchronizowany, żeby wpisy się nie pomieszały. Użyj asyncio.Lock
# oraz biblioteki aiofiles (pip install aiofiles).


import asyncio
import aiofiles


lock = asyncio.Lock()


async def zapisz_log(numer):
    tekst = f"Log z korutyny {numer}\n"

    async with lock:
        async with aiofiles.open("logi.txt", "a", encoding="utf-8") as plik:
            await plik.write(tekst)


async def main():
    await asyncio.gather(
        zapisz_log(1),
        zapisz_log(2),
        zapisz_log(3),
        zapisz_log(4),
        zapisz_log(5)
    )


asyncio.run(main())