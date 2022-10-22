#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre os em uma lista.
# Caso o número já esteja na lista, ele não será adicionado. No final, serão exibidos todos
# os valores unicos digitados em ordem crescente.
lista=[]
while True:
    n=(int(input('Digite um número:')))
    if n in lista:
        print('O valor não pode ser inserido pois já se encontra na lista')
    else:
        lista.append(n)
        print('Valor inserido na lista com sucesso')
    pergunta = ' '
    while pergunta not in 'SsNn':
        pergunta=(str(input('Deseja Continuar? [S/N]: '))).strip().upper()
    if pergunta=='N':
        break
print(f'Você digitou os valores {lista}.')
lista.sort()
print(f'Os valores de forma ordenada são:{lista}')