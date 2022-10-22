from random import randint #jogo de adivinhação
import time
print('Estou pensando em um número, tente adinvinhá-lo!...')
print('--'*20)
n=int(input('Em que número eu pensei? ')) #o jogador indica o número
print('--'*20)
print('PROCESSANDO...')
time.sleep(3)
nc=(randint(0,5)) #faz o computador pensar
print('--'*20)
#print('Eu pensei no número: {} ' .format(nc))
if n==nc:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print('GAME OVER!!!!Você perdeu! Eu pensei no número {} e não no {}!KKKK'.format(nc,n))


