#Crie um programa onde o usuário possa digitar cinco valores numericos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). no final, mostre a lista ordenada na tela.
valores=[]

for c in range(0,5):
    n=(int(input(f'Digite um numero: ')))
    if c==0 or n>len(valores):
        valores.append(n)
    else:
        pos=0
        while pos< len(valores):
            if n<=valores[pos]:
                valores.insert(pos,n)
                break
            pos+=1
print(f'Os valores digitados em ordem foram {valores} .')


