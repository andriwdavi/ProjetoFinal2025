import streamlit as st
from DAO.unidade_dao import UnidadeDAO
from models.unidade import Unidade

def criar_unidade():
    """
    Página para criar uma nova unidade.
    Apenas usuários do tipo 'Diretor' podem acessar.
    """

    usuario = st.session_state["usuario"]

    # Verifica se é diretor
    if usuario.get_tipo() != "ADMIN":
        st.error("Apenas o Diretor pode criar unidades!")
        return

    st.title("Criar Nova Unidade")

    # Nome da unidade
    nome = st.text_input("Nome da Unidade")

    # Faixa etária: apenas 10, 11, 12, 13, 14 ou 15
    faixa_etaria = st.selectbox("Faixa Etária", [10, 11, 12, 13, 14, 15])

    # Gênero da unidade
    genero = st.selectbox("Gênero", ["Masculino", "Feminino", "Misto"])

    if st.button("Criar Unidade"):
        # Valida campos
        if not nome.strip():
            st.warning("O nome da unidade não pode estar vazio!")
            return

        try:
            # Cria objeto Unidade
            unidade = Unidade(nome=nome, faixa_etaria=faixa_etaria, genero=genero)

            # Salva no banco
            dao = UnidadeDAO()
            dao.criar_tabela()  
            dao.salvar(unidade)

            st.success(f"✅ Unidade '{unidade.get_nome()}' criada com sucesso!")

        except ValueError as e:
            st.error(f"Erro ao criar unidade: {e}")
