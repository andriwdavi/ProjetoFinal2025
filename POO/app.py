import streamlit as st

from database.db import Database
from DAO.usuario_dao import UsuarioDAO
from models.usuario import Usuario

from views.login_page import mostrar_login
from views.menu_page import mostrar_menu


st.set_page_config(
    page_title="Sistema",
    layout="centered",
    initial_sidebar_state="collapsed"
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
if not usuario_dao.buscar_por_email("diretor@email.com"):
    diretor = Usuario(
        nome="Diretor",
        idade=35,
        genero="Masculino",
        email="diretor@email.com",
        senha="1234",
        tipo=0
    )
    usuario_dao.salvar(diretor)

# ==============================
# Controle de sessão
# ==============================
if "usuario" not in st.session_state:
    mostrar_login()
else:
    mostrar_menu()

