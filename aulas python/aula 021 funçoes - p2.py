def contador(i, f, p):
    """
    =>Faz uma contagem e mostra na tela.
    :param i: inicio da contagem,
    :param f: fim ada contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c=1
    while c<=f:
        print(f'{c}',end=' ')
        c+=p
    print('FIM!')

    help(contador)

def somar(a=0,b=0,c=0):
    s=a+b+c
    #print(f'A soma vale {s}.')
    return s
#contador(0,100,10)

r1=somar(3,2,5)
r2=somar(2,2)
r3=somar(6)
print(f'Os resultados foram: {r1},{r2} e {r3} ')