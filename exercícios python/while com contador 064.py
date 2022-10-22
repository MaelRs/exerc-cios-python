#Crie um programa que leia varios números inteiros pelo teclado. O programa so vai parar quando
# o usuario digitar o valor 999, que é a condição de parada no final mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag)
n=0
cont=0
soma=0
n=int(input('Digite um número:'))
while n!=999:
    cont=cont+1
    soma=soma+n
    n = int(input('Digite um número:'))

print('Foram digitados {} números e soma de todos eles é: {}'.format(cont,soma))