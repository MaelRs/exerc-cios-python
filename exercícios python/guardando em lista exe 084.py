#Faça um programa que leia Nome e peso de várias pessoas,guardando tudo em uma lista. No final mostre:
# a)Quantas pessoas foram cadastradas,
# b)Uma listagem com as pessoas mais pesadas.
# c)Uma listagem com as pessoas mais leves.
pessoas=[]
dados=[]
mai=men=0
while True:
    nome=(str(input('Nome: '))).strip().upper()
    dados.append(nome)
    peso=(int(input('peso: ')))
    dados.append(peso)
    if len(pessoas)==0:
        mai=men=dados[1]
    else:
        if dados[1]>mai:
            mai=dados[1]
        if dados[1]<men:
            men=dados[1]
    pessoas.append(dados[:])
    dados.clear()
    perg=' '
    while perg not in 'SsNn':
        perg=str(input('Deseja continuar? [S/N]')).strip().upper()
    if perg=='N':
        break
print(pessoas)
print(f'A) Foram cadastradas {len(pessoas)} pessoas.')
print(f'B) O maior peso foi de {mai} kg e a pessoa mais pesada é: ' ,end=' ')
for p in pessoas:#Para cada pessoa em pessoas:
    if p[1]==mai: # Se p[1]=maior
        print(f'[{p[0]}]...',end=' ') #Escreva o nome.
print(f'\nC) O menor peso foi {men} Kg. e a pessoa mais leve é: ',end=' ')
for p in pessoas:
    if p[1]==men:
        print(f'[{p[0]}]...',end=' ')
