n1=float(input('Digite a primeira Nota: '))
n2=float(input('Digite a segunda nota: '))
m=(n1+n2)/2
#print(m)
if m>=7:
    print('\033[1;30;42m PARABENS! Você Foi APROVADO!!\033[m')

elif m<5:
    print('Você foi \033[1;97;40m REPROVADO \033[m!!')
elif m>=5 or m<=6.9:
    print('Você está em \033[1;30;41m RECUPERAÇÃO!! \033[m')
