#lanche=['Hamburguer','Pizza','Suco','Pudim']
#print(lanche)
#lanche[3]='picolé'
#lanche.append('Cookie') # A função append() adiciona um elemento ao final da lista.
#lanche.insert(0,'bolo') # A função insert() adiciona um elemento em qualquer posição desejada.
#print(lanche)
#del(lanche[3]) #A função del() deleta um elemento de qualquer posição desejada da lista.
#lanche.pop(3) #A função .pop() tambem serve para deletar um elemento de qualquer posição da lista.
#lanche.remove('Pizza') #A função remove, remove o elemento indicado pelo nome ou valor da str.
#print(lanche)
# Para remover um elemento da lista sem saber se ele a compõe, basta usar a situação abaixo:
#if 'Pizza' in lanche:
#    lanche.remove('Pizza')

# É possível criar uma lista a partir de uma lista já existente usando a função "list(range(4,11)
valores=list(range(1,11))
valores=[8,2,5,4,9,3,0]
valores.sort() #A função 'sort()' serve para ordenar os valores apresentados na lista
print(valores)
valores.sort(reverse=True) #A função 'reverse=True', organiza de forma reversa a apresentação dos valores da lista
print(valores)