#main

from tkinter import filedialog
from tkinter import font
from tkinter import *
from tkinter import messagebox
import csv
from Importador import IPT
from CSV import Table
import PRODUTOSIMPORT 


class Application:
    def __init__(self, master=None):
        master.configure(bg='white')
        master.title('CLIPSE IMPORTADOR')
        master.iconbitmap('qendra.ico')
        self.cor = "WHITE"
        #d9d923
        self.fontePadrao = ("Arial", "30")
        self.primeiroContainer = Frame(master)
        master.geometry("800x500")
        self.primeiroContainer["pady"] = 0
        self.primeiroContainer["bg"] = self.cor
        self.primeiroContainer.pack(side = TOP, anchor= "w")

        self.segundoContainer = Frame(self.primeiroContainer)
        self.segundoContainer["pady"] = 1
        self.segundoContainer["padx"] = 3
        self.segundoContainer["width"] = 0
        self.segundoContainer["bg"] = self.cor
        self.segundoContainer.pack(side = TOP)

        self.terceiroContainer = Frame(self.primeiroContainer)
        self.terceiroContainer["padx"] = 0
        self.terceiroContainer["width"] = 0
        self.terceiroContainer.pack(side = BOTTOM)

        
        self.menubar = Menu()

        
        self.configmenu = Menu(self.menubar, tearoff=0)
        self.configmenu.add_command(label="Equipamento", command=self.nada)
        self.configmenu.add_command(label="Importador", command= self.ipt)
        self.configmenu.add_command(label="Aparencia", command=self.nada)
        self.configmenu.add_command(label="...", command=self.nada)

        self.menubar.add_cascade(label="⚙️ Configurações", menu=self.configmenu)
        self.menubar.add_command(label="Equipamento", command=self.nada)
        self.menubar.add_command(label="? Ajuda", command=self.nada)

        master.title('   Clipse programa principal')
        master.config(menu=self.menubar)
        


        fonte = ("Times New Roman", "12")
        comprimento = 18
        altura = 2




        btnProdutos = Button(self.segundoContainer)
        btnProdutos["command"] = self.produtos
        btnProdutos["text"] = "🍇  PRODUTOS"
        btnPeso = Button(self.segundoContainer)
        btnPeso["command"] = self.nada
        btnPeso["text"] = "⚓️  PESO"
        btnImportar = Button(self.segundoContainer)
        btnImportar["text"] = "🔄  IMPORTAR"
        btnImportar["command"] = self.importa
##        btnConfig = Button(self.segundoContainer)
##        btnConfig["text"] = "⚙️  CONF."
##        btnConfig["command"] = self.nada


            
        for btn in (btnProdutos, btnPeso, btnImportar,): #btnConfig):  
            btn["font"] = fonte
            btn["width"] = comprimento
            btn["height"] = altura
            btn["bg"] = self.cor
            btn["bd"] = 0
            btn["fg"] = "BLACK"
            btn.pack(side = LEFT)
    
        
        
        l = Label(background="#000745")
        l.pack(fill='both',expand=True)

        self.default_font = font.nametofont("TkTextFont")
        self.default_font.configure(family="Helvetica")



    def nada(self):
        return 0
    

    def ipt(self):
        root = Tk()
        IPT.ipt(root)

    def produtos(self):
        print(10)
        Table.listar()
 
    def importa(self):
        print(10)
        PRODUTOSIMPORT.listaritens()
    


root = Tk()
Application(root)
root.mainloop()


    
    
