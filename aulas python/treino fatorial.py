def fatorial(numero):
    fat=1
    for c in range (numero,0,-1):
        fat*=c
        if(c!=1):
            print(c,' x ',end="")
        else:
            print(c,' = ',end="")
    print(fat)


numero=int(input('Digite um número: '))
fatorial(numero)
