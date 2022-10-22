cont=0
soma=0
n=0

while n!=999:
    n=int(input('Digite um número: '))
    if n==999:
        break
    cont=cont+1
    soma=soma+n
print(f'A quantidade de números digitados foi {cont} e a soma deles é: {soma}')
#faça um programa que leia varios numeros inteiros e só pare quando digitado 999.
# No final, informe a quantidade de numeros digitados e a soma deles