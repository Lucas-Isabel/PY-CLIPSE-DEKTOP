from tkinter import *



def listar():
    window = Tk()
    window.grid()
    window.array = []
##    btnPlu = Button(window, width = 5)
##    btnPlu.grid(row=0, column=0, stick='w')
##    inputPlu = Entry(window)
##    inputPlu.grid(row=0, column=0, stick='w')
    canvas = Canvas(window, width = 700, height=400)
    canvas.grid(row=1, column=0, sticky="news", padx=15, pady=15)
    scroll_bar = Scrollbar(window, orient=VERTICAL, command = canvas.yview)
    scroll_bar.grid(row=1, column=1, sticky='ns')
    canvas.config(yscrollcommand = scroll_bar.set)
    produtos_frame = Frame(canvas)
    canvas.create_window((0, 0), window=produtos_frame, anchor='ne')



    def listaritens():
        arquivoCsv = open('itensCSV.csv', 'r')
        coluna = 0
        line = 2
        for linha in arquivoCsv:
            item = linha
            plu, desc, preço, venda, validade = item.split(';')
            if len(plu) < 4:
                textPlu = '0'*(3 - len(plu)) + plu
            textpreco = 'R$ ' + (preço).replace('.', ',')
            textVenda = ''
            if venda == '0':
                textVenda = 'PESAVEL'
            elif venda == '1':
                textVenda = 'UNITARIO'
            textValidade = validade + ' DIAS'
            arraydeprop = []
            arraydeprop.append('PLU')
            arraydeprop.append('DESCRICAO')
            arraydeprop.append('PRECO')
            arraydeprop.append('VENDA')
            arraydeprop.append('VALIDADE')
            arraydeprop.append(textPlu)
            arraydeprop.append(desc)
            arraydeprop.append(textpreco)
            arraydeprop.append(textVenda)
            arraydeprop.append(textValidade)
            
            for prop in arraydeprop:
                if coluna == 0 or coluna == 2:
                    tmp = Listbox(produtos_frame, width=7, height=1, font='Calibri, 10')
                else:
                    tmp = Listbox(produtos_frame, width=10, height=1, font='Calibri, 10')
                window.array.append(prop)
                tmp.insert(END, prop)
                if coluna == 0 or coluna == 2:
                    tmp.grid(ipady=2, ipadx=0,padx=0, pady=0, column=coluna, row=line)
                else:
                    tmp.grid(ipady=2, ipadx=30,padx=0, pady=0, column=coluna, row=line) 
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

#listar()
