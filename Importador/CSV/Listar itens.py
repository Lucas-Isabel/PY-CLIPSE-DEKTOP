from tkinter import *


window = Tk()
window.grid()



window.array = []
canvas = Canvas(window, width = 1320, height=700)
canvas.grid(row=0, column=0, sticky="news")
scroll_bar = Scrollbar(window, orient=VERTICAL, command = canvas.yview)
scroll_bar.grid(row=0, column=1, sticky='ns')
canvas.config(yscrollcommand = scroll_bar.set)
produtos_frame = Frame(canvas)
canvas.create_window((0, 0), window=produtos_frame, anchor='ne')



def listaritens():
    arquivoCsv = open('itensCSV.csv', 'r')
    coluna = 0
    line = 0
    for linha in arquivoCsv:
        item = linha
        plu, desc, preço, venda, validade = item.split(';')
        arraydeprop = item.split(';')
        for prop in arraydeprop:
            tmp = Listbox(produtos_frame, width=10, height=1)
            window.array.append(prop)
            tmp.insert(END, prop)
            tmp.grid(ipadx=30,padx=0, pady=0, column=coluna, row=line)        
            coluna += 1
            if coluna > 4:
                coluna = 0
        line += 1
    #print(window.array)
    arquivoCsv.close()

    produtos_frame.update_idletasks()



    canvas.config(scrollregion=canvas.bbox("all"))
  


def editarItem(cod):
    arquivoCsv = open('itensCSV.csv', 'r')
    arquivoModificado = open('itensmod.csv', 'w')
    for linha in arquivoCsv:
        item = linha
        plu, desc, preço, venda, validade = item.split(';')
        numPlu = int(plu)
        if(cod == numPlu):
            arquivoModificado.write(f'{plu};{desc2};{preco2};{venda2};{val2}\n')
        else:
            arquivoModificado.write(linha)
       
    arquivoCsv.close()
    arquivoModificado.close()
            
#editarItem(1)


listaritens()
window.mainloop()
