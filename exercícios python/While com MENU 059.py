# Crie um programe que leia 2 valores e mostre um menu na tela:
# [1] somar [2] multiplicar [3]maior [4] novos números [5] sair do programa.
from time import sleep
n = int(input('Digite um número: '))
n1 = int(input('Digite um número: '))
opção=0
while opção!=5:
    print('''Escolha uma opção do menu:
    [1] Somar,
    [2] Multiplicar,
    [3] Maior
    [4] Novos números
    [5] sair do programa''')
    opção=int(input('Digite sua opção: '))
    if opção==1:
        resul=n+n1
        print('A soma dos numeros {} e {} é: {}' .format(n,n1,resul))
    elif opção==2:
        resul=n*n1
        print('A multiplicação entre {} e {} é: {}'.format(n,n1,resul))
    elif opção==3:
        if n>n1:
            maior=n
        else:
            maior=n1
        print('O maior entre {} e {} é {}'.format(n,n1,maior))
    elif opção==4:
        print('Informe os números novamente!')
        n=int(input('Digite um novo numero:'))
        n1=int(input('Digite outro novo numero:'))
    elif opção==5:
        print('Finalizando!')
        sleep(1)
        print('\033[1;31;107m Fim do programa!Volte sempre!\033[m')
        quit()
    else:
        print('Opção INVÁLIDA! Tente Novamente.')
    print('=-='*10)
    sleep(2)




