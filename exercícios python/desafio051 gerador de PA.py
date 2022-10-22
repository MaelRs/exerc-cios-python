#Desenvolva um programa que leia o primeiro termo e a razão de uma pA. no final mostre os 10 primeiros
# termos dessa progressão.
pt=int(input('Primeiro termo: '))
r=int(input('Digite a razão: '))
décimo=pt+(10-1)*r
for c in range (pt,décimo+r,r): #primeiro elemento é o número "1" e a Razão é o n°: "10".
    print('{}'.format(c),end=' -> ')
print('ACABOU!!')