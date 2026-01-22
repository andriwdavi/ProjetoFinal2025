class Classe:
    def __init__(self, nome, nivel, id=None):
        self._id = None
        self.set_id(id)
        self.set_nome(nome)
        self.set_nivel(nivel)

    def get_id(self):
        return self._id

    def set_id(self, id):
        if id is None or id > 0:
            self._id = id
        else:
            raise ValueError("ID deve ser positivo")


    def get_id(self):
        return self._id

    def set_id(self, id):
        if id is None or id > 0:
            self._id = id
        else:
            raise ValueError("ID deve ser positivo")


    def get_nivel(self):
        return self._nivel

    def set_nivel(self, nivel):
        if isinstance(nivel, int) and nivel > 0:
            self._nivel = nivel
        else:
            raise ValueError("Nível deve ser um número inteiro positivo")
