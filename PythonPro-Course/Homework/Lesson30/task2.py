# 2. Wiele wątków i join()
# Uruchom 5 wątków. Każdy powinien otrzymać swój numer od 1 do 5 i go wyświetlić. 
# Główny program ma poczekać na zakończenie wszystkich wątków.

import threading
import time

def wiele_watkow(numer_watku):
    print(f"Wątek numer {numer_watku} mówi: Cześć!")
    time.sleep(3)
watki = []
for i in range(1,6):
    thread = threading.Thread(
        target=wiele_watkow,
        args=(i,)
    )
    watki.append(thread)
    thread.start()

print("Wszystkie wątki zostały uruchomione.")

for thread in watki:
    thread.join()

print("Wszystkie wątki zakończyły pracę.")