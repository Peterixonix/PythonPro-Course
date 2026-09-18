# 16. Stwórz klasę RateLimiter z metodą acquire(). Klasa powinna pozwalać na wykonanie
# acquire() tylko n razy na sekundę. Jeśli limit jest przekroczony, acquire() powinno
# asynchronicznie czekać tyle, ile trzeba, by kolejne wywołanie było dozwolone. Przetestuj,
# tworząc 20 zadań, które próbują wywołać acquire() w pętli, z ograniczeniem np. do 5
# zapytań/sekundę.


import asyncio
import time


class RateLimiter:
    def __init__(self, n):
        self.n = n
        self.odstep = 1 / n
        self.ostatnie_wywolanie = 0
        self.lock = asyncio.Lock()

    async def acquire(self):
        async with self.lock:
            teraz = time.monotonic()
            czas_oczekiwania = self.odstep - (teraz - self.ostatnie_wywolanie)

            if czas_oczekiwania > 0:
                await asyncio.sleep(czas_oczekiwania)

            self.ostatnie_wywolanie = time.monotonic()


async def zadanie(numer, limiter):
    await limiter.acquire()
    print(f"Zadanie {numer} - {time.strftime('%H:%M:%S')}")


async def main():
    limiter = RateLimiter(5)

    zadania = []

    for i in range(1, 21):
        task = asyncio.create_task(zadanie(i, limiter))
        zadania.append(task)

    await asyncio.gather(*zadania)


asyncio.run(main())