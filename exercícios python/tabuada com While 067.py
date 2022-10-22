#faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado pelo usuario
# o programa será interrompido quando o número solicitado for negativo.
print('=='*25)
n=int(input('Quer ver a tabuada de qual número? digite: '))
print('=='*25)
if n < 0:
    print('Programa tabuada encerrado. VOLTE SEMPRE!')
    quit()
else:
    for c in range(1, 11):
        print(n, 'x', c, '=', n * c)

    while n>0:
        print('==' * 25)
        n=int(input('Quer ver a tabuada de qual número? digite:  '))
        print('==' * 25)
        if n < 0:
           print('Programa tabuada encerrado. VOLTE SEMPRE!')
           quit()
        else:
            for c in range(1, 11):
                print(n, 'x', c, '=', n * c)

print('Fim')

