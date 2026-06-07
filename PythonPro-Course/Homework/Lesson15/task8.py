import sqlite3

class DatabaseRaw:
    def __init__(self, db_name = 'task.db'):
        self.db_name = db_name
    
    def init_db(self):
        with sqlite3.connect(self.db_name) as conn:
         c = conn.cursor()
         c.execute("""--sql
                   CREATE TABLE IF NOT EXISTS zadania(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   opis TEXT NOT NULL,
                   zrobione BOOLEAN NOT NULL default 0 CHECK (zrobione IN (0, 1)))""")
         conn.commit()
         return "Utworzono tabelę."
         

    def alter_dodaj_prio(self):
        qr = '''--sql
        ALTER TABLE zadania 
        ADD priorytet INTEGER default 1;'''
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(qr)
            conn.commit()
            return "Dodano nową kolumne 'priorytet'"
            
    
    def pobierz_zadania(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, opis, zrobione, priorytet FROM zadania")
            

class TaskManagerRaw(DatabaseRaw):
    def dodaj_zadanie(self, opis, prio):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO zadania (opis, priorytet) VALUES (?, ?)",(opis, prio))
            conn.commit()
            return "Dodano nowe zadanie"
            

    
    def oznacz_jako_zrobione(self, id_zadania: int):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE zadania SET zrobione = ? WHERE id = ?",(True, id_zadania))
            conn.commit()
            return f"Zadanie numer: {id_zadania} Ustawiono jako zrobione."
            
    
    def usun_zadanie(self, id_zadanie: int):
        qr = """--sql
        DELETE FROM
        zadania WHERE id = ?"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(qr, (id_zadanie,))
            conn.commit()
            return f"Usunięto zadanie numer {id_zadanie}"

    
    def wyszukaj_zad(self, search: str):
        qr = """--sql
        SELECT opis
        FROM zadania
        WHERE opis LIKE ?"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(qr, (f"%{search}%",))
            print("Wyszukano zadanie")
            return cursor.fetchall()
   

           
            

       
d = DatabaseRaw()
print(d.init_db())
print(d.alter_dodaj_prio())
t = TaskManagerRaw()
print(t.dodaj_zadanie("Jedz.", 1))
print(t.dodaj_zadanie("Nie rób nic.", 3))
print(t.dodaj_zadanie("Śpij.", 2))
print(t.oznacz_jako_zrobione(2))
print(t.wyszukaj_zad("N"))
print(t.usun_zadanie(3))