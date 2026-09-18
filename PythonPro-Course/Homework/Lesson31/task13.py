# 13. Używając asyncio, napisz prosty serwer TCP, który nasłuchuje na localhost:8888. Kiedy
# klient się połączy i wyśle wiadomość, serwer powinien odesłać tę samą wiadomość z
# powrotem i zamknąć połączenie. Wskazówka: poszukaj w dokumentacji
# asyncio.start_server


import asyncio


async def obsluz_klienta(reader, writer):
    dane = await reader.read(100)
    wiadomosc = dane.decode()

    print(f"Otrzymano: {wiadomosc}")

    writer.write(dane)
    await writer.drain()

    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(
        obsluz_klienta,
        "localhost",
        8888
    )

    print("Serwer działa na localhost:8888")

    async with server:
        await server.serve_forever()


asyncio.run(main())