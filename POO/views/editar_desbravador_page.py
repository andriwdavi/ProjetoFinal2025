import streamlit as st
from DAO.usuario_dao import UsuarioDAO
from DAO.unidade_dao import UnidadeDAO


def editar_desbravador():
    st.subheader("✏️ Editar Desbravador")

    usuario_dao = UsuarioDAO()
    unidade_dao = UnidadeDAO()

    desbravadores = usuario_dao.listar_desbravadores()
    unidades = unidade_dao.listar_todas()

    if not desbravadores:
        st.info("Nenhum desbravador cadastrado.")
        return

    if not unidades:
        st.warning("Nenhuma unidade cadastrada.")
        return

    mapa_desbravadores = {
        f"{d.get_nome()} (ID {d.get_id()})": d
        for d in desbravadores
    }

    label_desbravador = st.selectbox(
        "Selecione o desbravador",
        list(mapa_desbravadores.keys())
    )

    desbravador = mapa_desbravadores[label_desbravador]

    genero_atual = desbravador.get_genero()

    if genero_atual == "Masculino":
        genero_atual = "M"
    elif genero_atual == "Feminino":
        genero_atual = "F"

    nome = st.text_input("Nome", desbravador.get_nome())
    idade = st.number_input(
        "Idade",
        min_value=10,
        max_value=15,
        value=desbravador.get_idade()
    )

    genero = st.selectbox(
        "Gênero",
        ["M", "F"],
        index=["M", "F"].index(genero_atual)
    )

    mapa_unidades = {
        f"{u.get_nome()} (ID {u.get_id()})": u
        for u in unidades
    }

    unidade_atual_id = desbravador.get_unidade_id()

    index_unidade = 0
    for i, u in enumerate(unidades):
        if u.get_id() == unidade_atual_id:
            index_unidade = i
            break

    unidade_label = st.selectbox(
        "Unidade",
        list(mapa_unidades.keys()),
        index=index_unidade
    )

    nova_unidade = mapa_unidades[unidade_label]

    if st.button("💾 Salvar alterações"):
        try:
            desbravador.set_nome(nome)
            desbravador.set_idade(idade)

            if genero == "M":
                desbravador.set_genero("Masculino")
            else:
                desbravador.set_genero("Feminino")

            desbravador.set_unidade_id(nova_unidade.get_id())

            usuario_dao.atualizar(desbravador)

            st.success("Desbravador atualizado com sucesso!")
            st.rerun()

        except ValueError as e:
            st.error(str(e))
