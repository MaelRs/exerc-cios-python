#Refaça o desafio 51, lendo o primeiro termo da PA. mostrando os 10 primeiros termos
# utilizando a estrutura while.
print('=-='*10)
print(' \033[1;30;42m!      GERADOR DE P.A      !\033[m')
print('=-='*10)
n=int(input('primeiro termo:'))
r=int(input('Digite a razão: '))
termo=n
ct=1
while ct<=10:
    print('{} -'.format(termo),end=' ')
    termo=termo+r
    ct=ct+1
print('FIM!')



