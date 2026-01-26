import streamlit as st
from DAO.unidade_dao import UnidadeDAO

def listar_unidades():
    st.title("📋 Unidades")

    usuario = st.session_state["usuario"]

    dao = UnidadeDAO()
    unidades = dao.listar_todas()

    if not unidades:
        st.warning("Nenhuma unidade cadastrada.")
        return

    for unidade in unidades:
        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(
                f"🏕 **{unidade.get_nome()}** | "
                f"Faixa etária: {unidade.get_faixa_etaria()} | "
                f"Gênero: {unidade.get_genero()}"
            )

        with col2:
            if usuario.get_tipo() == "ADMIN":
                if st.button("❌ Excluir", key=f"del_unidade_{unidade.get_id()}"):
                    dao.excluir(unidade.get_id())
                    st.success("Unidade excluída com sucesso!")
                    st.rerun()
