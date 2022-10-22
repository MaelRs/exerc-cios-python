#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
#Seu programa deverá ler um número pelo teclado e mostrá-lo por extenso.

cont=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze',
    'doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito,','dezenove','vinte')
pergunta='SsNn'
while True:
    num=int(input('Digite um número entre 0 e 20:'))

    #pergunta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    #while pergunta not in '|SsNn':
     #   num = int(input('Digite um número entre 0 e 20:'))
      #  print(f'Você digitou o número {cont[num]}.')

   # if pergunta=='S':
        #num = int(input('Digite um número entre 0 e 20:'))

    if 0<=num<=20 or pergunta=='N':
        break
    print('Tente novamente! ',end=' ')
print(f'Você digitou o número {cont[num]}.')
#    while pergunta!='Nn':
        #pergunta = str(input('Deseja continuar? [S/N] '))
