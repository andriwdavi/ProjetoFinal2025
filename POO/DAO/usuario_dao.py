import sqlite3
from models.usuario import Usuario

class UsuarioDAO:
    def __init__(self, db_name="app.db"):
        self.db_name = db_name

    def salvar(self, usuario: Usuario):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Mapeamento STRING -> INT
        tipo_map = {
            "ADMIN": 0,
            "LIDER": 1,
            "DESBRAVADOR": 2
        }

        cursor.execute("""
            INSERT INTO usuarios (nome, idade, genero, email, senha, tipo)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            usuario.get_nome(),
            usuario.get_idade(),
            usuario.get_genero(),
            usuario.get_email(),
            usuario.get_senha(),
            tipo_map[usuario.get_tipo()]  # 👈 conversão aqui
        ))

        usuario._id = cursor.lastrowid

        conn.commit()
        conn.close()

    def buscar_por_id(self, id: int) -> Usuario | None:
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, idade, genero, email, senha, tipo
            FROM usuarios
            WHERE id = ?
        """, (id,))

        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            return Usuario(
                id=resultado[0],
                nome=resultado[1],
                idade=resultado[2],
                genero=resultado[3],
                email=resultado[4],
                senha=resultado[5],
                tipo=resultado[6]  # 👈 agora o set_tipo sabe lidar com int
            )

        return None

    def buscar_por_email(self, email: str) -> Usuario | None:
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, idade, genero, email, senha, tipo
            FROM usuarios
            WHERE email = ?
        """, (email,))

        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            return Usuario(
                id=resultado[0],
                nome=resultado[1],
                idade=resultado[2],
                genero=resultado[3],
                email=resultado[4],
                senha=resultado[5],
                tipo=resultado[6]
            )

        return None
