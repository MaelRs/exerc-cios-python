#Escreva um código que leia um número e informe seu dobro, triplo e sua raiz quadrada.
n1= int(input('Número qualquer: '))
d = n1*2
t = n1*3
rq = n1**(1/2)

print('O dobro de \033[0;33;40m{}\033[m é: \033[0;30;107m{}\033[m,\nO seu triplo é: \033[1;30;47m{}\033[m \ne sua raiz quadrada é: \033[1;30;107m{:.2f}\033[m '.format(n1,d,t,rq))
