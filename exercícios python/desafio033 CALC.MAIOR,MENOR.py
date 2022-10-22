# "Faça um programa que leia 3 números e mostre qual é o maio e qual é o menor"
n1 = int(input('Digite primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
menor=n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3
maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3

print('O maior número entre {},{} e {} é: {}'.format(n1, n2, n3,maior ))
print('O menor número entre {},{} e {} é: {}'.format(n1, n2, n3,menor ))
