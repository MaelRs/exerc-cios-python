#faça um programa que leia 5 valores numericos e guarde os em uma lista.
#No final mostre qual foi o maior e o menor valor digitado e suas respectivas posiçoes na lista.
valores=list()
for c in range (0,5):
    valores.append(int(input(f'Digite o {c}° valor: ')))
print(f'Os valores digitados para a lista são : {valores}')
maior=max(valores)
menor=min(valores)
print(f'O maior valor digitado foi: {max(valores)} e foi localizado na(s) posição(ões) ',end=' ')
for i, v in enumerate(valores):
    if v==maior:
        print(f'{i}...',end=' ')
print()
print(f'O menor valor digitado foi: {min(valores)} e foi localizado na(s) posição(ões) ',end=' ')
for i, v in enumerate(valores):
    if v==menor:
        print(f'{i}...',end=' ')
print()

