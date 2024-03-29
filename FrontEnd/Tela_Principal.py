from PyQt5 import QtCore, QtGui, QtWidgets


class TelaPrincipal(object):
    '''
    Este é um trecho de código Python que define a interface gráfica da tela de principal do sistema. 
    A classe TelaPrincipal define os elementos gráficos da tela, como botões, rótulos e a janela principal. 
    O método setupUi é responsável por configurar os elementos na janela, enquanto o método retranslateUi é usado para definir
    o texto dos elementos da interface. 
    O código usa a biblioteca PyQt5 para criar a interface gráfica.
    '''
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(291, 596)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(2, 2, 291, 591))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(-1, 0, 291, 591))
        self.label.setStyleSheet("background-color:rgba(16, 30,    41, 240);\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.ButtonDepositar = QtWidgets.QPushButton(self.widget)
        self.ButtonDepositar.setGeometry(QtCore.QRect(20, 330, 121, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.ButtonDepositar.setFont(font)
        self.ButtonDepositar.setStyleSheet("QPushButton#ButtonDepositar{\n"
"background-color: rgba(2, 65, 118, 255);\n"
"color: rgba(250, 250, 250, 200);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#ButtonDepositar:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(2, 65, 118, 100);\n"
"background-position: calc(100% - 10px)center;\n"
"}\n"
"QPushButton#ButtonDepositar:hover{\n"
"background-color: rgba(2, 65, 118, 200);\n"
"}")
        self.ButtonDepositar.setObjectName("ButtonDepositar")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 91, 91))
        font = QtGui.QFont()
        font.setFamily("dripicons-v2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgba(0, 125, 236, 255);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("IMG/banco-de-dinheiro.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ButtonSacar = QtWidgets.QPushButton(self.widget)
        self.ButtonSacar.setGeometry(QtCore.QRect(150, 330, 121, 40))
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
        self.ButtonSair = QtWidgets.QPushButton(self.widget)
        self.ButtonSair.setGeometry(QtCore.QRect(20, 530, 250, 40))
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
        self.ButtonTransferir = QtWidgets.QPushButton(self.widget)
        self.ButtonTransferir.setGeometry(QtCore.QRect(20, 380, 121, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.ButtonTransferir.setFont(font)
        self.ButtonTransferir.setStyleSheet("QPushButton#ButtonTransferir{\n"
"background-color: rgba(2, 65, 118, 255);\n"
"color: rgba(250, 250, 250, 200);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#ButtonTransferir:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(2, 65, 118, 100);\n"
"background-position: calc(100% - 10px)center;\n"
"}\n"
"QPushButton#ButtonTransferir:hover{\n"
"background-color: rgba(2, 65, 118, 200);\n"
"}")
        self.ButtonTransferir.setObjectName("ButtonTransferir")
        self.ButtonHistorico = QtWidgets.QPushButton(self.widget)
        self.ButtonHistorico.setGeometry(QtCore.QRect(150, 380, 121, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.ButtonHistorico.setFont(font)
        self.ButtonHistorico.setStyleSheet("QPushButton#ButtonHistorico{\n"
"background-color: rgba(2, 65, 118, 255);\n"
"color: rgba(250, 250, 250, 200);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#ButtonHistorico:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(2, 65, 118, 100);\n"
"background-position: calc(100% - 10px)center;\n"
"}\n"
"QPushButton#ButtonHistorico:hover{\n"
"background-color: rgba(2, 65, 118, 200);\n"
"}")
        self.ButtonHistorico.setObjectName("ButtonHistorico")
        self.ButtonExcluir = QtWidgets.QPushButton(self.widget)
        self.ButtonExcluir.setGeometry(QtCore.QRect(20, 480, 251, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.ButtonExcluir.setFont(font)
        self.ButtonExcluir.setStyleSheet("QPushButton#ButtonExcluir{\n"
"background-color: rgba(2, 65, 118, 255);\n"
"color: rgba(250, 250, 250, 200);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#ButtonExcluir:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(2, 65, 118, 100);\n"
"background-position: calc(100% - 10px)center;\n"
"}\n"
"QPushButton#ButtonExcluir:hover{\n"
"background-color: rgba(2, 65, 118, 200);\n"
"}")
        self.ButtonExcluir.setObjectName("ButtonExcluir")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 251, 111))
        self.label_3.setStyleSheet("background-color: rgba(2, 65, 118, 255);\n"
"border-radius:15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.labelNome = QtWidgets.QLabel(self.widget)
        self.labelNome.setGeometry(QtCore.QRect(40, 120, 221, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelNome.setFont(font)
        self.labelNome.setObjectName("labelNome")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(40, 150, 111, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.labelSaldo = QtWidgets.QLabel(self.widget)
        self.labelSaldo.setGeometry(QtCore.QRect(40, 170, 141, 19))
        self.labelSaldo.setObjectName("labelSaldo")
        self.ButtonAtualizar = QtWidgets.QPushButton(self.widget)
        self.ButtonAtualizar.setGeometry(QtCore.QRect(190, 179, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.ButtonAtualizar.setFont(font)
        self.ButtonAtualizar.setStyleSheet("QPushButton#ButtonAtualizar{\n"
"background-color: rgba(0, 55, 100, 255);\n"
"color: rgba(250, 250, 250, 200);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#ButtonAtualizar:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(2, 65, 118, 100);\n"
"background-position: calc(100% - 10px)center;\n"
"}\n"
"QPushButton#ButtonAtualizar:hover{\n"
"background-color: rgba(0, 40, 80, 150);\n"
"}")
        self.ButtonAtualizar.setObjectName("ButtonAtualizar")
        self.labelNumero = QtWidgets.QLabel(self.widget)
        self.labelNumero.setGeometry(QtCore.QRect(40, 190, 63, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelNumero.setFont(font)
        self.labelNumero.setObjectName("labelNumero")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ButtonDepositar.setText(_translate("Form", "Depositar"))
        self.ButtonSacar.setText(_translate("Form", "Sacar"))
        self.ButtonSair.setText(_translate("Form", "Sair"))
        self.ButtonTransferir.setText(_translate("Form", "Transferir"))
        self.ButtonHistorico.setText(_translate("Form", "Historico"))
        self.ButtonExcluir.setText(_translate("Form", "Excluir"))
        self.labelNome.setText(_translate("Form", "Olá, Willians"))
        self.label_5.setText(_translate("Form", "Saldo em conta"))
        self.labelSaldo.setText(_translate("Form", "R$ 0.00"))
        self.ButtonAtualizar.setText(_translate("Form", "Atualizar"))
        self.labelNumero.setText(_translate("Form", "Conta 111"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = TelaPrincipal()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
