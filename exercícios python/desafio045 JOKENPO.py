print('{:=^40}'.format('JOKENPO '))
from random import randint
from time import sleep
lista=('PEDRA','PAPEL','TESOURA')
computador=randint(0,2)
print('''ESCOLHA UMA OPÇÃO
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador=int(input('Qual é a sua jogada?  '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-='*20)
print('O computador jogou \033[1;30;107m {} \033[m'.format(lista[computador]))
print('O jogador jogou \033[1;97;41m {} \033[m'.format(lista[jogador]))
print('-='*20)
if computador==0 and jogador==1:
    print('Você Venceu!')
elif computador==1 and jogador==2:
    print('Você venceu!!')
elif computador==2 and jogador==0:
            print('Você Venceu')
elif jogador==0 and computador==1:
    print('Você Perdeu!')
elif jogador==1 and computador==2:
    print('Você perdeu!!')
elif jogador==2 and computador==0:
    print('Você perdeu!')
else:
    print('Deu Empate!')

#s=choice(lista)
#j=input('Digite uma opção de Pedra, Papel ou Tesoura: ')
#if s==p and j==papel:
    #print('Você venceu!!O item escolhido pelo computador é:{}'.format(s))
#elif s==t and j==p:
    #print('Você perdeu! O item escolhido pelo computador foi {}'.format(s))
#elif s==pp and j==t:
    #print('Você venceu!! o item escolhido pelo computador foi {}'.format(s))




