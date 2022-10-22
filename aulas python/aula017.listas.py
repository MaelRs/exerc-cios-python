num=[2,5,9,1]
#num[2]=3
num.append(7)
#num.sort(reverse=True)
num.insert(2,2)
if 5 in num:
    num.remove(5)
else:
    print('Número 4 não encontrado')
#num.pop(2)
print(num)
print(f'Essa lista contém {len(num)} elementos.')

#valores=list()
#for cont in range(0,5):
#    valores.append(int(input('Digite um Valor: ')))
#print(valores)
#for c, v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}!')
#print('Cheguei ao final da lista!')

'''a=[2,3,4,7]
b=a[:]
b[2]=8
print(f'A lista A: {a}')
print(f'A lista B: {b}')'''