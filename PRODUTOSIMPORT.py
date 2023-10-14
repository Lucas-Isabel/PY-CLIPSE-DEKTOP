import serial
import time
from sklearn.utils import shuffle
from random import randint



def listaritens():
    porta = serial.Serial(port='COM20',
                      baudrate=9600,
                      bytesize=serial.EIGHTBITS,
                      parity=serial.PARITY_NONE,
                      stopbits=serial.STOPBITS_ONE)


    
    print(porta)


##    text = f'\x02001\x02'
##    text = bytearray(text, 'utf-8')
##    porta.write(text)
##    a = porta.read(size=3)
##    print(a)
    
    hexa = [
    "\x00",
    "\x01",
    "\x02",
    "\x03",
    "\x04",
    "\x05",
    "\x06",
    "\x07",
    "\x08",
    "\x09",
    "\x0a",
    "\x0b",
    "\x0c",
    "\x0d",
    "\x0e",
    "\x0f",
    "\x10",
    "\x11",
    "\x12",
    "\x13",
    "\x14",
    "\x15",
    "\x16",
    "\x17",
    "\x18",
    "\x19",
    "\x1a",
    "\x1b",
    "\x1c",
    "\x1d",
    "\x1e",
    "\x1f",
    "\x20",
    "\x21",
    "\x22",
    "\x23",
    "\x24",
    "\x25",
    "\x26",
    "\x27",
    "\x28",
    "\x29",
    "\x2a",
    "\x2b",
    "\x2c",
    "\x2d",
    "\x2e",
    "\x2f",
    "\x30",
    "\x31",
    "\x32",
    "\x33",
    "\x34",
    "\x35",
    "\x36",
    "\x37",
    "\x38",
    "\x39",
    "\x3a",
    "\x3b",
    "\x3c",
    "\x3d",
    "\x3e",
    "\x3f",
    "\x40",
    "\x41",
    "\x42",
    "\x43",
    "\x44",
    "\x45",
    "\x46",
    "\x47",
    "\x48",
    "\x49",
    "\x4a",
    "\x4b",
    "\x4c",
    "\x4d",
    "\x4e",
    "\x4f",
    "\x50",
    "\x51",
    "\x52",
    "\x53",
    "\x54",
    "\x55",
    "\x56",
    "\x57",
    "\x58",
    "\x59",
    "\x5a",
    "\x5b",
    "\x5c",
    "\x5d",
    "\x5e",
    "\x5f",
    "\xf0",
    "\xf1",
    "\xf2",
    "\xf3",
    "\xf4",
    "\xf5",
    "\xf6",
    "\xf7",
    "\xf8",
    "\xf9",
    "\xfa",
    "\xfb",
    "\xfc",
    "\xfd",
    "\xfe",
    "\xff",
    "\x60",
    "\x61",
    "\x62",
    "\x63",
    "\x64",
    "\x65",
    "\x66",
    "\x67",
    "\x68",
    "\x69",
    "\x6a",
    "\x6b",
    "\x6c",
    "\x6d",
    "\x6e",
    "\x6f",
    "\x70",
    "\x71",
    "\x72",
    "\x73",
    "\x74",
    "\x75",
    "\x76",
    "\x77",
    "\x78",
    "\x79",
    "\x7a",
    "\x7b",
    "\x7c",
    "\x7d",
    "\x7e",
    "\x7f",
    "\x80",
    "\x81",
    "\x82",
    "\x83",
    "\x84",
    "\x85",
    "\x86",
    "\x87",
    "\x88",
    "\x89",
    "\x8a",
    "\x8b",
    "\x8c",
    "\x8d",
    "\x8e",
    "\x8f",
    "\x90",
    "\x91",
    "\x92",
    "\x93",
    "\x94",
    "\x95",
    "\x96",
    "\x97",
    "\x98",
    "\x99",
    "\x9a",
    "\x9b",
    "\x9c",
    "\x9d",
    "\x9e",
    "\x9f",
    "\xa0",
    "\xa1",
    "\xa2",
    "\xa3",
    "\xa4",
    "\xa5",
    "\xa6",
    "\xa7",
    "\xa8",
    "\xa9",
    "\xaa",
    "\xab",
    "\xac",
    "\xad",
    "\xae",
    "\xaf",
    "\xb0",
    "\xb1",
    "\xb2",
    "\xb3",
    "\xb4",
    "\xb5",
    "\xb6",
    "\xb7",
    "\xb8",
    "\xb9",
    "\xba",
    "\xbb",
    "\xbc",
    "\xbd",
    "\xbe",
    "\xbf",
    "\xc0",
    "\xc1",
    "\xc2",
    "\xc3",
    "\xc4",
    "\xc5",
    "\xc6",
    "\xc7",
    "\xc8",
    "\xc9",
    "\xca",
    "\xcb",
    "\xcc",
    "\xcd",
    "\xce",
    "\xcf",
    "\xd0",
    "\xd1",
    "\xd2",
    "\xd3",
    "\xd4",
    "\xd5",
    "\xd6",
    "\xd7",
    "\xd8",
    "\xd9",
    "\xda",
    "\xdb",
    "\xdc",
    "\xdd",
    "\xde",
    "\xdf",
    "\xe0",
    "\xe1",
    "\xe2",
    "\xe3",
    "\xe4",
    "\xe5",
    "\xe6",
    "\xe7",
    "\xe8",
    "\xe9",
    "\xea",
    "\xeb",
    "\xec",
    "\xed",
    "\xee",
    "\xef",
    ]


    ini = 0
    fim = 0
    a = ''
    funcionou = []
    naofuncionou = []
    maisrepetidos = []
    arquivoCsv = open('itensCSV.csv', 'r')
    coluna = 0
    line = 0
    c1 = 0
    c2 = 0
    hexa_copy = hexa
    a = ''
    indiceMeio = int((len(hexa_copy)/2 -2))
    
    for linha in arquivoCsv:
        itFinal = -1
        itMeio = indiceMeio
        itMeioMenosUm = indiceMeio
        c1 = 0
        item = linha
        plu, desc, preco, venda, validade = item.split(';')
        #print(plu, desc, preco, venda, validade, sep='')
        print(plu)
        preco = preco.replace('.','')
        if venda == '0':
            venda = "\x10"
        elif venda == '1':
            venda = '\x20'
        if len(plu) < 3:
            plu =  '0'*(3-len(plu))  + plu
        if len(desc) < 15:
            desc = desc + ' '*(15-len(desc))
        if len(preco) < 6:
            preco = '0'*(6-len(preco)) + preco
        if len(validade) < 3:
            validade = '0'*(3-len(validade)) + validade
        meio = time.time()
        meio = meio - ini
        #print(f"criou o array: {meio}")  
        #print(plu, desc, preco, venda, validade)
        if True:
            print(c1)
            for t in hexa:
                text = f'\x03{plu}{desc}00{preco}{validade}\x10{t}'
                text = bytearray(text, 'utf-8')
                porta.write(text)
                a = porta.read(size=3)
                print(a)
                if a != b'E1t' and a != b'E5p':
                    #print(f'antes do meio -- saida: {a}   posicao:{c1}    plu: {plu}')
                    funcionou.append(f'{a}: {plu} + {c1} + {t}')
                    break
