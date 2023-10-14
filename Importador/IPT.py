from tkinter import *
from tkinter import ttk
import BalancaCsv
import os



def ipt(self):
    self.title('CLIPSE IMPORTADOR')
    self.portas = ['COM1',
                   'COM2',
                   'COM3',
                   'COM4',
                   'COM5']
    self.formatos = ['Csv',
                    'Itensmgv',
                    'Txitens']
    self.velocidades = [2400,
                   9600,
                   115200,]
    

    self.fontePadrao = ("Arial", "10")
    self.primeiroContainer = Frame(self)
    self.primeiroContainer["pady"] = 10
    self.primeiroContainer.pack()

    self.segundoContainer = Frame(self)
    self.segundoContainer["padx"] = 10
    self.segundoContainer.pack()

    self.terceiroContainer = Frame(self)
    self.terceiroContainer["padx"] = 50
    self.terceiroContainer["pady"] = 60
    self.terceiroContainer.pack()
    
    self.quartoContainer = Frame(self)
    self.quartoContainer["pady"] = 10
    self.quartoContainer.pack()

    self.quintoContainer = Frame(self)
    self.quintoContainer["pady"] = 10
    self.quintoContainer.pack()

    self.penultimoContainer = Frame(self)
    self.penultimoContainer["pady"] = 100
    self.penultimoContainer.pack()

    self.titulo = Label(self.primeiroContainer, text="Importador Andine\n\n\n\n")
    self.titulo["font"] = ("Arial", "10", "bold")
    self.titulo.pack()

    self.formatoLabel = Label(self.segundoContainer,text="Formato do arquivo: ", font=self.fontePadrao)
    self.formatoLabel.pack(side=LEFT)
    self.formato = ttk.Combobox(self.segundoContainer, values=self.formatos)
    self.formato["width"] = 70
    self.formato.pack()


    self.velocidadeLabel = Label(self.terceiroContainer,text="Velocidade:            ", font=self.fontePadrao)
    self.velocidadeLabel.pack(side=LEFT)
    self.velocidade = ttk.Combobox(self.terceiroContainer, values=self.velocidades)
    self.velocidade.pack(side=LEFT)

    #self.nome = Entry(self.terceiroContainer)
    #self.nome["width"] = 30
    #self.nome["font"] = self.fontePadrao
    #self.nome.pack(side=LEFT)


    self.portaLabel = Label(self.terceiroContainer, text="         Porta:                    ", font=self.fontePadrao)
    self.portaLabel.pack(side=LEFT)
    self.porta = ttk.Combobox(self.terceiroContainer, values=self.portas)
    self.porta.pack()


    #self.senha = Entry(self.quartoContainer)
    #self.senha["width"] = 30
    #self.senha["font"] = self.fontePadrao
    #self.senha["show"] = "*"
    #self.senha.pack(side=LEFT)

    #self.autenticar = Button(self.quartoContainer)
    #self.autenticar["text"] = "Autenticar"
    #self.autenticar["font"] = ("Calibri", "8")
    #self.autenticar["width"] = 12
    #self.autenticar["command"] = self.verificaSenha
    #self.autenticar.pack()

    #elf.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
    #self.mensagem.pack()

    #self.formato = ttk.Combobox(self.quartoContainer, values=[1,2,3])
    #self.formato.pack()

    self.caminhoLabel = Label(self.quintoContainer,text="Caminho do arquivo:", font=self.fontePadrao)
    self.caminhoLabel.pack(side=LEFT)
    
    self.caminho = Entry(self.quintoContainer)
    self.caminho["width"] = 65
    self.caminho["font"] = self.fontePadrao
    self.caminho.pack(side=LEFT)

    self.teste = "Importar"
    self.autenticar = Button(self.penultimoContainer)
    self.autenticar["text"] = self.teste
    self.autenticar["font"] = ("Calibri", "10")
    self.autenticar["width"] = 12
    self.autenticar["height"] = 2
    self.autenticar["command"] = self.config
    self.autenticar.pack(side=LEFT)


    self.sera = '' #Label(self.quintoContainer,text="Caminho do arquivo:", font=self.fontePadrao)
    self.sera2 = '' #Entry(self.quintoContainer)]

    
#Método verificar senha
def verificaSenha(self):
    usuario = self.nome.get()
    senha = self.senha.get()
    if usuario == "usuariodevmedia" and senha == "dev":
        self.mensagem["text"] = "Autenticado"
    else:
        self.mensagem["text"] = "Erro na autenticação"

def config(self):
    caminho = self.caminho.get()
    porta = self.porta.get()
    velocidade = self.velocidade.get()
    formato = self.formato.get()

    configuracoes = open('config.txt', 'w')
    configuracoes.write(str( caminho )+'\n')
    configuracoes.write(str( porta  )+'\n')
    configuracoes.write(str( velocidade )+'\n')
    configuracoes.write(str( formato )+'\n')
    configuracoes.close()
    self.pegarDadosconfig()

def pegarDadosconfig(self):
    if self.caminho.get() != '':
        print(1)
        props =[]
        configs = open('config.txt', 'r')
        for linha in configs:
            props.append(linha)
        self.autenticar["text"] = "importado"
        print(props)
        configs.close()
        BalancaCsv.mudaParaCsv(tipo = props[3].strip('\n'))
        


##root = Tk()
##ipt(root)
##root.mainloop()
