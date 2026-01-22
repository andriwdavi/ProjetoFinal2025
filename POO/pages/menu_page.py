import streamlit as st

def mostrar_menu():
    usuario = st.session_state["usuario"]

    st.title("Menu do Sistema")
    st.write(f"Bem-vindo, **{usuario.get_nome()}**")

    opcao = st.selectbox(
        "Escolha uma opção:",
        ["Mostrar meus dados", "Logout"]
    )

    if opcao == "Mostrar meus dados":
        st.write(f"Nome: {usuario.get_nome()}")
        st.write(f"Email: {usuario.get_email()}")
        st.write(f"Tipo: {usuario.get_tipo()}")

    elif opcao == "Logout":
        if st.button("Confirmar logout"):
            del st.session_state["usuario"]
            st.success("Logout realizado")
            st.rerun()
