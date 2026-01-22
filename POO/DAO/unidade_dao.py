import sqlite3
from models.unidade import Unidade
from models.usuario import Usuario

class UnidadeDAO:
    def __init__(self, db_name="database/app.db"):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)

    # ------------------ Criar tabela ------------------
    def criar_tabela(self):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS unidades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                faixa_etaria INTEGER NOT NULL,
                genero TEXT NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    # ------------------ Salvar unidade ------------------
    def salvar(self, unidade: Unidade):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO unidades (nome, faixa_etaria, genero)
            VALUES (?, ?, ?)
        """, (
            unidade.get_nome(),
            unidade.get_faixa_etaria(),
            unidade.get_genero()
        ))

        unidade.set_id(cursor.lastrowid)

        conn.commit()
        conn.close()

    # ------------------ Listar todas as unidades ------------------
    def listar_todas(self):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT id, nome, faixa_etaria, genero FROM unidades")
        linhas = cursor.fetchall()
        conn.close()

        unidades = []
        for l in linhas:
            unidades.append(Unidade(
                id=l[0],
                nome=l[1],
                faixa_etaria=l[2],
                genero=l[3]
            ))
        return unidades

    # ------------------ Listar unidades com desbravadores ------------------
    def listar_unidades_com_desbravadores(self):
        """
        Retorna uma lista de unidades e para cada unidade uma lista de desbravadores nela
        """
        conn = self.conectar()
        cursor = conn.cursor()

        # Buscar todas as unidades
        cursor.execute("SELECT id, nome, faixa_etaria, genero FROM unidades")
        unidades_raw = cursor.fetchall()

        resultado = []

        for unidade_row in unidades_raw:
            unidade_id = unidade_row[0]
            unidade = Unidade(
                id=unidade_id,
                nome=unidade_row[1],
                faixa_etaria=unidade_row[2],
                genero=unidade_row[3]
            )

            # Buscar desbravadores dessa unidade
            cursor.execute("""
                SELECT id, nome, idade, genero, email, senha, tipo, unidade_id, classe_atual_id
                FROM usuarios
                WHERE unidade_id = ? AND tipo = 2
            """, (unidade_id,))

            desbravadores_raw = cursor.fetchall()
            desbravadores = []

            for d in desbravadores_raw:
                desbravador = Usuario(
                    id=d[0],
                    nome=d[1],
                    idade=d[2],
                    genero=d[3],
                    email=d[4],
                    senha=d[5],
                    tipo="DESBRAVADOR",
                    unidade_id=d[7],
                    classe_atual_id=d[8]
                )
                desbravadores.append(desbravador)

            resultado.append({
                "unidade": unidade,
                "desbravadores": desbravadores
            })

        conn.close()
        return resultado
