from random import randint
import datetime
import threading
from database.sql import *

class Banco():

    __slots__ = ['bd', 'sinc', 'numero']

    def __init__(self):
        self.bd = Database()
        self.sinc = threading.Lock()

    def add_conta(self, usuario, senha, nome, cpf):
        if not self.bd.verificarCPF(cpf):
            if not self.bd.verificarUsuario(usuario):
                while True:
                    numero = randint(100, 999)
                    if not self.bd.verificarNumero(numero):
                        self.numero = numero
                        break
                self.sinc.acquire()
                self.bd.cadastrar(usuario, numero, senha, nome, cpf)
                self.sinc.release()

                return True, "Cadastro realizado com sucesso."
            else:
                return False, 'Usuário já estar cadastrado.'
        else:
            return False, 'CPF já estar cadastrado.'
    
    def login(self, usuario, senha):
        flag = self.bd.verificarUsuario(usuario, senha, False)
        if flag[0]:
            b = self.bd.enterAccount(usuario)
            return b
        else:
            return flag

    def verificarSaldo(self, numero):
        return self.bd.get_saldo(numero)

    def depositar(self,  numero, valor, NoHis=True):
        valor = float(valor)
        flag = self.bd.get_saldo(numero).split(',')
        print(f"Limite {float(flag[1])} saldo {float(flag[0])}")
        print('Valor ',valor)

        if float(flag[1]) < valor or valor <= 0 or float(flag[0]) + valor > float(flag[1]):
            return False, "Não foi possível fazer o deposito."
        else:
            self.sinc.acquire()
            self.bd.set_saldo(numero, valor)
            data = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
            if NoHis:
                his = f" Deposito:\n      Valor: {valor:.2f}\n       Data: {data}\n\n"
                self.bd.set_historico(numero, his)
            self.sinc.release()
            return True, "Deposito realizado com sucesso."

    def sacar(self, numero, valor, senha, NoHis=True):
        valor = float(valor)
        flag = self.bd.get_saldo(numero).split(',')
        if valor > float(flag[0]) or valor <= 0:
            return False, "Valor maior que o saldo ou valor menor que 0."
        else:
            if self.bd.verificaSenha(senha, numero):
                self.sinc.acquire()
                self.bd.set_saldo(numero, valor, False)
                if NoHis:
                    data = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
                    his = f" Saque:\n      Valor: {valor:.2f}\n       Data: {data}\n\n"
                    self.bd.set_historico(numero, his)
                self.sinc.release()
                return True, "Saque realizado com sucesso."
            return False, "Senha invalida."

    def transferir(self, numero, senha, destino, valor):
        valor = float(valor)
        retirou = self.sacar(numero, valor, senha, False)
        if retirou[0]:
            self.depositar(destino, valor, False)
            data = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
            his = f" Transferencia:\n       Enviou para: {destino}\n       Valor: {valor:.2f}\n       Data: {data}\n\n"
            self.sinc.acquire()
            self.bd.set_historico(numero, his)
            his = f" Transferencia:\n       Recebeu de: {numero}\n       Valor: {valor:.2f}\n       Data: {data}\n\n"
            self.bd.set_historico(destino, his)
            self.sinc.release()
            return True, "Transferencia realizada com sucesso."
        else:
            return False, "Não foi possivel finalizar a transferencia."
    
    def historico(self, numero):
        return self.bd.get_historico(numero)


    def excluirConta(self, numero, senha=None):
        self.sinc.acquire()
        print(f'Numero {numero}')
        self.cursor.execute(f'DELETE FROM cliente WHERE numero = {numero}')
        self.sinc.release()

if __name__ == "__main__":
    c = Banco()

    c.add_conta(5, 5, 'ablas', 55555555555)

    print(c.bd.get_saldo(686))

