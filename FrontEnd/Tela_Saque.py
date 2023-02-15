from PyQt5 import QtCore, QtGui, QtWidgets


class TelaSaque(object):
    '''
    Este é um trecho de código Python que define a interface gráfica da tela de saque do sistema. 
    A classe TelaSaque define os elementos gráficos da tela, como botões, rótulos e a janela principal. 
    O método setupUi é responsável por configurar os elementos na janela, enquanto o método retranslateUi é usado para definir
    o texto dos elementos da interface. 
    O código usa a biblioteca PyQt5 para criar a interface gráfica.
    '''
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(295, 594)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(2, 2, 291, 591))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 291, 591))
        self.label.setStyleSheet("background-color:rgba(16, 30,    41, 240);\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineSaldo = QtWidgets.QLineEdit(self.widget)
        self.lineSaldo.setGeometry(QtCore.QRect(20, 210, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineSaldo.setFont(font)
        self.lineSaldo.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px")
        self.lineSaldo.setObjectName("lineSaldo")
        self.ButtonSacar = QtWidgets.QPushButton(self.widget)
        self.ButtonSacar.setGeometry(QtCore.QRect(20, 490, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.ButtonSacar.setFont(font)
        self.ButtonSacar.setStyleSheet("QPushButton#ButtonSacar{\n"
"background-color: rgba(2, 65, 118, 255);\n"
"color: rgba(250, 250, 250, 200);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#ButtonSacar:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(2, 65, 118, 100);\n"
"background-position: calc(100% - 10px)center;\n"
"}\n"
"QPushButton#ButtonSacar:hover{\n"
"background-color: rgba(2, 65, 118, 200);\n"
"}")
        self.ButtonSacar.setObjectName("ButtonSacar")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 141, 121))
        font = QtGui.QFont()
        font.setFamily("dripicons-v2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgba(0, 125, 236, 255);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("IMG/pilha-de-moedas-de-dolar.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
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
        self.lineSenha = QtWidgets.QLineEdit(self.widget)
        self.lineSenha.setGeometry(QtCore.QRect(20, 250, 250, 30))
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
        self.labelNotificacao = QtWidgets.QLabel(self.widget)
        self.labelNotificacao.setGeometry(QtCore.QRect(20, 340, 251, 20))
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
        self.lineSaldo.setPlaceholderText(_translate("Form", "  R$ "))
        self.ButtonSacar.setText(_translate("Form", "Sacar"))
        self.ButtonVoltar.setText(_translate("Form", "Voltar"))
        self.lineSenha.setPlaceholderText(_translate("Form", "  Senha"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = TelaSaque()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
