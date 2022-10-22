from random import choice
a1=input('Nome do aluno 1: ')
a2=input('Nome do aluno 2: ')
a3=input('Nome do aluno 3: ')
a4=input('Nome do aluno 4: ')
lista = [a1,a2,a3,a4]
s=choice(lista)
print('O aluno escolhido para apagar o quadro é: \033[1;30;107m {} \033[m '.format(s))
