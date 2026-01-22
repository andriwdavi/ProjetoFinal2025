import streamlit as st
from DAO.usuario_dao import UsuarioDAO
from DAO.unidade_dao import UnidadeDAO
from models.usuario import Usuario

def inscrever_dbv():
    """
    Página para inscrever um desbravador no sistema.
    Apenas usuários Diretor ou Conselheiro podem inscrever.
    """

    usuario_logado = st.session_state["usuario"]

    # Verificação de acesso
    if usuario_logado.get_tipo() not in ["ADMIN", "CONSELHEIRO"]:
        st.error("Apenas Diretor ou Conselheiro podem inscrever desbravadores!")
        return

    st.title("Inscrever Desbravador")

    # Dados do desbravador
    nome = st.text_input("Nome")
    idade = st.number_input("Idade", min_value=10, max_value=100, step=1)
    genero = st.selectbox("Gênero", ["Masculino", "Feminino", "Outro"])
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    # Selecionar unidade
    unidade_dao = UnidadeDAO()
    unidade_dao.criar_tabela()
    unidades = unidade_dao.listar_todas()

    if not unidades:
        st.warning("Não há unidades cadastradas. Crie uma unidade primeiro.")
        return

    unidade_opcoes = {f"{u.get_nome()} ({u.get_faixa_etaria()} anos, {u.get_genero()})": u.get_id() for u in unidades}
    unidade_selecionada = st.selectbox("Unidade", list(unidade_opcoes.keys()))
    unidade_id = unidade_opcoes[unidade_selecionada]

    if st.button("Inscrever Desbravador"):
        if not nome.strip() or not email.strip() or not senha.strip():
            st.warning("Preencha todos os campos obrigatórios!")
            return

        try:
            novo_dbv = Usuario(
                nome=nome,
                idade=idade,
                genero=genero,
                email=email,
                senha=senha,
                tipo="DESBRAVADOR",
                unidade_id=unidade_id
            )

            usuario_dao = UsuarioDAO()
            usuario_dao.salvar(novo_dbv)

            st.success(f"✅ Desbravador '{novo_dbv.get_nome()}' inscrito com sucesso!")

        except Exception as e:
            st.error(f"Erro ao inscrever desbravador: {e}")
