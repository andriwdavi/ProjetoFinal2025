import sqlite3
from models.usuario import Usuario

class UsuarioDAO:
    def __init__(self, db_name="database/app.db"):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)

    # ------------------ Salvar usuário ------------------
    def salvar(self, usuario: Usuario):
        conn = self.conectar()
        cursor = conn.cursor()

        tipo_map = {
            "ADMIN": 0,
            "LIDER": 1,
            "DESBRAVADOR": 2
        }

        cursor.execute("""
            INSERT INTO usuarios (nome, idade, genero, email, senha, tipo, unidade_id, classe_atual_id)
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

    # ------------------ Buscar por ID ------------------
    def buscar_por_id(self, id: int) -> Usuario | None:
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, idade, genero, email, senha, tipo, unidade_id, classe_atual_id
            FROM usuarios
            WHERE id = ?
        """, (id,))

        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            tipo_map = {0: "ADMIN", 1: "LIDER", 2: "DESBRAVADOR"}
            tipo_str = tipo_map.get(resultado[6], "DESBRAVADOR")

            return Usuario(
                id=resultado[0],
                nome=resultado[1],
                idade=resultado[2],
                genero=resultado[3],
                email=resultado[4],
                senha=resultado[5],
                tipo=tipo_str,
                unidade_id=resultado[7],
                classe_atual_id=resultado[8]
            )

        return None

    # ------------------ Buscar por email ------------------
    def buscar_por_email(self, email: str) -> Usuario | None:
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, idade, genero, email, senha, tipo, unidade_id, classe_atual_id
            FROM usuarios
            WHERE email = ?
        """, (email,))

        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            tipo_map = {0: "ADMIN", 1: "LIDER", 2: "DESBRAVADOR"}
            tipo_str = tipo_map.get(resultado[6], "DESBRAVADOR")

            return Usuario(
                id=resultado[0],
                nome=resultado[1],
                idade=resultado[2],
                genero=resultado[3],
                email=resultado[4],
                senha=resultado[5],
                tipo=tipo_str,
                unidade_id=resultado[7],
                classe_atual_id=resultado[8]
            )

        return None

    def listar_desbravadores(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, idade, genero, email, senha, tipo, unidade_id, classe_atual_id
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
                    tipo="DESBRAVADOR"
                )
            )

        return desbravadores
    
    def atualizar(self, usuario: Usuario):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        tipo_map = {
            "ADMIN": 0,
            "LIDER": 1,
            "DESBRAVADOR": 2
        }

        cursor.execute("""
            UPDATE usuarios
            SET nome = ?, idade = ?, genero = ?, email = ?, senha = ?, tipo = ?, unidade_id = ?, classe_atual_id = ?
            WHERE id = ?
        """, (
            usuario.get_nome(),
            usuario.get_idade(),
            usuario.get_genero(),
            usuario.get_email(),
            usuario.get_senha(),
            tipo_map[usuario.get_tipo()],
            usuario.unidade_id,
            usuario.classe_atual_id,
            usuario.get_id()
        ))

        conn.commit()
        conn.close()

    def excluir(self, usuario_id: int):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM usuarios WHERE id = ?",
            (usuario_id,)
        )

        conn.commit()
        conn.close()
