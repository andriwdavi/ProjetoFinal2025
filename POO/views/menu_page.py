import streamlit as st
from views.criar_unidade_page import criar_unidade
from views.inscrever_dbv_page import inscrever_dbv
from views.listar_unidades_page import listar_unidades

def mostrar_menu():
    """
    Menu principal do sistema.
    Mostra opções de acordo com o tipo do usuário.
    """

    # Verifica se usuário está logado
    if "usuario" not in st.session_state:
        st.error("Você precisa estar logado!")
        return

    usuario = st.session_state["usuario"]

    st.title("Menu de Operações")
    st.write(f"👤 Usuário logado: **{usuario.get_nome()}**")
    st.write(f"📧 Email: {usuario.get_email()}")

    st.divider()

    # Define opções disponíveis dependendo do tipo
    opcoes = ["Início", "Meus Dados", "Listar Unidades", "Logout"]

    if usuario.get_tipo() == "ADMIN":
        opcoes.insert(1, "Criar Unidade")
        opcoes.insert(2, "Inscrever Desbravador")
    elif usuario.get_tipo() == "CONSELHEIRO":
        opcoes.insert(1, "Inscrever Desbravador")

    # Selectbox para escolher operação
    opcao = st.selectbox("Selecione uma opção:", opcoes)

    # Redireciona para a página escolhida
    if opcao == "Início":
        st.success("Bem-vindo ao sistema!")

    elif opcao == "Meus Dados":
        st.subheader("Dados do usuário")
        st.write(f"Nome: {usuario.get_nome()}")
        st.write(f"Idade: {usuario.get_idade()}")
        st.write(f"Gênero: {usuario.get_genero()}")
        st.write(f"Email: {usuario.get_email()}")

    elif opcao == "Criar Unidade":
        criar_unidade()

    elif opcao == "Inscrever Desbravador":
        inscrever_dbv()

    elif opcao == "Listar Unidades":
        listar_unidades()

    elif opcao == "Logout":
        st.session_state.clear()
        st.success("Logout realizado com sucesso!")
        st.rerun()
