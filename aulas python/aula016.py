#tuplas
#lanche=('hamburguer','suco','Pizza','Pudim','batata frita')
#print(len(lanche))
#for cont in range (0,len(lanche)):
    #print(cont)
 #   print(f'Eu vou comer {lanche[cont]} na posição {cont}')
#for pos,comida in enumerate (lanche):
    #print(f'Eu vou comer {comida} na posição {pos}')
#for comida in lanche:
    #print(f'Eu vou comer {comida}!!')
#print('Comi pra caramba!')
#print (lanche[-2])
#print(sorted(lanche))
a=(2,5,4)
b=(5,8,1,2)
c=b+a
#print(c)
#print(len(c))     #Retorna o tamanho da variável "c".
#print(c.count(5)) #retorna a quantidade de números 5 contida na váriavel 'C'.
#print(c.index(8)) #indica a posição em que o número "8" está na variável 'C'.

#pessoa=('Ismael', 37, 'M', 86)
#print(len(pessoa))
#del(pessoa)
#print(pessoa)

alf=('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
letra=str(input('Digite uma Letra: ')).strip().upper()
pos=1

lista=[]
#print(alf.index(letra))
#print(alf.rfind(letra))
'''for pos, char in enumerate (alf):
    if char==letra:
        lista.append(pos+1)
print(lista)'''
for pos,char in enumerate(alf):
    if letra==char:
        print(pos+1)

#print([pos+1 for pos, char in enumerate(letra) if char == letra])



