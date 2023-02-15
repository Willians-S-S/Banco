from random import randint
import datetime
import threading
from database.sql import *

class Banco():

    """
        A classe Banco instancia um objeto Banco capaz de acessar um banco de dados para registro 
        e recuperação de dados de contas bancárias, além de realização de transações financeiras, 
        como saques, depósitos e transferências.

        Attributes
        ----------
        __slots__ : list
            Define todos os atributos que podem ser criados na classe.
        bd: objeto de Database()
            Armazena uma instância da classe Database que possui as operaçõesque podem ser executadas no banco de dados.
        sinc: objeto de threading.Lock()
            controla o acesso simultâneo de threads.

        Methods
        -------
        add_conta(self, usuario, senha, nome, cpf)
            Verifica se já existe uma conta com CPF e usuario, caso não, cria a conta.

        login(self, usuario, senha)
            Verifica se os dados inseridos pelo usuário correspondem para uma conta e retorna o nome, saldo, numero 
            do usuário se a conta existir.

        verificarSaldo(self, numero)
            Verifica o saldo de uma conta e o retorna.

        depositar(self,  numero, valor, NoHis=True)
            Deposita o valor em sua conta bancária.

        sacar(self, numero, valor, senha, NoHis=True)
            Retirar um valor de uma conta bancária.

        transferir(self, numero, senha, destino, valor)
            Faz a transferência do valor da conta remetente para a conta destino.

        historico(self, numero)
            Retorna uma string com o histórico de todas as transações realizado na conta.

        excluirConta(self, numero, senha=None)
            Faz a exclusão de uma conta.
    """

    __slots__ = ['bd', 'sinc', 'numero']

    def __init__(self, senha):
        self.bd = Database(senha)
        self.sinc = threading.Lock()

    def add_conta(self, usuario, senha, nome, cpf):
        """
            verifique se já existe uma conta com esse CPF e usuario caso não, crie a conta.

            parameters
            ----------
            usuario: str
                Usuario da conta
            senha: str
                Senha de acesso à conta.
            nome: str
                Nome do titular da conta.
            CPF: Str
                CPF do titular da conta.
            
            returns
            -------
                Sucesso: Retorna True e uma string com informação que a conta foi criada.
                Falha: Retorna Falso e uma string com informação que a conta não foi criada.
        """
        try:
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
        except:
            print()
    
    def login(self, usuario, senha):

        """
            Verifica se os dados inseridos pelo usuário correspondem para uma 
            conta e retorna nome, saldo, numero do usuário se a conta existir.

            parameters
            ----------
            usuario: str
                Usuario da conta.
            senha: str
                Senha de acesso à conta.

            returns
            -------
                Sucesso: Retorna o nome, saldo, numero da conta bancária.
                Falha: Retorna Falso.
        """

        flag = self.bd.verificarUsuario(usuario, senha, False)
        if flag[0]:
            b = self.bd.enterAccount(usuario)
            return b
        else:
            return flag

    def verificarSaldo(self, numero):
        return self.bd.get_saldo(numero)

    def depositar(self,  numero, valor, NoHis=True):
        """
            Deposita o valor na conta bancária.

            parameters
            ----------
            numero: int
                Numero da conta bancária
            valor: str
                Valor a ser depositado.
            NoHis: Boolean
                Valor booleano para identificar se a transação se refere a um depósito
                ou uma transferência, pois a função de depósito é usada também no 
                processo de transferência.
            Returns
            -------
                Successo: Retorna True e uma string com informação sobre o sucesso do deposito.
                Falha: Retorna Falso e uma string com informação sobre a falha do deposito.
        """
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
        """
            Sacar de uma conta bancária.

            parameters
            ----------
            numero: str
                Numero da conta bancária
            valor: str
                Valor a ser depositado.
            senha: str
                Senha de acesso à conta.
            NoHis: Boolean
                Valor booleano para identificar se a transação se refere a um saque
                ou uma transferência, pois a função de saque é usada também no 
                processo de transferência.
            Returns
            -------
                Successo: Retorna True e uma string com informação sobre o sucesso do saque.
                Falha: Retorna Falso e uma string com informação sobre a falha do saque.
        """
        
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
        """
            Faz a transferência do valor da conta remetente para uma conta destino.

            parameters
            ----------
            numero: str
                Numero da conta bancária remetente.
            senha: str
                Senha de acesso à conta.
            destino: str
                Numero da conta bancária alvo.
            Valor: str
                valor da transferência
            Returns
            -------
                Successo: Retorna True e uma string com informação sobre o sucesso da transferência.
                Falha: Retorna Falso e uma string com informação sobre a falha da transferência.
        """
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
        """
            Retorna uma string com o histórico de todas as transações realizado na conta.

            parameters
            ----------
            numero: str
                Numero da conta bancária.
            returns
            -------
                retorna o histórico da conta.
        """
        return self.bd.get_historico(numero)


    def excluirConta(self, numero, senha=None):
        """
            Faz a exclusão da conta bancária.

            parameters
            ----------
            numero: str
                Numero da conta bancária remetente.
            senha: str
                Senha de acesso à conta.
            
            returns
            -------
                retorna None.

        """
        self.sinc.acquire()
        print(f'Numero {numero}')
        self.cursor.execute(f'DELETE FROM cliente WHERE numero = {numero}')
        self.sinc.release()

