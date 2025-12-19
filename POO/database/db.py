import sqlite3

class Database:
    def __init__(self, db_name="app.db"):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)
    
    def criar_tabelas(self):
        conn = self.conectar()
        cursor = conn.cursor()


        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                genero TEXT NOT NULL,
                email TEXT NOT NULL,
                senha TEXT NOT NULL
                tipo INTEGER
            )
        """)

        conn.commit()
        conn.close()