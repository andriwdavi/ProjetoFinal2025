import streamlit as st
from DAO.unidade_dao import UnidadeDAO
from models.unidade import Unidade

def mostrar_cadastro_unidade():
    st.title("Cadastro de Unidade")

    # 🔒 Verificação de permissão
    if "usuario" not in st.session_state:
        st.error("Você precisa estar logado.")
        return

    if st.session_state.usuario.get_tipo() != "ADMIN":
        st.error("Acesso negado. Apenas administradores podem cadastrar unidades.")
        return

    nome = st.text_input("Nome da unidade")

    if st.button("Salvar"):
        try:
            unidade = Unidade(nome=nome)
            dao = UnidadeDAO()
            dao.salvar(unidade)

            st.success("Unidade cadastrada com sucesso!")
        except Exception as e:
            st.error(str(e))
