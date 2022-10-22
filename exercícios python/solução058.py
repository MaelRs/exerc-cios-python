from random import randint
computador=randint(0,10)
print('Sou seu computador, acabei de pensar em um número entre  e 10.')
print('Será que vc consegue adivinhar qual é?')
acertou=False
palpites=0
while not acertou:
    jogador=int(input('Qual é o seu palpite? '))
    palpites=palpites+1
    if jogador==computador:
        acertou=True
    else:
        if jogador<computador:
            print('Mais... Tente mais uma vez.')
        elif jogador>computador:
            print('Menos... Tente novamente.')
print('Acertou!! Eu pensei no número {} e com {} palpites vc acertou'.format(computador,palpites))