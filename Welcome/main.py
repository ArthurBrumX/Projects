# Uma aplicacao GUI com o intuito de o usuario inserir suas informacoes e receber uma mensagem de boas vindas!

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from telaMain import Ui_MainWindow
import sys

class telaPrincipal(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(telaPrincipal,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela Princiál")

        self.bntConcluir.clicked.connect(lambda: self.bntConcluir.setCurrentWidget(self.BoasVindas))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = telaPrincipal()
    window.show()
    app.exec()
