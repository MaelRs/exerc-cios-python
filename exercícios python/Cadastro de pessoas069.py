m18=0
th=0
mm20=0
while True:
    idade=int(input('Digite a idade: '))
    sexo=' '
    while sexo not in 'MmFf':
        sexo=str(input('Sexo: [M/F] ')).strip().upper()[0]
    resp=' '
    while resp not in 'SsNn':
        resp=str(input('Deseja continuar: [Ss/Nn] ')).strip().upper()[0]
    if idade>18:
        m18+=1
    if sexo=='M':
        th+=1
    if sexo=='F' and idade<20:
        mm20+=1
    if resp=='N':
        break
print(f'A quantidade de pessoas com mais de 18 anos cadastrada foi de {m18},\n '
      f'o número de homens cadastrados foi de {th},\no total de mulheres com menos de 20 anos é {mm20}.')
print('Fim!')