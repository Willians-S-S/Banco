from PyQt5 import QtCore, QtGui, QtWidgets


class TelaHistorico(object):
    '''
    Essa é uma classe que define a interface gráfica de uma tela de histórico em PyQt5. Ela cria uma janela sem bordas e com fundo translúcido, 
    e contém um label e um botão para voltar, estilizados com cores personalizadas. 
    Além disso, ela também inclui um QTextBrowser para exibir o histórico.
    '''
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(293, 593)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(1, 1, 291, 591))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(1, 0, 291, 591))
        self.label.setStyleSheet("background-color:rgba(16, 30,    41, 240);\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.ButtonVoltar = QtWidgets.QPushButton(self.widget)
        self.ButtonVoltar.setGeometry(QtCore.QRect(20, 520, 250, 40))
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
        self.textHistorico = QtWidgets.QTextBrowser(self.widget)
        self.textHistorico.setGeometry(QtCore.QRect(12, 18, 261, 471))
        self.textHistorico.setStyleSheet("background-color:rgba(16, 30,    41, 240);\n"
"border-radius:10px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textHistorico.setFont(font)

        self.textHistorico.setObjectName("textHistorico")
        
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ButtonVoltar.setText(_translate("Form", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = TelaHistorico()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
