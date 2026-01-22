import sqlite3
from models.unidade import Unidade

class UnidadeDAO:
    def __init__(self, db_name="app.db"):
        self.db_name = db_name

    def salvar(self, unidade: Unidade):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO unidades (nome)
            VALUES (?)
        """, (unidade.get_nome(),))

        unidade.set_id(cursor.lastrowid)

        conn.commit()
        conn.close()

    def buscar_por_id(self, id: int):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome FROM unidades WHERE id = ?
        """, (id,))

        row = cursor.fetchone()
        conn.close()

        if row:
            return Unidade(id=row[0], nome=row[1])
        return None
