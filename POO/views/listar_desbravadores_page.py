import streamlit as st
from DAO.usuario_dao import UsuarioDAO

def listar_desbravadores():
    st.title("👥 Desbravadores")

    usuario_logado = st.session_state["usuario"]

    dao = UsuarioDAO()
    desbravadores = dao.listar_desbravadores()

    if not desbravadores:
        st.warning("Nenhum desbravador cadastrado.")
        return

    for d in desbravadores:
        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(
                f"👤 **{d.get_nome()}** | "
                f"{d.get_idade()} anos | "
                f"{d.get_genero()} | "
                f"{d.get_email()}"
            )

        with col2:
            # somente diretor pode excluir
            if usuario_logado.get_tipo() == "ADMIN":
                if st.button("❌ Excluir", key=f"del_dbv_{d.get_id()}"):
                    dao.excluir(d.get_id())
                    st.success("Desbravador excluído!")
                    st.rerun()
