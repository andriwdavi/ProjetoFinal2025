import sqlite3

class Database:
    def __init__(self, db_name="app.db"):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def criar_tabelas(self):
        conn = self.conectar()
        cursor = conn.cursor()

        # Tabela UNIDADES
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS unidades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        """)

        # Tabela CLASSES
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS classes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        """)

        # Tabela USUARIOS
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                genero TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL,
                tipo TEXT NOT NULL,
                cargo TEXT,
                unidade_id INTEGER,
                classe_atual_id INTEGER,
                FOREIGN KEY (unidade_id) REFERENCES unidades(id),
                FOREIGN KEY (classe_atual_id) REFERENCES classes(id)
            )
        """)

        # Tabela PROGRESSO_CLASSES
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
