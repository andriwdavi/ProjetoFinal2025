from models.usuario import Usuario

class Lider(Usuario):
    def __init__(
        self,
        nome,
        idade,
        genero,
        email,
        senha,
        cargo,
        unidade_id,
        id=None
    ):
        super().__init__(nome, idade, genero, email, senha, tipo="LIDER", id=id)

        self._cargo = None
        self._unidade_id = None

        self.set_cargo(cargo)
        self.set_unidade_id(unidade_id)

    def get_cargo(self):
        return self._cargo

    def set_cargo(self, cargo):
        if isinstance(cargo, str) and len(cargo.strip()) >= 3:
            self._cargo = cargo.strip()
        else:
            raise ValueError("Cargo deve ter no mínimo 3 caracteres")


    def get_unidade_id(self):
        return self._unidade_id

    def set_unidade_id(self, unidade_id):
        if isinstance(unidade_id, int) and unidade_id > 0:
            self._unidade_id = unidade_id
        else:
            raise ValueError("Unidade ID deve ser um inteiro positivo")
