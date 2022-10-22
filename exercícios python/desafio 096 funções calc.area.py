#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
# terreno retangular {largura e comprimento} e mostre a área do terreno.
def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


titulo('CONTROLE DE TERRENOS')
def area(largura, comprimento):
    calc=largura*comprimento
    print(f'A area de um terreno de {largura} x {comprimento} é de {calc}m²')


largura=float(input('Largura (m): '))
comprimento=float(input('Comprimento (m): '))
area(largura,comprimento)
'''def area(a,b):
    print(f'Largura = {a},Comprimento= {b} .')
    calc=a*b
    print(f'A area de um terreno de {a} x {b} é de {calc}m²')


a=float(input('Largura (m): '))
b=float(input('Comprimento (m): '))
area(a,b)'''