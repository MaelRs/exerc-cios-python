from random import shuffle
n1=input('Aluno 1: ')
n2=input('Aluno 2: ')
n3=input('Aluno 3: ')
n4=input('Aluno 4: ')
n5=input('Aluno 5: ')
lista=[n1,n2,n3,n4,n5]
shuffle(lista)
print('A ordem determinada é:')
print('\033[1;97;40m',lista,'\033[m')
