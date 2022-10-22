carro=0
moto=0
voto=[]
while True:
    print('Escolha seu voto'
          '\n[1]- Carro'
          '\n[2]- Moto'
          '\n[0]- Sair'
          )
    opção=int(input('O que você escolhe:'))

    if opção==1:
        carro+=1
    if opção==2:
        moto+=1
    if opção==0:
        break

print(f'O total da votação para Carro foi de {carro} votos \n e para Motos foi de {moto} votos')