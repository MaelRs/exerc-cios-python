#desenvolva um programa que pergunte  distancia de uma viagem em km. Calcule o preço da passagem, combrando R$0,50 por km para viagens até 200km  e R$0,45 para viagens mais longas
d=float(input('Qual a distancia a percorrer na viagem? '))
vvc=d*0.50 #valor da viagem mais curta
vvl=d*0.45 #valor da viagem mais longa
#print('O valor da viagem mais curta é: R$ {} e o da viagem mais longa é:R$ {} .'.format(vvc,vvl))
if d>200:
    print('O valor da viagem é:R$ {:.2f}. '.format(vvl))
else:
    print('O valor da viagem é: R$ {:.2f}.'.format(vvc))

if d<=200:
    preço=d*0.50
else:
    preço=d*0.45
print('O valor da viagem é:R$ {:.2f}.'.format(preço))