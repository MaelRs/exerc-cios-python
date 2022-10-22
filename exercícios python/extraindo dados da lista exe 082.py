#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados,
# respectivamente. Ao final, mostre o conteudo das tres listas geradas.

valores=[]
pares=[]
impares=[]
while True:
    n = (int(input('Digite um número:')))
    valores.append(n)
    pergunta=' '
    while pergunta not in 'SsNn':
        pergunta=(str(input('Deseja continuar? [S/N]: '))).strip().upper()
    if pergunta in 'Nn':
        break
    if n%2==0:
        pares.append(n)
    else:
        impares.append(n)
print('=='*30)
print(f'Os números digitados foram : {valores}')
print(f'A lista de números pares é: {pares}')
print(f'A lista dos números impares é: {impares}')
print('=='*30)

