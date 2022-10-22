#crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada o programa deverá perguntar se o usuario quer ou nao continuar.
# No final, mostrar:
# a) Quantas pessoas tem mais de 18 anos;
# b)Quantos homens foram cadastrados;
# c)Quantas mulheres tem menos de 20 anos
print('=='*33)
print('                    CADASTRO DE PESSOAS      ')
print('=='*33)
p='S'
m18=0
hc=0
mm20=0
while p in 'Ss':
    idade = int(input('Digite a idade:'))
    sexo = str(input('Sexo:')).strip().upper()
    while sexo not in 'MmFf':
        sexo = str(input('Sexo:')).strip().upper()
    print('=='*33)
    p = str(input('Deseja continuar? [S/N]:'))
    while p not in 'SsNn':
        p = str(input('Deseja continuar? [S/N]:'))
    print('=='*33)
    if idade>=18:
        m18=m18+1
    if sexo=='M':
        hc=hc+1
    if sexo=='F' and idade<20:
        mm20=mm20+1



print(f'A quantidade de pessoas com mais de 18 anos cadastradas foram {m18},\n'
      f'a quantidade de homens cadastrados foi {hc} e \n '
      f'o total de mulheres com menos de 20 anos é: {mm20}')

