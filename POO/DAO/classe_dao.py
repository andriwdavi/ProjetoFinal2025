import sqlite3
from models.classe import Classe

class ClasseDAO:
    def __init__(self, db_name="app.db"):
        self.db_name = db_name

    def salvar(self, classe: Classe):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO classes (nome)
            VALUES (?)
        """, (classe.get_nome(),))

        classe.set_id(cursor.lastrowid)

        conn.commit()
        conn.close()

    def buscar_por_id(self, id: int):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome FROM classes WHERE id = ?
        """, (id,))

        row = cursor.fetchone()
        conn.close()

        if row:
            return Classe(id=row[0], nome=row[1])
        return None
