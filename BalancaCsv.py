import os
array_total = []
def mudaParaCsv(tipo = 'Txitens'):
    #01
    #1
    #000015
    #001299
    #005
    #ABACAXI

    
    if(os.path.isfile('itensMGV.txt') and tipo == 'Itensmgv'):
        arquivoMGV6 = open('itensMGV.TXT', 'r')
        arquivoCsv = open('itensCSV.csv', 'w')
        array = []
        for linha in arquivoMGV6:
            plu = linha[3:9]
            if int(plu) < 201:
                nome = linha[18:34]
                preco = linha[10:15]
                vendaNum = int(linha[2])
                validade = linha[15:18]

##            if vendaNum == 0:
##                venda = 'Kg'
##            elif vendaNum == 1:
##                venda = 'Un'
##            else: venda = str(vendaNum)
            
                linhaCsv = f'{int(plu)};{nome};{(float(preco)/100):.2f};{vendaNum};{int(validade)}'

                arquivoCsv.write(linhaCsv + '\n')
            
        arquivoMGV6.close()
        arquivoCsv.close()
        return True

    elif(os.path.isfile('Txitens.txt') and tipo == 'Txitens'):
        arquivoMGV6 = open('Txitens.TXT', 'r')
        arquivoCsv = open('itensCSV.csv', 'w')
        array = []
        for linha in arquivoMGV6:
            plu = linha[5:11]
            if int(plu) < 201:
                nome = linha[20:35]
                preco = linha[11:16]
                vendaNum = int(linha[4])
                validade = linha[17:20]

##            if vendaNum == 0:
##                venda = 'Kg'
##            elif vendaNum == 1:
##                venda = 'Un'
##            else: venda = str(vendaNum)
                
                linhaCsv = f'{int(plu)};{nome};{(float(preco)/100):.2f};{vendaNum};{int(validade)}'

                arquivoCsv.write(linhaCsv + '\n')
            
        arquivoMGV6.close()
        arquivoCsv.close()
        return True
    else:
        print('arquivo não encontrado ou importação configurada incorretamente')
        return False

i = mudaParaCsv()
