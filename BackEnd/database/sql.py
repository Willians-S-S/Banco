import mysql.connector as mysql
import datetime

class Database():
    
    def __init__(self):
        self.conexao = mysql.connect(host='localhost', db='conta', user='root', password='Tales of demons', autocommit=True)
        self.cursor = self.conexao.cursor()
    
    def cadastrar(self, usuario, numero, senha, nome, cpf, saldo = 0.0, limite = 1000.0):
        data = datetime.datetime.today().strftime("%d/%m/%y %H:%M")
        query = f'INSERT INTO cliente(cpf, nome, usuario, senha, numero, saldo, limite, historico) VALUES ("{cpf}", "{nome}", "{usuario}", "{senha}", {numero}, {saldo}, {limite}, "Data de de abertura: {data}\n\n")'
        self.cursor.execute(query)

    def get_saldo(self, numero):
        self.cursor.execute(f'select saldo, limite from cliente where numero = {numero}')
        flag = self.cursor.fetchall()
        valores = f'{flag[0][0]:.2f}, {flag[0][1]:.2f}'
        if flag:
            return valores
        else:
            return False
    
    def set_saldo(self, numero, valor, flag = True):
            saldo = self.get_saldo(numero).split(',')
            if flag: 
                valor += float(saldo[0])
            else:
                valor = float(saldo[0]) - valor
            self.cursor.execute(f'update cliente set saldo = {valor} where numero = {numero}')
    
    def enterAccount(self, usuario):
        self.cursor.execute(f'select nome, saldo, numero from cliente where usuario = "{usuario}"')
        resul = self.cursor.fetchall()
        resul = f'{resul[0][0]}, {resul[0][1]}, {resul[0][2]}' 
        print(resul)
        return True, resul
    
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