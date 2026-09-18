# 6.Stwórz korutynę pobierz_pogode(miasto), która po 1.5 sekundy zwraca słownik z fikcyjnymi
# danymi pogodowymi, np. {'miasto': miasto, 'temperatura': 25, 'stan': 'słonecznie'}.


import asyncio


async def pobierz_pogode(miasto):
    słownik = {
        'miasto': miasto, 
        'temperatura': 25, 
        'stan': 'słonecznie'
        }
    await asyncio.sleep(1.5)
    return słownik

async def main():
    wynik = await pobierz_pogode("Warszawa")
    print(wynik)

asyncio.run(main())