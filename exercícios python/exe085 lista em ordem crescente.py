# Crie um programa onde o usuário possa digitar sete valores numericos e cadastre-os em uma
# lista unica que mantenha separados os valores pares e impares. No final,
# mostre os valores pares e impares em ordem crescente.
valores=[[],[]]
pares=[]
impares=[]
lu=[pares[:],impares[:]]
for c in range (0,7):
    n=int(input(f'Digite o {c}º número:  '))
    if n%2==0:
        valores[0].append(n)
       # pares.append(n)
    else:
        valores[1].append(n)
        #impares.append(n)
valores[0].sort()
valores[1].sort()
#pares.sort()
print(f'A lista sequencial de números pares é {valores[0]}.')
#impares.sort()
print(f'A lista sequencial de números impares é {valores[1]}.')
#lu=[pares,impares]
print(f'A lista unica conforme solicitado é: {valores}')