##                print(c1)
##                print("apartir do meio: ",itMeio)
##                print("apartir do meio: ", itMeioMenosUm)
##                print("do final: ", itFinal)



                if itMeio != 256:
                    item = hexa_copy[itMeio]
                text = f'\x03{plu}{desc}00{preco}{validade}\x10{item}'
                text = bytearray(text, 'utf-8')
                porta.write(text)
                a = porta.read(size=3)
                if a != b'E1t' and a != b'E5p':
                    #print(f'depois do meio -- saida: {a}   posicao:{c1}    plu: {plu}')
                    funcionou.append(f'{a}: {plu} + {c1} + {t}')
                    c2 += 1
                    break


                item = hexa_copy[itFinal]
                text = f'\x03{plu}{desc}00{preco}{validade}\x10{item}'
                text = bytearray(text, 'utf-8')
                porta.write(text)
                a = porta.read(size=3)
                if a != b'E1t' and a != b'E5p':
                    #print(f'depois do meio -- saida: {a}   posicao:{c1}    plu: {plu}')
                    funcionou.append(f'{a}: {plu} + {c1} + {t}')
                    c2 += 1
                    break
##
##
##                item = hexa_copy[itMeio]
##                text = f'\x03{plu}{desc}00{preco}{validade}\x10{item}'
##                text = bytearray(text, 'utf-8')
##                porta.write(text)
##                a = porta.read(size=3)
##                if a != b'E1t' and a != b'E5p':
##                    #print(f'depois do meio -- saida: {a}   posicao:{c1}    plu: {plu}')
##                    funcionou.append(f'{a}: {plu} + {c1} + {t}')
##                    c2 += 1
##                    break

                item = hexa_copy[itMeioMenosUm]
                text = f'\x03{plu}{desc}00{preco}{validade}\x10{item}'
                text = bytearray(text, 'utf-8')
                porta.write(text)
                a = porta.read(size=3)
                if a != b'E1t' and a != b'E5p':
                    #print(f'depois do meio -- saida: {a}   posicao:{c1}    plu: {plu}')
                    funcionou.append(f'{a}: {plu} + {c1} + {t}')
                    c2 += 1
                    break


                itMeioMenosUm -= 1                
                itFinal -= 1
                itMeio += 1
                c1+=1








##            for xor in hexa:
##                print(plu, desc, preco.replace('.', ''), venda, validade, sep='')
##                text = f'x\02{plu}{desc}00{preco}{validade}{venda}{xor}'
##                print(text)
##                bytetext = bytearray(text, 'utf-8')
##                porta.write(bytetext)
##                saida = porta.read(size=1)
##                print(saida)




    if a == b'E1t' or a == b'E5p':
        naofuncionou.append(f'{a} + {plu}')
    print("FORAM IMPORTADOS:  ", len(funcionou), end="\n\n")
    #print(funcionou)
    print(len(naofuncionou), end="\n\n")
    print(naofuncionou)
    arquivoCsv.close()
    
    print(fim - ini)
    print(maisrepetidos)
    print(c2)



    ini = time.time()
    #print("\n\n\n\n\n\n\n"+str(len(hexa))+"\n\n\n\n\n\n\n")
    #listaritens()
    fim = time.time()
    print(f"""
    ===================================================================================================================================================================

                                o tempo total foi de:               {fim - ini}

    ====================================================================================================================================================================

                                """)



#listaritens()


