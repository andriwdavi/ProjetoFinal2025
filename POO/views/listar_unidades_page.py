import streamlit as st
from DAO.unidade_dao import UnidadeDAO

def listar_unidades():
    st.title("📋 Lista de Unidades")

    dao = UnidadeDAO()
    dao.criar_tabela()  # garante que a tabela de unidades exista

    unidades = dao.listar_unidades_com_desbravadores()

    if not unidades:
        st.warning("Nenhuma unidade cadastrada ainda.")
        return

    for item in unidades:
        unidade = item["unidade"]
        desbravadores = item["desbravadores"]

        st.subheader(f"🏕 Unidade: {unidade.get_nome()} ({unidade.get_faixa_etaria()} anos, {unidade.get_genero()})")

        if desbravadores:
            st.write("👥 Desbravadores inscritos:")
            for d in desbravadores:
                st.write(f"- {d.get_nome()} | {d.get_idade()} anos | {d.get_email()}")
        else:
            st.write("Nenhum desbravador inscrito nesta unidade.")

        st.divider()
