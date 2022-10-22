from random import randint
print('=='*30)
print('VAMOS JOGAR PAR OU IMPAR?')
print('=='*30)
vit=0
while True:
    computador=randint(1,10)
    jogador=int(input('Digite um número: '))
    opção=str(input('PAR ou IMPAR? [P/I] : ')).strip().upper()
    while opção not in 'PpIi':
        opção = str(input('PAR ou IMPAR? [P/I] : ')).strip().upper()[0]
    if (jogador+computador)%2==0:
        result='Par'
    else:
        result='Impar'

    if opção=='P'and result=='Par' or opção=='I'and result=='Impar':
        soma=jogador+computador
        vit+=1
        print(f'Voce venceu!Você jogou o número {jogador}, o computador jogou o número {computador},'
              f' a soma resultou em {soma} que gerou um número {result}')
    else:
        break
#print(f'Você perdeu! Você jogou o número {jogador}, o computador jogou o número {computador},
# a soma resultou em {soma} que gerou um número {result}')
print(f'Após vencer por {vit} vez(es), você Perdeu essa!')
