class Usuario:
    def __init__(
        self,
        nome,
        idade,
        genero,
        email,
        senha,
        tipo,
        id=None,
        unidade_id=None,
        classe_atual_id=None
    ):
        self._id = None
        self._unidade_id = None
        self._classe_atual_id = None

        self.set_id(id)
        self.set_nome(nome)
        self.set_idade(idade)
        self.set_genero(genero)
        self.set_email(email)
        self.set_senha(senha)
        self.set_tipo(tipo)
        self.set_unidade_id(unidade_id)
        self.set_classe_atual_id(classe_atual_id)

    # ------------------ ID ------------------
    def get_id(self):
        return self._id

    def set_id(self, id):
        if id is None:
            self._id = None
        elif isinstance(id, int) and id > 0:
            self._id = id
        else:
            raise ValueError("ID deve ser um inteiro positivo")

    # ------------------ Nome ------------------
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        if nome and len(nome) >= 3:
            self._nome = nome
        else:
            raise ValueError("Nome deve ter pelo menos 3 caracteres")

    # ------------------ Idade ------------------
    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
        if isinstance(idade, int) and 0 <= idade <= 100:
            self._idade = idade
        else:
            raise ValueError("Idade inválida")

    # ------------------ Gênero ------------------
    def get_genero(self):
        return self._genero

    def set_genero(self, genero):
        if genero:
            self._genero = genero
        else:
            raise ValueError("Gênero não pode ser vazio")

    # ------------------ Email ------------------
    def get_email(self):
        return self._email

    def set_email(self, email):
        if email and "@" in email:
            self._email = email
        else:
            raise ValueError("Email inválido")

    # ------------------ Senha ------------------
    def get_senha(self):
        return self._senha

    def set_senha(self, senha):
        if senha and len(senha) >= 3:
            self._senha = senha
        else:
            raise ValueError("Senha deve ter pelo menos 3 caracteres")

    # ------------------ Tipo ------------------
    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        mapa_int_para_str = {
            0: "ADMIN",
            1: "LIDER",
            2: "DESBRAVADOR"
        }

        if isinstance(tipo, str) and tipo.isdigit():
            tipo = int(tipo)

        if isinstance(tipo, int) and tipo in mapa_int_para_str:
            self._tipo = mapa_int_para_str[tipo]
        elif isinstance(tipo, str) and tipo in mapa_int_para_str.values():
            self._tipo = tipo
        else:
            raise ValueError("Tipo de usuário inválido")

    # ------------------ Unidade ------------------
    def get_unidade_id(self):
        return self._unidade_id

    def set_unidade_id(self, unidade_id):
        if unidade_id is None:
            self._unidade_id = None
        elif isinstance(unidade_id, int) and unidade_id > 0:
            self._unidade_id = unidade_id
        else:
            raise ValueError("Unidade inválida")

    # ------------------ Classe Atual ------------------
    def get_classe_atual_id(self):
        return self._classe_atual_id

    def set_classe_atual_id(self, classe_id):
        if classe_id is None or (isinstance(classe_id, int) and classe_id > 0):
            self._classe_atual_id = classe_id
        else:
            raise ValueError("Classe atual ID inválido")
