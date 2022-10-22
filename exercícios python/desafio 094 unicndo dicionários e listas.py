#Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados
# de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) uma lista com todas as mulheres
# c) uma lista com todas as pessoas com idade acima da média
galera=[]
pessoa={}
soma=media=0
while True:
    pessoa.clear()
    pessoa['nome']=str(input('Nome: '))
    sexo=' '
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]:')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
            print('\033[1:30:41m ERRO! Responda apenas M ou F :\033[m')
    pessoa['idade']=int(input('Idade: '))
    soma+=pessoa['idade']
    galera.append(pessoa.copy())
    perg=' '
    while perg not in 'SsNn':
        perg=str(input('Quer continuar? [S/N]: ')).strip().upper()
        if perg not in 'SsNn':
            print('\033[1:30:41m ERRO! Responda apenas S ou N \033[m')
    if perg=='N':
        break
print(f'A) Foram cadastradas {len(galera)} pessoas.')
media=soma/len(galera)
print(f'B) A média de idade das pessoas é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram' ,end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f' {p["nome"]}...',end=' ')
print(f'\nD) As pessoas que estão com idade acima da média são:', end=' ')
for p in galera:
    if p['idade']>=media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}',end=' ')
    print()
print('ENCERRADO')
