import sqlite3
import os

class Database:
    def __init__(self, db_name="app.db"):
        # Cria pasta database se não existir
        if not os.path.exists("database"):
            os.makedirs("database")
        self.db_name = os.path.join("database", db_name)

    def conectar(self):
        """Conecta no banco de dados SQLite"""
        return sqlite3.connect(self.db_name)

    def criar_tabelas(self):
        """Cria todas as tabelas do sistema"""

        conn = self.conectar()
        cursor = conn.cursor()

        # ------------------ UNIDADES ------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS unidades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                faixa_etaria INTEGER NOT NULL,
                genero TEXT NOT NULL
            )
        """)

        # ------------------ CLASSES ------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS classes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        """)

        # ------------------ USUARIOS ------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                genero TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL,
                tipo INTEGER NOT NULL,
                cargo TEXT,
                unidade_id INTEGER,
                classe_atual_id INTEGER,
                FOREIGN KEY (unidade_id) REFERENCES unidades(id),
                FOREIGN KEY (classe_atual_id) REFERENCES classes(id)
            )
        """)

        # ------------------ PROGRESSO_CLASSES ------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS progresso_classes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                desbravador_id INTEGER NOT NULL,
                classe_id INTEGER NOT NULL,
                progresso INTEGER NOT NULL,
                FOREIGN KEY (desbravador_id) REFERENCES usuarios(id),
                FOREIGN KEY (classe_id) REFERENCES classes(id)
            )
        """)

        conn.commit()
        conn.close()
