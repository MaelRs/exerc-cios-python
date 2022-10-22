#Escreva um codigo que leia um número e informe seu antecessor e seu sucessor.
print('-='*20,'\033[1;30;42m Teste de Número \033[m','-='*20)
n1=int(input('Digite um numero: '))
print('O Antecessor de {} é: \033[1;30;42m{}\033[m'.format(n1,n1-1))
print('O Sucessor de {} é: \033[1;35;40m{}\033[m '.format(n1, n1+1))
