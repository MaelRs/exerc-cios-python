#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde os em um dicionario.
# No final, coloque rsse dicionario em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
print('\033[1:30:42m          JOGO DE DADOS          \033[m')
jogo={}
resultado=[]
jogo['Jogador 1']= randint(1,6)
jogo['Jogador 2']= randint(1,6)
jogo['Jogador 3']= randint(1,6)
jogo['Jogador 4']= randint(1,6)
resultado.append(jogo.copy())
ranking=[]
for k,v in jogo.items():
    print(f'O {k} tirou {v} no dado .')
    sleep(0.5)
ranking=sorted(jogo.items(),key=itemgetter(1),reverse=True)
print('-='*30)
print('\033[1:30:42m          Ranking dos Jogadores          \033[m')
for i, v in enumerate(ranking):
    print(f'No {i+1}° lugar está o {v[0]} com {v[1]} pontos ')
    sleep(0.5)

#if jogo['Jogador 1']>jogo['Jogador 2']>jogo['Jogador 3']>jogo['Jogador 4']:


