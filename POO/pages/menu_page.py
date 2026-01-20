import streamlit as st

def mostrar_menu():
    usuario = st.session_state["usuario"]

    st.title("Menu do Sistema")
    st.write(f"Bem-vindo, **{usuario.nome}**")

    opcao = st.selectbox(
        "Escolha uma opção:",
        ["Mostrar meus dados", "Logout"]
    )

    if opcao == "Mostrar meus dados":
        st.write(f"Nome: {usuario.nome}")
        st.write(f"Email: {usuario.email}")

    elif opcao == "Logout":
        if st.button("Confirmar logout"):
            del st.session_state["usuario"]
            st.success("Logout realizado")
            st.rerun()
