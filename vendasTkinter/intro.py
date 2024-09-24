# Começo do projeto 20/09/2024

# Importar Bibliotecas

from tkinter import ttk
from tkinter import *

class splash:
    def __init__(self):
        self.splashmainw = Tk()
        self.splashmainw.title("Curso de vendas em Python Tkinter")
        width = 900
        heigth = 670
        self.splashmainw.config("green")
        tela_largura = self.splashmainw.winfo_screenwidth()
        tela_altura = self.splashmainw.winfo_screenwidth()
        x = (tela_largura / 2) - (width / 2)
        y = (tela_altura / 2) - (heigth / 2)
        self.slpashmainw.geometry("%dx%d+%d+%d" % (width,heigth,x,y))
        self.splashmainw.resizable(0,0)
