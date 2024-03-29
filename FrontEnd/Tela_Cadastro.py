from PyQt5 import QtCore, QtGui, QtWidgets


class TelaCadastro(object):
    '''
    "TelaCadastro", que é usada para criar uma tela de cadastro com alguns campos de entrada, como nome, CPF, usuário e senha. 
    A interface gráfica da tela é criada com a biblioteca PyQt5 e utiliza várias propriedades de estilo para personalizar a aparência dos widgets, 
    incluindo cores, fontes e bordas.
    '''
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(287, 591)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-1, 0, 291, 591))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 290, 591))
        self.label.setStyleSheet("background-color:rgba(16, 30,    41, 240);\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineNome = QtWidgets.QLineEdit(self.widget)
        self.lineNome.setGeometry(QtCore.QRect(20, 210, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineNome.setFont(font)
        self.lineNome.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px")
        self.lineNome.setObjectName("lineNome")
        self.lineCpf = QtWidgets.QLineEdit(self.widget)
        self.lineCpf.setGeometry(QtCore.QRect(20, 260, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineCpf.setFont(font)
        self.lineCpf.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px")
        self.lineCpf.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineCpf.setObjectName("lineCpf")
        self.ButtonCadastrar = QtWidgets.QPushButton(self.widget)
        self.ButtonCadastrar.setGeometry(QtCore.QRect(20, 490, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.ButtonCadastrar.setFont(font)
        self.ButtonCadastrar.setStyleSheet("QPushButton#ButtonCadastrar{\n"
"background-color: rgba(2, 65, 118, 255);\n"
"color: rgba(250, 250, 250, 200);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#ButtonCadastrar:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(2, 65, 118, 100);\n"
"background-position: calc(100% - 10px)center;\n"
"}\n"
"QPushButton#ButtonCadastrar:hover{\n"
"background-color: rgba(2, 65, 118, 200);\n"
"}")
        self.ButtonCadastrar.setObjectName("ButtonCadastrar")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 180, 150))
        font = QtGui.QFont()
        font.setFamily("dripicons-v2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgba(0, 125, 236, 255);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("IMG/user.svg"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineUsuario = QtWidgets.QLineEdit(self.widget)
        self.lineUsuario.setGeometry(QtCore.QRect(20, 310, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineUsuario.setFont(font)
        self.lineUsuario.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px")
        self.lineUsuario.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineUsuario.setObjectName("lineUsuario")
        self.lineSenha = QtWidgets.QLineEdit(self.widget)
        self.lineSenha.setGeometry(QtCore.QRect(20, 360, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineSenha.setFont(font)
        self.lineSenha.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px")
        self.lineSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineSenha.setObjectName("lineSenha")
        self.ButtonVoltar = QtWidgets.QPushButton(self.widget)
        self.ButtonVoltar.setGeometry(QtCore.QRect(20, 540, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.ButtonVoltar.setFont(font)
        self.ButtonVoltar.setStyleSheet("QPushButton#ButtonVoltar{\n"
"background-color: rgba(2, 65, 118, 255);\n"
"color: rgba(250, 250, 250, 200);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#ButtonVoltar:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(2, 65, 118, 100);\n"
"background-position: calc(100% - 10px)center;\n"
"}\n"
"QPushButton#ButtonVoltar:hover{\n"
"background-color: rgba(2, 65, 118, 200);\n"
"}")
        self.ButtonVoltar.setObjectName("ButtonVoltar")
        self.labelNotificacao = QtWidgets.QLabel(self.widget)
        self.labelNotificacao.setGeometry(QtCore.QRect(20, 410, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelNotificacao.setFont(font)
        self.labelNotificacao.setText("")
        self.labelNotificacao.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNotificacao.setObjectName("labelNotificacao")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineNome.setPlaceholderText(_translate("Form", " Nome Completo"))
        self.lineCpf.setPlaceholderText(_translate("Form", " CPF"))
        self.ButtonCadastrar.setText(_translate("Form", "Cadastrar"))
        self.lineUsuario.setPlaceholderText(_translate("Form", "  Usuário"))
        self.lineSenha.setPlaceholderText(_translate("Form", "  Senha"))
        self.ButtonVoltar.setText(_translate("Form", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = TelaCadastro()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
