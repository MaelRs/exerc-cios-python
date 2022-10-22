#Crie um programa que leia um número inteiro e diga se ele é par ou impar.
n=int(input('Digite um número:'))
result=n%2
#print('O resultado é: {}'.format(result))
if result==0:
    print('O número \033[1;33;107m {} \033[m , é \033[1;30;107m PAR \033[m.'.format(n))
else:
    print('O número \033[1;33;107m {} \033[m é \033[1;30;107m ÍMPAR \033[m.'.format(n))