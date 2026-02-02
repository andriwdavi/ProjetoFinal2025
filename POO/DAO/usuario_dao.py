import sqlite3
from models.usuario import Usuario


class UsuarioDAO:
    def __init__(self, db_name="database/app.db"):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)

    # ------------------ SALVAR ------------------
    def salvar(self, usuario: Usuario):
        conn = self.conectar()
        cursor = conn.cursor()

        tipo_map = {
            "ADMIN": 0,
            "LIDER": 1,
            "DESBRAVADOR": 2
        }

        cursor.execute("""
            INSERT INTO usuarios (
                nome, idade, genero, email, senha, tipo, unidade_id, classe_atual_id
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            usuario.get_nome(),
            usuario.get_idade(),
            usuario.get_genero(),
            usuario.get_email(),
            usuario.get_senha(),
            tipo_map[usuario.get_tipo()],
            usuario.get_unidade_id(),
            usuario.get_classe_atual_id()
        ))

        usuario.set_id(cursor.lastrowid)

        conn.commit()
        conn.close()

    # ------------------ BUSCAR POR ID ------------------
    def buscar_por_id(self, id: int) -> Usuario | None:
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, idade, genero, email, senha, tipo, unidade_id, classe_atual_id
            FROM usuarios
            WHERE id = ?
        """, (id,))

        row = cursor.fetchone()
        conn.close()

        if not row:
            return None

        tipo_map = {0: "ADMIN", 1: "LIDER", 2: "DESBRAVADOR"}

        return Usuario(
            id=row[0],
            nome=row[1],
            idade=row[2],
            genero=row[3],
            email=row[4],
            senha=row[5],
            tipo=tipo_map[row[6]],
            unidade_id=row[7],
            classe_atual_id=row[8]
        )

    # ------------------ BUSCAR POR EMAIL ------------------
    def buscar_por_email(self, email: str) -> Usuario | None:
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, idade, genero, email, senha, tipo, unidade_id, classe_atual_id
            FROM usuarios
            WHERE email = ?
        """, (email,))

        row = cursor.fetchone()
        conn.close()

        if not row:
            return None

        tipo_map = {0: "ADMIN", 1: "LIDER", 2: "DESBRAVADOR"}

        return Usuario(
            id=row[0],
            nome=row[1],
            idade=row[2],
            genero=row[3],
            email=row[4],
            senha=row[5],
            tipo=tipo_map[row[6]],
            unidade_id=row[7],
            classe_atual_id=row[8]
        )

    # ------------------ LISTAR DESBRAVADORES ------------------
    def listar_desbravadores(self):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, idade, genero, email, senha, unidade_id, classe_atual_id
            FROM usuarios
            WHERE tipo = 2
        """)

        rows = cursor.fetchall()
        conn.close()

        desbravadores = []

        for r in rows:
            desbravadores.append(
                Usuario(
                    id=r[0],
                    nome=r[1],
                    idade=r[2],
                    genero=r[3],
                    email=r[4],
                    senha=r[5],
                    tipo="DESBRAVADOR",
                    unidade_id=r[6],
                    classe_atual_id=r[7]
                )
            )

        return desbravadores

    # ------------------ ATUALIZAR ------------------
    def atualizar(self, usuario: Usuario):
        conn = self.conectar()
        cursor = conn.cursor()

        tipo_map = {
            "ADMIN": 0,
            "LIDER": 1,
            "DESBRAVADOR": 2
        }

        cursor.execute("""
            UPDATE usuarios
            SET
                nome = ?,
                idade = ?,
                genero = ?,
                email = ?,
                senha = ?,
                tipo = ?,
                unidade_id = ?,
                classe_atual_id = ?
            WHERE id = ?
        """, (
            usuario.get_nome(),
            usuario.get_idade(),
            usuario.get_genero(),
            usuario.get_email(),
            usuario.get_senha(),
            tipo_map[usuario.get_tipo()],
            usuario.get_unidade_id(),
            usuario.get_classe_atual_id(),
            usuario.get_id()
        ))

        conn.commit()
        conn.close()

    # ------------------ EXCLUIR ------------------
    def excluir(self, usuario_id: int):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM usuarios WHERE id = ?",
            (usuario_id,)
        )

        conn.commit()
        conn.close()
