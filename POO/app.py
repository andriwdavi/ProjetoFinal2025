import streamlit as st

from database.db import Database
from DAO.usuario_dao import UsuarioDAO
from models.usuario import Usuario

from pages.login_page import mostrar_login
from pages.menu_page import mostrar_menu


st.set_page_config(
    page_title="Sistema",
    layout="centered"
)

# ==============================
# Inicialização do banco
# ==============================
db = Database()
db.criar_tabelas()

usuario_dao = UsuarioDAO()

# ==============================
# Usuário admin padrão (seed)
# ==============================
if not usuario_dao.buscar_por_email("admin@email.com"):
    admin = Usuario(
        nome="Administrador",
        idade=30,
        genero="Masculino",
        email="admin@email.com",
        senha="1234",
        tipo=1
    )
    usuario_dao.salvar(admin)

# ==============================
# Controle de sessão
# ==============================
if "usuario" not in st.session_state:
    mostrar_login()
else:
    mostrar_menu()

