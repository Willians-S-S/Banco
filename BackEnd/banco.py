from conta import *
import mysql.connector as mysql
from random import randint
import datetime
import threading
class Banco():

    # __slots__ = ['_conta','_usuario', '_senha', '_nome', '_cpf', '_saldo', '_limite']

    def __init__(self):
        self.conexao = mysql.connect(host='localhost', db='conta', user='root', password='Tales of demons', autocommit=True)
        self.cursor = self.conexao.cursor()
        self.sinc = threading.Lock()
        # self._conta = Conta()

    # @property
    # def conta(self):
    #     return self._conta
    
    # @conta.setter
    # def conta(self, conta):
    #     self._conta = conta

    def add_conta(self, usuario, senha, nome, cpf, saldo = 0.0, limite = 1000.0):
        if not self.verificarCPF(cpf):
            if not self.verificarUsuario(usuario):
                data = datetime.datetime.today().strftime("%d/%m/%y %H:%M")
                while True:
                    numero = randint(100, 999)
                    if not self.verificarNumero(numero):
                        self.numero = numero
                        break

                query = f'INSERT INTO cliente(cpf, nome, usuario, senha, numero, saldo, limite, historico) VALUES ("{cpf}", "{nome}", "{usuario}", "{senha}", {numero}, {saldo}, {limite}, "Data de de abertura: {data}\n\n")'
                #self.sinc.acquire()
                self.cursor.execute(query)
                #self.sinc.release()
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

    def verificarUsuario(self, usuario, senha = None, UserPassword = True):
        if UserPassword:
            self.cursor.execute(f'SELECT usuario FROM cliente WHERE usuario = "{usuario}"')
            exists = self.cursor.fetchall()
            if exists:
                return True    
            return False
        else:
            self.cursor.execute(f'SELECT usuario, senha FROM cliente WHERE usuario = "{usuario}" and senha = "{senha}"')
            exists = self.cursor.fetchall()
            if exists:
                return True, 'Exite.'
            return False, 'Usuário ou senha não encontrado.'
    
    def verificaSenha(self, senha, numero):
        self.cursor.execute(f'select senha, numero from cliente where senha = "{senha}" and numero = {numero}')
        flag = self.cursor.fetchall()
        if flag:
            return True
        return False
    
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
    
    def get_saldo(self, numero):
        self.cursor.execute(f'select saldo, limite from cliente where numero = {numero}')
        flag = self.cursor.fetchall()
        if flag:
            return flag
        else:
            return False
    
    def set_saldo(self, numero, valor, flag = True):
            saldo = self.get_saldo(numero)
            if flag: 
                valor += saldo[0][0]
            else:
                valor = saldo[0][0] - valor
            self.cursor.execute(f'update cliente set saldo = {valor} where numero = {numero}')
    
    def get_historico(self, numero):
        self.cursor.execute(f'select historico from cliente where numero = {numero}')
        flag = self.cursor.fetchone()
        return flag

    def set_historico(self, numero, his):
        flag = self.get_historico(numero)
        flag = flag[0]
        if len(flag) >= 500:
            flag = flag[0:35:]
        his = flag + '\n' + his
        self.cursor.execute(f'update cliente set historico = "{his}" where numero = {numero}')

    def depositar(self,  numero, valor, NoHis=True):
        valor = float(valor)
        flag = self.get_saldo(numero)
        print(NoHis)
        if flag[0][1] < valor or valor <= 0 or flag[0][0] + valor > flag[0][1]:
            return False, "Não foi possível fazer o deposito."
        else:
            #self.sinc.acquire()
            self.set_saldo(numero, valor)
            data = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
            if NoHis:
                his = f" Deposito:\n      Valor: {valor:.2f}\n       Data: {data}\n\n"
                self.set_historico(numero, his)
            #self.sinc.release()
            return True, "Deposito realizado com sucesso."

    def sacar(self, numero, valor, senha, NoHis=True):
        valor = float(valor)
        flag = self.get_saldo(numero)
        if valor > flag[0][0] or valor <= 0:
            return False, "Valor maior que o saldo ou valor menor que 0."
        else:
            if self.verificaSenha(senha, numero):
                #self.sinc.acquire()
                self.set_saldo(numero, valor, False)
                if NoHis:
                    data = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
                    his = f" Saque:\n      Valor: {valor:.2f}\n       Data: {data}\n\n"
                    self.set_historico(numero, his)
                #self.sinc.release()
                return True, "Saque realizado com sucesso."
            return False, "Senha invalida."

    def transferir(self, numero, senha, destino, valor):
        valor = float(valor)
        retirou = self.sacar(numero, valor, senha, False)
        if retirou[0]:
            self.depositar(destino, valor, False)
            data = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
            his = f" Transferencia:\n       Enviou para: {destino}\n       Valor: {valor:.2f}\n       Data: {data}\n\n"
            #self.sinc.acquire()
            self.set_historico(numero, his)
            his = f" Transferencia:\n       Recebeu de: {numero}\n       Valor: {valor:.2f}\n       Data: {data}\n\n"
            self.set_historico(destino, his)
            #self.sinc.release()
            return True, "Transferencia realizada com sucesso."
        else:
            return False, "Não foi possivel finalizar a transferencia."


    def excluirConta(self, numero, senha=None):
        #self.sinc.acquire()
        print(f'Numero {numero}')
        self.cursor.execute(f'DELETE FROM cliente WHERE numero = {numero}')
        #self.sinc.release()

    
    # def excluirConta(self, numero, senha):
    #     try:
    #         flag, index = self.verificarNumeroB(numero)
    #         if flag:
    #             if self.conta[index].verificaSenha(senha):
    #                 self.conta.pop(index)
    #                 print("Conta excluida com sucesso")
    #                 return True
    #             else:
    #                 print("Senha inválida")
    #                 return False
    #         else:
    #             print("Numero invalido")
    #             return False
    #     except ValueError:
    #         print("Valor inválido")
    #         return False
    
    # def listarContasB(self):
    #     for i in self.conta:
    #         print(i.dadosConta())
    #         print()
    
    # def buscarConta(self, numero):
    #     flag, index = self.verificarNumeroB(numero)
    #     if flag:
    #         print(self.conta[index].dadosConta())
    #     else:
    #         print("Dados não encontrado")
    #     pass

    # @staticmethod
    # def totalContasB():
    #     print(f"Total de contas: {Conta.get_totalContas()}")
    #     return True

