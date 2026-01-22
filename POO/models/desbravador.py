from models.usuario import Usuario

class Desbravador(Usuario):
    def __init__(
        self,
        nome,
        idade,
        genero,
        email,
        senha,
        unidade_id,
        classe_atual_id,
        id=None
    ):
        super().__init__(nome, idade, genero, email, senha, tipo="DESBRAVADOR", id=id)

        self._unidade_id = None
        self._classe_atual_id = None

        self.set_unidade_id(unidade_id)
        self.set_classe_atual_id(classe_atual_id)

    def get_unidade_id(self):
        return self._unidade_id

    def set_unidade_id(self, unidade_id):
        if isinstance(unidade_id, int) and unidade_id > 0:
            self._unidade_id = unidade_id
        else:
            raise ValueError("Unidade ID deve ser um inteiro positivo")


    def get_classe_atual_id(self):
        return self._classe_atual_id

    def set_classe_atual_id(self, classe_atual_id):
        if isinstance(classe_atual_id, int) and classe_atual_id > 0:
            self._classe_atual_id = classe_atual_id
        else:
            raise ValueError("Classe atual ID deve ser um inteiro positivo")
