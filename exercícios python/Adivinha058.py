# Melhore o jogo do desafio 028 onde o computador vai pensar em um numero de 0 a 10.
# Só que agora o jogador vai tentar adivinhar até acertar, Monstrando no final
# quantos palpites foram necessários para vencer.
contn=1
from random import randint
from time import sleep
print('Estou pensando em um número, tente adivinhá-lo...')
n=int(input('Em qual número estou pensando: '))
nc=randint(1,10)
#acertou=False
while n!=nc:
    n = int(input('Tente novamente:'))
    contn=contn+1
print('Eu pensei no número {}.'.format(nc))
print('Após {} tentativas você conseguiu acertar! Eu pensei no número {} e você digitou {} PARABENS!'.format(contn,nc,n))