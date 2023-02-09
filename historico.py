import datetime

class Historico():

    def __init__(self):
        self._dataDeabertura = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
        self._trasacoes = []
    
    @property
    def dataDeabertura(self):
        return self._dataDeabertura
    
    @dataDeabertura.setter
    def dataDeabertura(self):
        self._dataDeabertura = datetime.datetime.today().strftime("%d/%m/%y %H:%M")

    @property
    def trasacoes(self):
        return self._trasacoes
    
    @trasacoes.setter
    def trasacoes(self, valor):
        self._trasacoes.append(valor)

    def imprimir(self):
        text = ''
        text = f"Data de de abertura: {self.dataDeabertura}\n\nTransações:\n\n"
        for valor in self.trasacoes:
            text += f"- {valor}\n\n"
        return text
