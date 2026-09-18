# 7.Używając korutyny z zadania 6, napisz program, który współbieżnie pobierze dane
# pogodowe dla listy miast: ["Warszawa", "Kraków", "Gdańsk"] i wydrukuje wyniki.



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

    wynik1, wynik2, wynik3 = await asyncio.gather(
    pobierz_pogode("Warszawa"),
    pobierz_pogode("Kraków"),
    pobierz_pogode("Gdańsk")
    )

    print(wynik1)
    print(wynik2)
    print(wynik3)
    

asyncio.run(main())