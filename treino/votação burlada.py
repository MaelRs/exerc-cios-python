# Melhore o jogo do desafio 028 onde o computador vai pensar em um numero de 0 a 10.
# Só que agora o jogador vai tentar adivinhar a té acertar, Monstrando no final
# quantos palpites foram necessários para vencer.

lula=0
bolsonaro=0
voto=0

while True:
    print('Escolha seu voto'
          '\n[1]- lula'
          '\n[2]- bolsonaro'
          '\n[0]- Sair'
          )
    opção=int(input('O que você escolhe:'))

    if opção==1:
        lula+=1
        voto+=1
        #bolsonaro+=-1
        print('\033[1;30;41mSeu voto foi registrado para Lula \033[m')
        print('--' * 20)
        print('---- Placar ----')
        print(f'Bolsonaro={bolsonaro}')
        print(f'Lula={lula}')
        print('--' * 20)
    if opção==2:
        #lula+=10
        bolsonaro+=1
        voto+=1
        print('\033[1;30;42mSeu voto foi Registrado para Bolsonaro \033[m')
        print('--' * 20)
        print('---- Placar ----')
        print(f'Bolsonaro={bolsonaro}')
        print(f'Lula={lula}')
        print('--'*20)
    if opção==0:
        break

print(f'O total da votação para Lula foi {lula} e para Bolsonaro foi {bolsonaro}')
print(f'Foram registrados {voto} votos')
resb=voto/100*65
resl=voto/100*35

print(f'O Bolsonaro recebeu {resb}% de todos os votos')
print(f'O Lula Recebeu {resl}% de todos os votos.')

