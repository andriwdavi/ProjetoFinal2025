class Usuario:
    def __init__(
            self,
            nome: str,
            idade: int,
            genero: str,
            email: str,
            senha: str,
            tipo=None,
            id: int | None = None
    ):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.email = email
        self.senha = senha
        self.tipo = tipo
