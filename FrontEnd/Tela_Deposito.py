from PyQt5 import QtCore, QtGui, QtWidgets


class TelaDeposito(object):
    '''
    A classe TelaDeposito contém um método setupUi que define a aparência e comportamento dos widgets que compõem a tela, como uma label, 
    um QLineEdit para o usuário digitar o valor do depósito, dois QPushButtons para depositar e voltar, respectivamente, 
    e uma QLabel para exibir notificações. 
    A função retranslateUi é responsável por definir os textos dos widgets.
    '''
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(290, 594)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(1, 2, 291, 591))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(-1, 0, 291, 591))
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
        self.ButtonDepositar = QtWidgets.QPushButton(self.widget)
        self.ButtonDepositar.setGeometry(QtCore.QRect(20, 480, 250, 40))
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
        self.ButtonVoltar.setGeometry(QtCore.QRect(20, 530, 250, 40))
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
        self.labelNotificacao.setGeometry(QtCore.QRect(20, 290, 251, 20))
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
        self.ButtonDepositar.setText(_translate("Form", "Depositar"))
        self.ButtonVoltar.setText(_translate("Form", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = TelaDeposito()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
