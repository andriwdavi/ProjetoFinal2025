import streamlit as st
from DAO.usuario_dao import UsuarioDAO

def mostrar_login():
    st.title("Login")

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        dao = UsuarioDAO()
        usuario = dao.buscar_por_email(email)

        if usuario and usuario.senha == senha:
            st.session_state["usuario"] = usuario
            st.success("Login realizado com sucesso!")
            st.rerun()
        else:
            st.error("Email ou senha inválidos")
