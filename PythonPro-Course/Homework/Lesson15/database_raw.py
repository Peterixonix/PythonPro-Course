import sqlite3


DATABASE_NAME = 'todo_raw.db'




def init_db():
    """Inicjalizuje bazę danych i tworzy tabelę, jeśli nie istnieje."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        # Używamy IF NOT EXISTS, aby uniknąć błędu przy ponownym
        cursor.execute('''--sql
        CREATE TABLE IF NOT EXISTS zadania (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        opis TEXT NOT NULL,
        zrobione BOOLEAN NOT NULL default 0 CHECK (zrobione IN (0, 1)))
        ''')
        conn.commit()

def alter_dodaj_prio():
    qr = '''--sql
    ALTER TABLE zadania 
    ADD priorytet INTEGER default 1;'''
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(qr)
        conn.commit()


def dodaj_zadanie(opis: str, prio: int = 1):
    """Dodaje nowe zadanie do bazy danych."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        # Używamy placeholderów (?), aby zapobiec SQL Injection
        cursor.execute("INSERT INTO zadania (opis, priorytet) VALUES (?, ?)",(opis, prio))
        conn.commit()


def pobierz_zadania():
    """Pobiera wszystkie zadania z bazy danych."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, opis, zrobione, priorytet FROM zadania")
        return cursor.fetchall()


def oznacz_jako_zrobione(id_zadania: int):
    """Oznacza zadanie o podanym ID jako zrobione."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE zadania SET zrobione = ? WHERE id = ?",
        (True, id_zadania))
        conn.commit()

def usun_zadanie(id_zadanie: int):
    qr = """--sql
    DELETE FROM
    zadania WHERE id = ?
    """
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(qr, (id_zadanie,))
        conn.commit()

def wyszukaj_zad(search: str):
    qr = """--sql
    SELECT id, opis, zrobione, priorytet
    FROM zadania
    WHERE opis LIKE ?"""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(qr, (f"%{search}%",))
        return cursor.fetchall()
        


