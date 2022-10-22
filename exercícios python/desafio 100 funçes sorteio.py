#faça um programa que tenha uma lista chamada numeros() e dus funç~eos chamadas sorteio() e somaPar().
# A Primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função
# vai mostrar a coma entre todos os valores PARES sorteados pela função anterior.
from random import randint
from time import sleep

def sorteio(lista):
    print('\033[1:30:42m SORTEANDO 5 NÚMEROS ALEATÓRIOS: \033[m',end=' ')
    for cont in range(0,5):
        n=randint(1,10)
        lista.append(n)
        print(f'{n}',end=' ')
        sleep(0.3)
    print('PRONTO!!')


def somaPar(lista):
    soma=0
    for valor in lista:
        if valor%2==0:
            soma+=valor
    print(f'Somando os valores pares de {lista} temos {soma}')


numeros=list()
sorteio(numeros)
somaPar(numeros)