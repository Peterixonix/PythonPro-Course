# 18. Stwórz zadanie, które działa w nieskończonej pętli, co sekundę drukując "Pracuję...". W
# głównej korutynie main, pozwól mu pracować przez 5 sekund, a następnie je anuluj
# (task.cancel()). W "pracującej" korutynie obsłuż wyjątek asyncio.CancelledError, aby
# wydrukować komunikat "Anulowano, sprzątam..." przed jej ostatecznym zakończeniem.


import asyncio


async def pracuj():
    try:
        while True:
            print("Pracuję...")
            await asyncio.sleep(1)

    except asyncio.CancelledError:
        print("Anulowano, sprzątam...")
        raise


async def main():
    task = asyncio.create_task(pracuj())

    await asyncio.sleep(5)

    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        pass


asyncio.run(main())