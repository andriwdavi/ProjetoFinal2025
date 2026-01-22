import sqlite3
from models.lider import Lider

class LiderDAO:
    def __init__(self, db_name="database/app.db"):
        self.db_name = db_name

    def salvar(self, lider: Lider):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO usuarios
            (nome, idade, genero, email, senha, tipo, cargo, unidade_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            lider.get_nome(),
            lider.get_idade(),
            lider.get_genero(),
            lider.get_email(),
            lider.get_senha(),
            lider.get_tipo(),
            lider.get_cargo(),
            lider.get_unidade_id()
        ))

        lider.set_id(cursor.lastrowid)

        conn.commit()
        conn.close()
