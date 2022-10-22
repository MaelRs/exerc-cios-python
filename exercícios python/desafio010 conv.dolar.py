print('\033[1;30;107m CONVERSÃO DE DOLAR(U$) PARA REAL (R$)\033[m')
saldo=float(input('Saldo em carteira: R$  '))
d=(saldo/3.27)
print('A quantidade de dolar que vc consegue comprar com R${} , é igual a :\033[1;30;42mU$$ {:.2f}\033[m'.format(saldo,d))