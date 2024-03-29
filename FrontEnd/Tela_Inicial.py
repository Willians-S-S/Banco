from PyQt5 import QtCore, QtGui, QtWidgets


class TelaInicial(object):
    '''
    Este é um trecho de código Python que define a interface gráfica de uma tela inicial de um sistema. 
    A classe TelaInicial define os elementos gráficos da tela, como botões, rótulos e a janela principal. 
    O método setupUi é responsável por configurar os elementos na janela, enquanto o método retranslateUi é usado para definir
    o texto dos elementos da interface. 
    O código usa a biblioteca PyQt5 para criar a interface gráfica.

    '''
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(291, 591)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-1, 0, 291, 591))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 291, 590))
        self.label.setStyleSheet("background-color:rgba(16, 30,    41, 240);\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.ButtonCadastrar = QtWidgets.QPushButton(self.widget)
        self.ButtonCadastrar.setGeometry(QtCore.QRect(20, 320, 121, 40))
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
        self.label_2.setGeometry(QtCore.QRect(55, 30, 191, 201))
        font = QtGui.QFont()
        font.setFamily("dripicons-v2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgba(0, 125, 236, 255);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("IMG/banco-de-dinheiro.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ButtonLogin = QtWidgets.QPushButton(self.widget)
        self.ButtonLogin.setGeometry(QtCore.QRect(150, 320, 121, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.ButtonLogin.setFont(font)
        self.ButtonLogin.setStyleSheet("QPushButton#ButtonLogin{\n"
"background-color: rgba(2, 65, 118, 255);\n"
"color: rgba(250, 250, 250, 200);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#ButtonLogin:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(2, 65, 118, 100);\n"
"background-position: calc(100% - 10px)center;\n"
"}\n"
"QPushButton#ButtonLogin:hover{\n"
"background-color: rgba(2, 65, 118, 200);\n"
"}")
        self.ButtonLogin.setObjectName("ButtonLogin")
        self.ButtonSair = QtWidgets.QPushButton(self.widget)
        self.ButtonSair.setGeometry(QtCore.QRect(25, 525, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.ButtonSair.setFont(font)
        self.ButtonSair.setStyleSheet("QPushButton#ButtonSair{\n"
"background-color: rgba(2, 65, 118, 255);\n"
"color: rgba(250, 250, 250, 200);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#ButtonSair:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(2, 65, 118, 100);\n"
"background-position: calc(100% - 10px)center;\n"
"}\n"
"QPushButton#ButtonSair:hover{\n"
"background-color: rgba(2, 65, 118, 200);\n"
"}")
        self.ButtonSair.setObjectName("ButtonSair")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ButtonCadastrar.setText(_translate("Form", "Cadastrar"))
        self.ButtonLogin.setText(_translate("Form", "Log In"))
        self.ButtonSair.setText(_translate("Form", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = TelaInicial()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
