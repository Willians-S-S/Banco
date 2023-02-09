from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys
from server_cliente import *
from hashlib import md5

from Tela_Inicial import *
from Tela_Cadastro import *
from Tela_Login import *
from Tela_Principal import *
from Tela_Deposito import *
from Tela_Saque import *
from Tela_Transferir import *
from Tela_Historico import *


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()

        self.Tela_Inicial = TelaInicial()
        self.Tela_Inicial.setupUi(self.stack0)

        self.Tela_Cadastro = TelaCadastro()
        self.Tela_Cadastro.setupUi(self.stack1)

        self.Tela_Login = TelaLogin()
        self.Tela_Login.setupUi(self.stack2)

        self.Tela_Principal = TelaPrincipal()
        self.Tela_Principal.setupUi(self.stack3)

        self.Tela_Deposito = TelaDeposito()
        self.Tela_Deposito.setupUi(self.stack4)

        self.Tela_Saque = TelaSaque()
        self.Tela_Saque.setupUi(self.stack5)

        self.Tela_Transferir = TelaTransferir()
        self.Tela_Transferir.setupUi(self.stack6)

        self.Tela_Historico = TelaHistorico()
        self.Tela_Historico.setupUi(self.stack7)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)


class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)

        
        try:
            self.server = server_cliente('10.180.42.32', 8005)
        except ConnectionRefusedError:
            QtWidgets.QMessageBox.information(None, 'ERROR', f'Não foi possível conectar ao servidor.'
                                                             f'\nVerifique a conexão e tente novamente')
            sys.exit()
        
        self.index = None

        self.Tela_Inicial.ButtonCadastrar.clicked.connect(self.BotaoParaTelaCadastro)
        self.Tela_Inicial.ButtonLogin.clicked.connect(self.BotaoParaTelaLogin)
        self.Tela_Inicial.ButtonSair.clicked.connect(self.sair)

        self.Tela_Cadastro.ButtonCadastrar.clicked.connect(self.BotaoCadastrar)
        self.Tela_Cadastro.ButtonVoltar.clicked.connect(self.BotaoVoltarTelaInicial)

        self.Tela_Login.ButtonLogin.clicked.connect(self.BotaoLogin)
        self.Tela_Login.ButtonVoltar.clicked.connect(self.BotaoVoltarTelaInicial)

        self.Tela_Principal.ButtonAtualizar.clicked.connect(self.BotaoAtualizar)
        self.Tela_Principal.ButtonDepositar.clicked.connect(self.BotaoParaTelaDeposito)
        self.Tela_Principal.ButtonSacar.clicked.connect(self.BotaoParaTelaSacar)
        self.Tela_Principal.ButtonTransferir.clicked.connect(self.BotaoParaTelaTransferir)
        self.Tela_Principal.ButtonSair.clicked.connect(self.BotaoVoltarTelaInicial)
        self.Tela_Principal.ButtonHistorico.clicked.connect(self.BotaoParaTelaHistorico)
        self.Tela_Principal.ButtonExcluir.clicked.connect(self.BotaoExcluir)

        self.Tela_Deposito.ButtonDepositar.clicked.connect(self.BotaoDepoistar)
        self.Tela_Deposito.ButtonVoltar.clicked.connect(self.BotaoParaTelaPrincipal)

        self.Tela_Saque.ButtonSacar.clicked.connect(self.BotaoSacar)
        self.Tela_Saque.ButtonVoltar.clicked.connect(self.BotaoParaTelaPrincipal)

        self.Tela_Transferir.ButtonTransferir.clicked.connect(self.BotaoTransferir)
        self.Tela_Transferir.ButtonVoltar.clicked.connect(self.BotaoParaTelaPrincipal)

        self.Tela_Historico.ButtonVoltar.clicked.connect(self.BotaoParaTelaPrincipal)

    def sair(self):
        # self.server.send('sair'.encode())
        self.request_server('sair')
        sys.exit()

    def BotaoVoltarTelaInicial(self):
        self.QtStack.setCurrentIndex(0)
        self.Tela_Cadastro.labelNotificacao.setText('')
        self.Tela_Login.labelNotificacao.setText('')

    def BotaoParaTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def BotaoParaTelaLogin(self):
        self.QtStack.setCurrentIndex(2)

    def BotaoParaTelaPrincipal(self):
        self.QtStack.setCurrentIndex(3)
        self.Tela_Deposito.labelNotificacao.setText('')
        self.Tela_Saque.labelNotificacao.setText('')

    def BotaoParaTelaDeposito(self):
        self.Tela_Deposito.labelNotificacao.setText('')
        self.QtStack.setCurrentIndex(4)

    def BotaoParaTelaSacar(self):
        self.Tela_Saque.labelNotificacao.setText('')
        self.QtStack.setCurrentIndex(5)

    def BotaoParaTelaTransferir(self):
        self.Tela_Transferir.labelNotificacao.setText('')
        self.QtStack.setCurrentIndex(6)
    
    def request_server(self, request):
        self.server.send(request.encode())
        recv = self.server.recv(2048)
        flag = recv.decode()
        # print(flag, type(flag))
        flag = flag.replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace(",", "").replace("'", '').split()
        return flag
    
    def concatenar(self, string):
        noti = ''
        for i in range(1,len(string)):
            noti += string[i] + " "
        return noti

    def BotaoCadastrar(self):
        nome = self.Tela_Cadastro.lineNome.text()
        cpf = self.Tela_Cadastro.lineCpf.text()
        usuario = self.Tela_Cadastro.lineUsuario.text()
        senha = self.Tela_Cadastro.lineSenha.text()
        if nome != '' and cpf != '' and usuario != '' and senha != '':
            if cpf.isdigit() and len(cpf) == 11:
                senha = senha.encode('utf-8')
                senha = md5(senha).hexdigest()
                solicit = f'add_conta*{usuario}*{senha}*{nome}*{cpf}'
                flag = self.request_server(solicit)
                noti = self.concatenar(flag)
                self.Tela_Cadastro.lineNome.setText("")
                self.Tela_Cadastro.lineCpf.setText("")
                self.Tela_Cadastro.lineUsuario.setText("")
                self.Tela_Cadastro.lineSenha.setText("")
                self.Tela_Cadastro.labelNotificacao.setText(noti)
            else:
                self.Tela_Cadastro.labelNotificacao.setText("O CPF não atendo os parametros.")
        else:
            self.Tela_Cadastro.labelNotificacao.setText("Todos os espaços devem ser preenchidos.")
        self.Tela_Cadastro.lineNome.setText("")
        self.Tela_Cadastro.lineCpf.setText("")
        self.Tela_Cadastro.lineUsuario.setText("")
        self.Tela_Cadastro.lineSenha.setText("")

    def BotaoLogin(self):
        usuario = self.Tela_Login.lineUsuario.text()
        senha = self.Tela_Login.lineSenha.text()
        if usuario != '' and senha != '':
            senha = senha.encode('utf-8')
            senha = md5(senha).hexdigest()
            print('Senha: ',senha)
            solicit = f'login*{usuario}*{senha}'
            # flag = self.request_server(solicit)
            self.server.send(solicit.encode())
            recv = self.server.recv(2048)
            flag4 = recv.decode()
            flag4 = flag4.replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace(",", "").replace("'", '').split()
            if flag4[0] == 'True':
                
                self.numero = int(flag4[3])
                # self.Tela_Principal.labelNome.setText(f"Olá, {flag4[1][1][0]}")
                # self.Tela_Principal.labelSaldo.setText(f"R$ {float(flag4[2]):.2f}")
                # self.Tela_Principal.labelNumero.setText(f"Conta {int(flag4[3])}")
                self.Tela_Principal.labelNome.setText(f"Olá, {flag4[1]}")
                self.Tela_Principal.labelSaldo.setText(f"R$ {float(flag4[2]):.2f}")
                self.Tela_Principal.labelNumero.setText(f"Conta {int(flag4[3])}")
                self.QtStack.setCurrentIndex(3)
            else:
                noti4 = self.concatenar(flag4)
                # caralho = str(flag4)
                self.Tela_Login.labelNotificacao.setText(noti4)
        else:
            self.Tela_Login.labelNotificacao.setText("Todos os espaços devem ser preenchidos.")
        self.Tela_Login.lineUsuario.setText("")
        self.Tela_Login.lineSenha.setText("")

    def BotaoAtualizar(self):
        solicit = f'get_saldo*{self.numero}'
        flag = self.request_server(solicit)
        self.Tela_Principal.labelSaldo.setText(f"R$ {float(flag[0]):.2f}")

    def BotaoDepoistar(self):
        valor = self.Tela_Deposito.lineSaldo.text()
        if valor != '':
            if valor.replace('.','').isdigit():
                solicit = f'depositar*{self.numero}*{float(valor)}'
                flag = self.request_server(solicit)
                noti = self.concatenar(flag)
                self.Tela_Deposito.labelNotificacao.setText(noti)
            else:
                self.Tela_Deposito.labelNotificacao.setText("Informe somente números.")
        else:
            self.Tela_Deposito.labelNotificacao.setText("Todos os espaços devem ser preenchidos.")
        self.Tela_Deposito.lineSaldo.setText('')

    def BotaoSacar(self):
        valor = self.Tela_Saque.lineSaldo.text()
        senha = self.Tela_Saque.lineSenha.text()
        if valor != '' and senha != '':
            if valor.replace('.','').isdigit():
                senha = senha.encode('utf-8')
                senha = md5(senha).hexdigest()
                solicit = f'sacar*{self.numero}*{valor}*{senha}'
                flag = self.request_server(solicit)
                if flag[0]:
                    noti = self.concatenar(flag)
                    self.Tela_Saque.labelNotificacao.setText(noti)
                else:
                    self.Tela_Saque.labelNotificacao.setText('Senha invalida.')
            else:
                self.Tela_Saque.labelNotificacao.setText('Informe somente números no espaço do valor.')
        else:
            self.Tela_Saque.labelNotificacao.setText("Todos os espaços devem estar preenchidos.")
        self.Tela_Saque.lineSaldo.setText('')
        self.Tela_Saque.lineSenha.setText('')

    def BotaoTransferir(self):
        valor = self.Tela_Transferir.lineSaldo.text()
        senha = self.Tela_Transferir.lineSenha.text()
        numero = self.Tela_Transferir.lineNumero.text()
        if valor != '' and senha != '' and numero != '':
            if valor.replace('.','').isdigit() and numero.replace('.','').isdigit():
                senha = senha.encode('utf-8')
                senha = md5(senha).hexdigest()
                solicit = f'transferir*{self.numero}*{senha}*{numero}*{valor}'
                flag = self.request_server(solicit)
                print(flag)
                noti = self.concatenar(flag)
                self.Tela_Transferir.labelNotificacao.setText(noti)
            else:
                self.Tela_Transferir.labelNotificacao.setText("Informe somente números")
        else:
            self.Tela_Transferir.labelNotificacao.setText("Todos os espaços devem ser preenchidos.")
        self.Tela_Transferir.lineSaldo.setText('')
        self.Tela_Transferir.lineSenha.setText('')
        self.Tela_Transferir.lineNumero.setText('')
    
    def concatenarHis(self, string):
        noti = ''
        for i in range(len(string)):
            noti += string[i] + ' '
        noti = noti.split('\\n')
        a = ''
        for i in noti:
            a += i + '\n'
        return a

    def BotaoParaTelaHistorico(self):
        solicit = f'get_historico*{self.numero}'
        flag = self.request_server(solicit)
        noti = self.concatenarHis(flag)
        self.Tela_Historico.textHistorico.setText(noti)
        self.QtStack.setCurrentIndex(7)

    def BotaoExcluir(self):
        solicit = f'excluirConta*{self.numero}'
        self.request_server(solicit)
        self.QtStack.setCurrentIndex(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())