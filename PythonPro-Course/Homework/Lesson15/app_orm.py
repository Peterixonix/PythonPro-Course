
from sqlalchemy.orm import Session
from sqlalchemy_app.database import get_db
from sqlalchemy_app.models import Zadanie

def pokaz_zadania(db: Session):
    zadania = db.query(Zadanie).all() 
    if not zadania:
        print("Brak zadań na liście.")
        return
    print("\n--- Twoja lista zadań ---")
    for zadanie in zadania:
        status = "✓" if zadanie.zrobione else "✗"
        print(f"[{status}] ID: {zadanie.id}, Opis: {zadanie.opis}")
    print("------------------------\n")

def wyszukiwanie_zadan(db: Session, fraza):
    wyszukaj = db.query(Zadanie).filter(Zadanie.opis.contains(fraza)).all()
    if not wyszukaj:
        print("Nie znaleziono zadania.")
    else: 
        print("Wyszukane zadanie")
    for wyszukiwanie in wyszukaj:
        print(f"{wyszukiwanie.id} {wyszukiwanie.opis}")

def dodaj_zadanie(db: Session, opis: str):
    nowe_zadanie = Zadanie(opis=opis) 
    db.add(nowe_zadanie)
    db.commit()
    db.refresh(nowe_zadanie)

def usun_zadanie(db: Session, id_zadania: int):
    usun = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    db.delete(usun)
    db.commit()

def oznacz_jako_zrobione(db: Session, id_zadania: int):
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first() 
    if zadanie:
        zadanie.zrobione = True 
        db.commit()
        print("Zadanie zaktualizowane!")
    else:
        print("Nie znaleziono zadania o podanym ID.")

def main():
    db_generator = get_db()
    db_session = next(db_generator)

    while True:
        print("Menu (SQLAlchemy):")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Usuń zadanie")
        print("5. Wyszukaj zadanie")
        print("6. Wyjdź")

        wybor = input("Wybierz opcję: ")
        if wybor == '1':
            pokaz_zadania(db_session)
        elif wybor == '2':
            opis = input("Podaj opis zadania: ")
            dodaj_zadanie(db_session, opis)
            print("Zadanie dodane!")
        elif wybor == '3':
            try:
                id_zadania = int(input("Podaj ID zadania do oznaczenia: "))
                oznacz_jako_zrobione(db_session, id_zadania)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == '4':
            try:
                id_zadania = int(input("Podaj id zadania do usunięcia: "))
                usun_zadanie(db_session, id_zadania)
                print("Zadanie zostało usunięte.")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == '5':
            wyszukiwanie = input("Podaj zadanie do wyszukania: ")
            wyszukiwanie_zadan(db_session, wyszukiwanie)
        elif wybor == '6':
            print("Do zobaczenia!")
            db_session.close()
            break
        else:
            print("Nieznana opcja, spróbuj ponownie.")

if __name__ == "__main__":
    main()  