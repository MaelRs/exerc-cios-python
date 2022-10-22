# Faça um programa que tenha uma função chamada contador(), que receba tres parametros:
# início, fim e passo, e realize a contagem. Seu programa tem que realizar tres contagens, atravez da função criada:
# A)de 1 até 10 de 1 em 1
# B)de 10 até 0 de 2 em 2
# C)Uma contagem personalizada.
from time import sleep
def contador(i,f,p):
    if p<0:
        p*=-1
    if p==0:
        p=1
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    #sleep(0.5)
    if i<f:
        cont=i
        while cont<=f:
            print(f'{cont}',end='-')
            sleep(0.5)
            cont+=p
        print('FIM!!')
    else:
        cont=i
        while cont>=f:
            print(f'{cont}',end='-')
            sleep(0.5)
            cont-=p
        print('FIM!!')



contador(1,10,1)
contador(10,0,2)
print('-='*20)
print('Agora você escolhe a contagem')
inicio=int(input('Digite o início: '))
fim=int(input('Digite o fim: '))
passo=int(input('Digite o passo: '))
contador(inicio,fim, passo)