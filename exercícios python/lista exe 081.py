# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados,
# B) A lista de valores ordenados de forma decrescente,
# C) Se o valor 5 foi digitado  e se está ou não na lista.
valores=[]
cont5=0
while True:
    n=(int(input('Digite um número: ')))
    valores.append(n)
    if n == 5:
        cont5=cont5+1
    pergunta=' '
    while pergunta not in 'SsNn':
        pergunta=str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if pergunta=='N':
        break
valores.sort(reverse=True)
print(f'a)A quantidade de números digitados foi {len(valores)} números')
print(f'b)Os números digitados em ordem decrescente são:{valores}')

if n==5:
    print(f'c) O número Cinco aparece {cont5} vezes entre os números digitados')
else:
    print('c) O número Cinco não foi encontrado dentre os números digitados')





