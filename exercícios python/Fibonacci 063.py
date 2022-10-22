# Escreva um programa que leia um numero n inteiro qualquer e # mostre na tela os n primeiros
# elementos de uma sequencia fibonacci. Ex: 0-1-1-2-3-5-8
print('--'*15)
print('\033[1;31;107m    SEQUENCIA DE FIBONACCI    \033[m')
print('--'*15)
n=int(input('Quantos termos você quer mostrar? '))
t1=0
t2=1

print('~'*30)
print('{} - {}'.format(t1,t2),end=' ')
cont=3
while cont<=n:
    t3=t1+t2
    print('- {}'.format(t3),end=' ')
    t1=t2
    t2=t3
    cont+=1

print('- Fim!')

