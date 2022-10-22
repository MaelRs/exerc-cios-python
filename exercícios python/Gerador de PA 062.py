#melhore o desafio 061 perguntando ao usuario se ele quer mostrar mais alguns termos.
# O programa se encerra quando ele diz que quer mostrar 0 termos.
print('\033[1;30;41m!     GERADOR DE PA     !\033[m')
print('=-='*15)
primeiro=int(input('Primeiro termo:'))
razão=int(input('Razão da PA: '))
termo=primeiro
cont=1
total=0
mais=10
while mais!=0:
    total=total+mais
    while cont<=total:
        print('{}'.format(termo),end=' ')
        termo=termo+razão
        cont=cont+1
    print('PAUSA')
    mais=int(input('Quer mostrar mais quantos termos?'))
print('Fim!!')
print('Progressão finalizada com {} termos mostrados.'.format(total))


