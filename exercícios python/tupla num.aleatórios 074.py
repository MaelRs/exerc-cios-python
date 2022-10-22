#Crie um programa que vai gerar 5 números aleatórios e colocar em uma túpla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
num=(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f'Os Números sorteados foram:{num}',end=' ')
print(f'\nO maior valor sorteado foi {max(num)}.')
print(f'\nO Menor valor sorteado foi {min(num)}.')


