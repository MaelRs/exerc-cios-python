# Crie um programe que leia 2 valores e mostre um menu na tela:
# [1] somar [2] multiplicar [3]maior [4] novos números [5] sair do programa.
n=int(input('Digite um número:'))
n1=int(input('digite um numero:'))
while True:
    print('''\033[1;30;43m  Escolha a ação no MENU abaixo:\033[m    
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMERO
    [5] SAIR DO PROGRAMA''')
    ação=(int(input('Digite uma ação:  ')))
    if ação!=1 and ação!=2 and ação!=3 and ação!=4 and ação!=5:
        print('\033[2;97;103m Opção INVÁLIDA, tente novamente! \033[m')

    if ação==1:
        soma=n+n1
        print(f'\033[1;30;107m A soma de {n} e {n1} é:{soma}  \033[m ')
        print('--'*15)
    if ação==2:
        mult=(n*n1)
        print(f'\033[1;30;41m O produto da multiplicação dos números {n} e {n1} é:{mult}  \033[m')
        print('--' * 15)
    if ação==3:
        if n>n1 and n!=n1:
            maior=n
        else:
            maior=n1
        print(f'\033[2;31;40m O maior valor digitado entre {n} e {n1} é: {maior}  \033[m')
    if ação==3 and n==n1:
        print('Os números digitados são IGUAIS.')
        print('--' * 15)
    if ação==4:
        n = int(input('Digite um número:'))
        n1 = int(input('digite um numero:'))
    if ação==5:
        print('ENCERRANDO O SISTEMA!! VOLTE SEMPRE!!!')
        break

