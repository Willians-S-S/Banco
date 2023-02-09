import mysql.connector as mysql
import datetime 
from cliente import *
from historico import *
import datetime
from random import randint

class Conta():

    __slots__ = ['_numero','_titular', 'saldo', '_limite', '_historico', '_senha', '_usuario', 'conexao', 'cursor']
    _totalContas = 0

    def __init__(self):
        self._titular = ''
        self._numero = 0
        self.saldo = 0.0
        self._limite = 0.0
        self._usuario = ''
        self._senha = ''
        self.conexao = mysql.connect(host='localhost', db='conta', user='root', password='Tales of demons', autocommit=True)
        self.cursor = self.conexao.cursor()
        Conta.set_totalContas()

    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, valor):   
        self._numero = valor

    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, valor):   
        self._titular = valor
    
    @property
    def usuario(self):
        return self._usuario
    
    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario
    
    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        self._senha = senha
    
    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, valor):   
        self._limite = valor
    
    @property
    def historico(self):
        return self._historico
    
    @historico.setter
    def historico(self, valor):   
        self._historico = valor
    
    def add_conta(self, usuario, senha, nome, cpf, saldo = 0.0, limite = 1000.0):
        if not self.verificarCPF(cpf):
            if not self.verificarUsuario(usuario):
                self.titular = Cliente(nome, cpf)
                self.historico = Historico()
                data = datetime.datetime.today().strftime("%d/%m/%y %H:%M")
                while True:
                    numero = randint(100, 999)
                    if not self.verificarNumero(numero):
                        self.numero = numero
                        break
                query = f'INSERT INTO cliente(cpf, nome, usuario, senha, numero, saldo, limite, historico) VALUES ("{cpf}", "{nome}", "{usuario}", MD5("{senha}"), {numero}, {saldo}, {limite}, "Data de de abertura: {data}")'
                self.cursor.execute(query)
                self.cursor.execute('select * from cliente')
                print(self.cursor.fetchall())
                return True, "Cadastro realizado com sucesso."
            else:
                return False, 'Usuário já estar cadastrado.'
        else:
            return False, 'CPF já estar cadastrado.'
    
    def login(self, usuario, senha):
        flag = self.verificarUsuario(usuario, senha, False)
        if flag[0]:
            self.cursor.execute(f'select nome, saldo, numero from cliente where usuario = "{usuario}"')
            resul = self.cursor.fetchall()
            print(resul)
            return True, resul
        else:
            return flag

    def verificarUsuario(self, usuario, senha = None, flag = True):
        if flag:
            self.cursor.execute(f'SELECT usuario FROM cliente WHERE usuario = "{usuario}"')
            exists = self.cursor.fetchall()
            if exists:
                return True
            else:
                return False
        else:
            self.cursor.execute(f'SELECT usuario, senha FROM cliente WHERE usuario = "{usuario}" and senha = MD5("{senha}")')
            exists = self.cursor.fetchall()
            if exists:
                return True, 'Exite.'
            else:
                return False, 'Usuário ou senha não encontrado.'
    
    def verificarCPF(self, cpf):
        self.cursor.execute(f'SELECT cpf FROM cliente WHERE cpf = "{cpf}"')
        exists = self.cursor.fetchall()
        if exists:
            return True
        else:
            return False

    def verificarNumero(self, numero):
        self.cursor.execute(f'SELECT numero FROM cliente WHERE numero = "{numero}"')
        exists = self.cursor.fetchall()
        if exists:
            return True
        else:
            return False

    def depositar(self, valor, flag=True):
        if self._limite < valor or valor <= 0 or self.saldo + valor > self.limite:
            data = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
            return False, "Não foi possível fazer o deposito."
        else:
            self.saldo += valor
            data = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
            if flag:
                self.historico.trasacoes = f" Deposito\n      Valor: {valor:.2f}\n       Data: {data}"
            return True, "Deposito realizado com sucesso."
    
    def sacar(self, valor, flag=True):
        if valor > self.saldo or valor <= 0:
            data = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
            #self.historico.trasacoes = f"Tentativa de saque de {valor} na data e hora {data}"
            return False, "Valor maior que o saldo ou valor menor que 0."
        else:
            self.saldo -= valor
            data = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
            if flag:
                self.historico.trasacoes = f" Saque\n      Valor: {valor:.2f}\n       Data: {data}"
            return True, "Saque realizado com sucesso."

    def transfere(self, destino, valor):
        retirou = self.sacar(valor, False)
        if retirou:
            destino.depositar(valor, False)
            data = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
            self.historico.trasacoes = f" Transferencia\n       Enviou\n       Valor: {valor:.2f}\n       Data: {data}"
            destino.historico.trasacoes = f" Transferencia\n       Recebeu: {self.numero}\n       Valor: {valor:.2f}\n       Data: {data}"
            return True, "Transferencia realizada com sucesso."
        else:
            return False, "Não foi possivel finalizar a transferencia."

    def extrato(self):
        data = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
        self.historico.trasacoes = f"tirou extrato - Saldo: {self.saldo} na data e hora {data}"
        return f"Data e hora: {data}\nNumero: {self.numero} \nSaldo: {self.saldo}\n"
    
    def historicoC(self):
        return self.historico.imprimir()

    def dadosConta(self):
        return f"{self.titular.dadosDoCliente()}Numero: {self.numero}\nSaldo: {self.saldo}\nUsuario: {self.usuario}"

    @staticmethod
    def get_totalContas():
        return Conta._totalContas

    @staticmethod
    def set_totalContas():
        Conta._totalContas += 1

def menu():
    print("\n1 - Criar conta."
    "\n2 - Fazer saque."
    "\n3 - Fazer deposito."
    "\n4 - Fazer transferência."
    "\n5 - Extrato."
    "\n6 - Historico."
    "\n7 - Total de Contas")

if __name__ == '__main__':

    clientes = {}
    while True:
        menu()
        op = int(input("\nDigite seu opção: "))
        if op == 1:
            print()
            nome = input("Digite seu nome: ")
            sobrenome = input("Digite seu sobrenome: ")
            cpf = input("Digite seu CPF: ")
            cli = Cliente(nome, sobrenome, cpf)
            numero = int(input("Digite o numero da conta: "))
            saldo = float(input("Digite o saldo: "))
            limite = float(input("Digite o limite: "))
            clientes[numero] = Conta(numero, cli, saldo, limite)
        elif op == 2:
            print()
            for chave in clientes.keys():
                print(f"Numeros das contas: {chave}" )
            numero = int(input("Digite o numero da conta para sacar: "))
            valor = float(input("Digite o valor: "))
            clientes[numero].sacar(valor)
        elif op == 3:
            print()
            numero = int(input("Digite o numero da conta para depositar: "))
            valor = float(input("Digite o valor: "))
            clientes[numero].depositar(valor)
        elif op == 4:
            print()
            numero = int(input("Digite o numero da conta que vai transferir: "))
            numeroDestino = int(input("Digite o numero da conta que vai receber: "))
            valor = float(input("Digite o valor de trasnferência: "))
            clientes[numero].transfere(clientes[numeroDestino], valor)
        elif op == 5:
            print()
            numero = int(input("Digite o numero da conta que deseja ver o extrato: "))
            clientes[numero].extrato()
        elif op == 6:
            numero = int(input("Digite o numero da conta que deseja ver o extrato: "))
            clientes[numero].imprimirHistorico()
        elif op == 7:
            print(f"Total de contas: {Conta.get_totalContas()}")



