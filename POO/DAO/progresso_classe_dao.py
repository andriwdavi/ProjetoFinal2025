import sqlite3
from models.progresso_classe import ProgressoClasse

class ProgressoClasseDAO:
    def __init__(self, db_name="app.db"):
        self.db_name = db_name

    def salvar(self, p: ProgressoClasse):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO progresso_classes
            (desbravador_id, classe_id, progresso)
            VALUES (?, ?, ?)
        """, (
            p.get_desbravador_id(),
            p.get_classe_id(),
            p.get_progresso()
        ))

        p.set_id(cursor.lastrowid)

        conn.commit()
        conn.close()
