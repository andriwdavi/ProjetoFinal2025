import streamlit as st
from DAO.unidade_dao import UnidadeDAO
from models.unidade import Unidade


def editar_unidade():
    st.subheader("✏️ Editar Unidade")

    dao = UnidadeDAO()
    unidades = dao.listar_todas()

    if not unidades:
        st.info("Nenhuma unidade cadastrada.")
        return

    # Mapeia unidades para o selectbox
    mapa_unidades = {
        f"{u.get_nome()} (ID {u.get_id()})": u
        for u in unidades
    }

    unidade_selecionada_label = st.selectbox(
        "Selecione a unidade",
        list(mapa_unidades.keys())
    )

    unidade = mapa_unidades[unidade_selecionada_label]

    # --- CAMPOS ---
    novo_nome = st.text_input(
        "Nome da unidade",
        value=unidade.get_nome()
    )

    faixas = [10, 11, 12, 13, 14, 15]
    faixa_etaria = st.selectbox(
        "Faixa etária",
        faixas,
        index=faixas.index(unidade.get_faixa_etaria())
    )

    generos = ["M", "F", "MISTO"]

    # 🔥 AQUI ESTÁ O FIX DO ERRO
    genero_atual = unidade.get_genero().upper()
    if genero_atual not in generos:
        genero_atual = "MISTO"

    genero = st.selectbox(
        "Gênero da unidade",
        generos,
        index=generos.index(genero_atual)
    )

    # --- BOTÃO ---
    if st.button("💾 Salvar alterações"):
        try:
            unidade.set_nome(novo_nome)
            unidade.set_faixa_etaria(faixa_etaria)
            unidade.set_genero(genero)

            dao.atualizar(unidade)

            st.success("Unidade atualizada com sucesso!")
            st.rerun()

        except ValueError as e:
            st.error(str(e))
