import sqlite3
from models.classe import Classe

class ClasseDAO:
    def __init__(self, db_name="database/app.db"):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def criar_tabela(self):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS classes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE
            )
        """)

        conn.commit()
        conn.close()

    def salvar(self, classe: Classe):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO classes (nome)
            VALUES (?)
        """, (classe.get_nome(),))

        classe.set_id(cursor.lastrowid)

        conn.commit()
        conn.close()

    def listar_todas(self):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT id, nome FROM classes")
        rows = cursor.fetchall()
        conn.close()

        classes = []
        for r in rows:
            classes.append(Classe(id=r[0], nome=r[1]))

        return classes
