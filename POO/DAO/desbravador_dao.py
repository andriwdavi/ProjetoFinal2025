import sqlite3
from models.desbravador import Desbravador

class DesbravadorDAO:
    def __init__(self, db_name="app.db"):
        self.db_name = db_name

    def salvar(self, d: Desbravador):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO usuarios
            (nome, idade, genero, email, senha, tipo, unidade_id, classe_atual_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            d.get_nome(),
            d.get_idade(),
            d.get_genero(),
            d.get_email(),
            d.get_senha(),
            d.get_tipo(),
            d.get_unidade_id(),
            d.get_classe_atual_id()
        ))

        d.set_id(cursor.lastrowid)

        conn.commit()
        conn.close()
