class ProgressoClasse:
    def __init__(self, desbravador_id, classe_id, progresso, id=None):
        self._id = None
        self.set_id(id)
        self.set_desbravador_id(desbravador_id)
        self.set_classe_id(classe_id)
        self.set_progresso(progresso)

    def get_id(self):
        return self._id

    def set_id(self, id):
        if id is None or id > 0:
            self._id = id
        else:
            raise ValueError("ID deve ser positivo")


    def get_desbravador_id(self):
        return self._desbravador_id

    def set_desbravador_id(self, desbravador_id):
        if isinstance(desbravador_id, int) and desbravador_id > 0:
            self._desbravador_id = desbravador_id
        else:
            raise ValueError("Desbravador ID deve ser um inteiro positivo")


    def get_classe_id(self):
        return self._classe_id

    def set_classe_id(self, classe_id):
        if isinstance(classe_id, int) and classe_id > 0:
            self._classe_id = classe_id
        else:
            raise ValueError("Classe ID deve ser um inteiro positivo")


    def get_progresso(self):
        return self._progresso

    def set_progresso(self, progresso):
        if isinstance(progresso, int) and 0 <= progresso <= 5:
            self._progresso = progresso
        else:
            raise ValueError("Progresso deve estar entre 0 e 5")
