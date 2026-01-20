from database.db import Database
from models.usuario import Usuario
from DAO.usuario_dao import UsuarioDAO


def main():
    # 1️⃣ Criar banco e tabelas
    db = Database()
    db.criar_tabelas()

    # 2️⃣ Criar DAO
    usuario_dao = UsuarioDAO()

    # 3️⃣ Criar objeto Usuario
    usuario = Usuario(
        nome="João",
        idade=25,
        genero="M",
        email="joao@email.com",
        senha="123456"
    )

    # 4️⃣ Salvar no banco
    usuario_dao.salvar(usuario)
    print(f"Usuário salvo com ID: {usuario.id}")

    # 5️⃣ Buscar o usuário pelo ID
    usuario_lido = usuario_dao.buscar_por_id(usuario.id)

    # 6️⃣ Mostrar resultado
    if usuario_lido:
        print("Usuário recuperado do banco:")
        print(
            usuario_lido.id,
            usuario_lido.nome,
            usuario_lido.idade,
            usuario_lido.genero,
            usuario_lido.email
        )
    else:
        print("Usuário não encontrado.")


if __name__ == "__main__":
    main()
