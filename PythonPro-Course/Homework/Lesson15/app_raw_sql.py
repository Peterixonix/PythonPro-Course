from database_raw import pobierz_zadania, init_db, dodaj_zadanie, oznacz_jako_zrobione, usun_zadanie, wyszukaj_zad
# import database_raw as db
import pdb

def pokaz_zadania():
    """Wyświetla listę wszystkich zadań."""
    zadania = pobierz_zadania()
    if not zadania:
        print("Brak zadań na liście.")
        return
    print("\n--- Twoja lista zadań ---")
    for i, (id_, opis, status, prio) in enumerate(zadania):
        status = "✓" if status else "✗"
        print(f"[{status}][ID:{id_}],[prio:{prio}]: {opis}")
        print("------------------------\n")

def menu_dodaj_zad():
    opis = input("Podaj opis zadania: ")
    prio = input("Priorytet: ")
    if prio == "":
        prio = 1
    else:
        try:
            prio = int(prio)
            if not (1 <= prio <= 5):
                raise ValueError
        except ValueError:
            print("Podano nieprawidłową liczbę")
    dodaj_zadanie(opis, prio)
    print("Zadanie dodane!")

def menu_wyszukaj_zad():
    opis = input("Wyszukaj zadanie: ")
    wyszukaj = wyszukaj_zad(opis)
    if not wyszukaj:
        print("Brak wyszukanego zadania.")
    else:
        print("Wyszukane zadanie: ")
        print(wyszukaj)

    
    



    


def main():
    # db.init_db()
    init_db() # Upewnij się, że baza i tabela istnieją

    while True:
        print("Menu:")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Usuń zadanie")
        print("5. Wyszukaj zadanie")
        print("6. Wyjdź")
        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            pokaz_zadania()
        elif wybor == '2':
            menu_dodaj_zad()

        elif wybor == '3':
            try:
                id_zadania = int(input("Podaj ID zadania do oznaczenia: "))
                oznacz_jako_zrobione(id_zadania)
                print("Zadanie zaktualizowane!")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == '4':
            id_zadania = int(input("Podaj zadanie do usunięcia: "))
            usun_zadanie(id_zadania)
            print("Zadanie zostało usunięte")
        elif wybor == "5":
            menu_wyszukaj_zad()
        elif wybor == '6':
            print("Do zobaczenia!")
            break
        else:
            print("Nieznana opcja, spróbuj ponownie.")
        

if __name__ == "__main__":
    main()