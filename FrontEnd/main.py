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
        '''
        Esta classe define a interface gráfica do usuário usando PyQt5. 
        Ele define uma janela principal (Main) e um layout de pilha de várias outras janelas (stack0 a stack7) 
        que podem ser alternadas dentro da janelaprincipal. 
        Cada tela é definida em seu próprio arquivo de classe, como TelaCadastro, TelaLogin etc. 
        O método setupUi() é chamado para cada tela para configurar sua aparência e funcionamento, 
        e cada uma delas é adicionada ao layout de pilha por meio do método addWidget().

        Parameters
        ----------
        Main: Object

        Returns
        -------
        None
        '''
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

        '''
        Esse trecho de código tenta se conectar a um servidor na máquina com o endereço IP '10.0.0.102' e a porta 8005. Se a conexão for recusada, 
        uma caixa de mensagem será exibida informando que não foi possível se conectar ao servidor e a aplicação será encerrada usando sys.exit().
        '''
        try:
            self.server = server_cliente('10.0.0.102', 8005)
        except ConnectionRefusedError:
            QtWidgets.QMessageBox.information(None, 'ERROR', f'Não foi possível conectar ao servidor.'
                                                            f'\nVerifique a conexão e tente novamente')
            sys.exit()
        
        '''
        Este trecho de código define as conexões de sinal e slot para vários botões da interface do usuário. 
        Cada vez que um botão é clicado, ele chama a função correspondente que executa uma determinada ação. 
        Por exemplo, ao clicar no botão 'ButtonLogin' em 'Tela_Login', o método 'BotaoLogin' é chamado.
        '''
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
        '''
        Botão para sair do sistema.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.request_server('sair')
        sys.exit()

    def BotaoVoltarTelaInicial(self):
        '''
        Botão que volta para a tela inicial do sistema.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.QtStack.setCurrentIndex(0)
        self.Tela_Cadastro.labelNotificacao.setText('')
        self.Tela_Login.labelNotificacao.setText('')

    def BotaoParaTelaCadastro(self):
        '''
        Botão para abrir a tela de cadastro.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.QtStack.setCurrentIndex(1)

    def BotaoParaTelaLogin(self):
        '''
        Botão para abrir a tela de login.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.QtStack.setCurrentIndex(2)

    def BotaoParaTelaPrincipal(self):
        '''
        Botão para a tela do menu do usuario. 
        ele limpa o campo de notificação da tela de principal, em seguida altera a tela atual do sistema para a tela principal.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.QtStack.setCurrentIndex(3)
        self.Tela_Deposito.labelNotificacao.setText('')
        self.Tela_Saque.labelNotificacao.setText('')

    def BotaoParaTelaDeposito(self):
        '''
        Botão para a tela de deposito, 
        ele limpa o campo de notificação da tela de deposito, em seguida altera a tela atual do sistema para a tela de deposito.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.Tela_Deposito.labelNotificacao.setText('')
        self.QtStack.setCurrentIndex(4)

    def BotaoParaTelaSacar(self):
        '''
        Botão para a tela sacar, 
        ele limpa o campo de notificação da tela de saque, em seguida altera a tela atual do sistema para a tela de deposito.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.Tela_Saque.labelNotificacao.setText('')
        self.QtStack.setCurrentIndex(5)

    def BotaoParaTelaTransferir(self):
        '''
        Botão para a tela transferir, 
        ele limpa o campo de notificação da tela transferir, em seguida altera a tela atual do sistema para a tela de transferir.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.Tela_Transferir.labelNotificacao.setText('')
        self.QtStack.setCurrentIndex(6)
    
    def request_server(self, request):
        '''
        Essa função envia uma requisição de mensagem para o servidor com a request como parâmetro. 
        Em seguida, aguarda uma resposta de até 2048 bytes do servidor e a converte em uma string. 
        Então, remove todos os caracteres desnecessários da resposta e retorna como uma lista de palavras.

        Parameters
        ----------
        request :Str

        Returns
        -------
        flag
        '''
        self.server.send(request.encode())
        recv = self.server.recv(2048)
        flag = recv.decode()
        flag = flag.replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace(",", "").replace("'", '').split()
        return flag
    

    def concatenar(self, string):
        '''
        Este é um método chamado concatenar que recebe uma string como entrada e concatena todos os caracteres da string, 
        exceto o primeiro caractere (índice 0), com um caractere de espaço entre cada caractere.
        A string concatenada resultante é então retornada.

        Parameters
        ----------
        string: Str

        Returns
        -------
        noti
        '''
        noti = ''
        for i in range(1,len(string)):
            noti += string[i] + " "
        return noti

    def BotaoCadastrar(self):
        '''
        Este é um método chamado BotaoCadastrar que é acionado quando o botão "Cadastrar" é clicado na tela de cadastro. 
        Ele recupera os valores dos campos de entrada para nome, cpf, 
        usuário e senha da tela de cadastro e verifica se todos os campos estão preenchidos. 
        Se algum campo estiver vazio, uma notificação será exibida na tela.

        Se todos os campos estiverem preenchidos, o código verifica se o CPF tem 11 dígitos e se é composto apenas por números. 
        Em seguida, a senha é codificada em utf-8 e criptografada usando o algoritmo MD5. 
        Uma solicitação é enviada ao servidor contendo as informações do novo usuário a ser adicionado. 
        A resposta do servidor é concatenada em uma string e exibida na tela de cadastro.

        Independentemente de ter sucesso ou falhar, todos os campos da tela de cadastro são limpos para que um novo usuário possa ser adicionado. 
        Se o CPF não atender aos parâmetros necessários, uma notificação informando isso é exibida na tela

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
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
        '''
        Este é um método chamado BotaoLogin que é acionado quando o botão "Login" é clicado na tela de login. 
        Ele recupera os valores dos campos de entrada para usuário e senha da tela de login e verifica se ambos estão preenchidos. 
        Se algum campo estiver vazio, uma notificação será exibida na tela.

        Se ambos os campos estiverem preenchidos, o código codifica a senha em utf-8 e a criptografa usando o algoritmo MD5. 
        Em seguida, é criada uma solicitação contendo as informações de login do usuário e enviada para o servidor. 
        A resposta do servidor é recebida e processada. 
        Se o primeiro elemento da resposta for 'True', o login é bem-sucedido e o usuário é direcionado para a tela principal do sistema.

        Caso contrário, uma notificação informando que o login falhou é exibida na tela de login. 
        Independentemente de ter sucesso ou falhar, os campos da tela de login são limpos para que um novo login possa ser feito.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
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
        '''
        Este é um método chamado BotaoAtualizar que é acionado quando o botão "Atualizar" é clicado na tela principal do sistema. 
        Ele cria uma solicitação contendo o número da conta do usuário e o tipo de solicitação, que é "verificarSaldo", e envia essa solicitação para o servidor.

        Em seguida, ele recebe uma resposta do servidor contendo o saldo atualizado da conta. 
        O saldo é formatado como um número de ponto flutuante com duas casas decimais e exibido na tela principal do sistema, 
        na label denominada "labelSaldo".

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        solicit = f'verificarSaldo*{self.numero}'
        flag = self.request_server(solicit)
        self.Tela_Principal.labelSaldo.setText(f"R$ {float(flag[0]):.2f}")

    def BotaoDepoistar(self):
        '''
        Este é um método chamado BotaoDepoistar que é acionado quando o botão "Depositar" é clicado na tela de depósito. 
        Ele verifica se o campo de valor não está vazio e se contém apenas dígitos. 
        Se for o caso, uma solicitação de depósito é enviada ao servidor com o número da conta e o valor do depósito. 
        O campo de notificação da tela de depósito é atualizado com a mensagem retornada pelo servidor e, em seguida, o campo de valor é limpo. 
        Se o campo de valor estiver vazio ou não contiver apenas dígitos, uma mensagem apropriada é exibida no campo de notificação.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
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
        '''
        O método BotaoSacar é chamado quando o usuário clica no botão "Sacar" na tela de operações. 
        Ele pega o valor e a senha inseridos pelo usuário, verifica se o valor é um número válido e codifica a senha usando o algoritmo MD5. 
        Em seguida, constrói uma mensagem com o número da conta, o valor e a senha codificada e envia uma solicitação ao servidor. 
        Se a operação for bem-sucedida, uma mensagem de notificação é exibida na tela de operações, caso contrário, 
        uma mensagem de senha inválida é exibida. Por fim, os campos de valor e senha são limpos.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
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
        '''
        Este é um método que é acionado quando o botão "Transferir" é pressionado na tela. 
        Ele pega o valor que foi inserido no campo de valor (lineSaldo), 
        a senha (lineSenha) e o número da conta de destino (lineNumero) da tela de transferência e verifica se todos eles foram preenchidos. 
        Se estiverem preenchidos, ele verifica se os campos de valor e número da conta contêm apenas números. 
        Se ambos forem numéricos, a senha é codificada em UTF-8 e convertida em um hash md5. Em seguida, 
        é criada uma solicitação de transferência com o número da conta de origem (self.numero), a senha hash, 
        o número da conta de destino e o valor a ser transferido. 
        Essa solicitação é enviada para o servidor por meio do método request_server() e a resposta é armazenada na variável flag. 
        Em seguida, a notificação de transferência é exibida na tela de transferência com a mensagem da resposta do servidor. 
        Caso contrário, a notificação informa que apenas números devem ser inseridos nos campos de valor e número da conta, 
        ou que todos os campos devem ser preenchidos. 
        Em todos os casos, os campos de valor, senha e número da conta são redefinidos.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
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
        '''
        Essa função recebe uma string e a transforma em um formato mais legível para o usuário exibir na tela como uma notificação de histórico. 
        Primeiramente, a função cria uma variável noti que vai armazenar a string processada. 
        Em seguida, ela percorre a string, adiciona um espaço entre cada elemento e armazena em noti. 
        Depois, ela quebra a string em uma lista com o separador '\n' e adiciona cada elemento em uma nova string a, 
        adicionando uma quebra de linha para cada elemento. 
        Por fim, a função retorna a string a.

        Parameters
        ----------
        string: str

        Returns
        -------
        a
        '''
        noti = ''
        for i in range(len(string)):
            noti += string[i] + ' '
        noti = noti.split('\\n')
        a = ''
        for i in noti:
            a += i + '\n'
        return a

    def BotaoParaTelaHistorico(self):
        '''
        A função BotaoParaTelaHistorico é responsável por obter o histórico de transações bancárias do cliente e exibi-las na tela de histórico.
        Para isso, é feita uma solicitação ao servidor bancário com o número da conta do cliente e o tipo de solicitação, que é "historico". 
        Em seguida, o resultado é passado para a função concatenarHis que formata as informações em uma string para ser exibida na tela.
        Por fim, a string formatada é atribuída ao widget de texto textHistorico da tela de histórico e a tela de histórico é exibida.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        solicit = f'historico*{self.numero}'
        flag = self.request_server(solicit)
        noti = self.concatenarHis(flag)
        self.Tela_Historico.textHistorico.setText(noti)
        self.QtStack.setCurrentIndex(7)

    def BotaoExcluir(self):
        '''
        Essa função BotaoExcluir é responsável por enviar uma solicitação ao servidor para excluir a conta do usuário logado. 
        Ela constrói a solicitação concatenando o número da conta do usuário com o comando "excluirConta" e então chama a função request_server para enviar a solicitação ao servidor. 
        Depois de enviar a solicitação, a função muda a página atual da GUI para a página inicial (index 0 na pilha de widgets QtStack).

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        solicit = f'excluirConta*{self.numero}'
        self.request_server(solicit)
        self.QtStack.setCurrentIndex(0)

if __name__ == "__main__":
    '''
    Esse trecho de código é o ponto de entrada do programa. 
    Ele verifica se o módulo atual é o módulo principal (ou seja, não foi importado como um módulo em outro arquivo) e, se for, 
    cria uma instância do aplicativo QApplication e a janela principal Main, e inicia o loop de eventos do aplicativo chamando app.exec_(). 
    Quando a janela principal é fechada, o loop de eventos termina e a execução do programa é encerrada
    '''
    app = QtWidgets.QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())