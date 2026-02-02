class Unidade:
    def __init__(self, nome, faixa_etaria, genero, id=None):
        self._id = None
        self.set_id(id)
        self.set_nome(nome)
        self.set_faixa_etaria(faixa_etaria)
        self.set_genero(genero)

    # ID
    def get_id(self):
        return self._id

    def set_id(self, id):
        if id is None or id > 0:
            self._id = id
        else:
            raise ValueError("ID deve ser positivo")

    # Nome
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        if nome and len(nome) >= 3:
            self._nome = nome
        else:
            raise ValueError("Nome da unidade deve ter pelo menos 3 caracteres")

    # Faixa etária
    def get_faixa_etaria(self):
        return self._faixa_etaria

    def set_faixa_etaria(self, faixa_etaria):
        valores_permitidos = [10, 11, 12, 13, 14, 15]
        if faixa_etaria in valores_permitidos:
            self._faixa_etaria = faixa_etaria
        else:
            raise ValueError(f"Faixa etária inválida! Deve ser um dos valores: {valores_permitidos}")

    # Gênero
    def get_genero(self):
        return self._genero

    def set_genero(self, genero):
        if genero:
            self._genero = genero
        else:
            raise ValueError("Gênero não pode ser vazio")
