# Crie um programa que leia vários números inteiros pelo teclado.No final da execução
# mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
r='S'
quant=0
soma=0
media=0
while r in 'Ss':
    n=int(input('Digite um número: '))
    soma+=n
    quant+=1
    if quant==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    r=str(input('Deseja continuar digitando:[S/N] ')).strip().upper()
media=soma/quant
print('Você digitou {} números e a média foi {}, o maior valor dentre eles foi {} '
      'e o menor foi {}'.format(quant,media,maior,menor))


