# 14. Zaimplementuj system z jednym producentem i dwoma konsumentami przy użyciu
# asyncio.Queue. Producent co 0.5 sekundy dodaje do kolejki liczbę (od 1 do 20).
# Konsumenci pobierają liczby z kolejki, jak tylko się pojawią, i wypisują, który konsument
# przetworzył daną liczbę (np. "Konsument 1 przetworzył liczbę: 5").


import asyncio


async def producent(kolejka):
    for liczba in range(1, 21):
        await asyncio.sleep(0.5)
        await kolejka.put(liczba)


async def konsument(nazwa, kolejka):
    while True:
        liczba = await kolejka.get()

        print(f"Konsument {nazwa} przetworzył liczbę: {liczba}")

        kolejka.task_done()


async def main():
    kolejka = asyncio.Queue()

    producent_task = asyncio.create_task(producent(kolejka))

    konsument1 = asyncio.create_task(konsument(1, kolejka))
    konsument2 = asyncio.create_task(konsument(2, kolejka))

    await producent_task
    await kolejka.join()

    konsument1.cancel()
    konsument2.cancel()


asyncio.run(main())