# 1. Pierwszy wątek.
# Napisz program, który tworzy i uruchamia jeden wątek. Wątek 
# powinien odczekać 3 sekundy, a następnie wyświetlić "Wątek zakończył pracę!".
# Główny program powinien w tym czasie wyświetlić "Główny program czeka na wątek...".

import threading
import time

def zadanie_dla_watku():
    print("Wątek startuje...")
    time.sleep(3)
    print("Wątek kończy pracę.")

thread = threading.Thread(target=zadanie_dla_watku)

thread.start()

print("Główny program czeka na wątek...")

thread.join()
print("Główny program zakończył działanie.")