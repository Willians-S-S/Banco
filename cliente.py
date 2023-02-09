class Cliente():

    __slots__ = ['_nome', '_cpf']

    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):   
        self._nome = valor
    
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, valor):
        self._cpf = valor

    def dadosDoCliente(self):
        return f"Nome completo: {self.nome}\nCPF: {self.cpf}\n"
