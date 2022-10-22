#Crie um programa que tenha uma função fatorial() que receba dois parametros:
# o primeiro que indique o número a calcular e o outro, chamado SHOW que será um valor logico(opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(n,show=False):
    f=1
    for c in range(n,0,-1):
        if show:   #Se for mostrar cálculo.
            print(f'{c}',end='')   #Imprima o (C) do contador, e coloque o end='' para não saltar linha
            if c>1:                # se o C for maior do que 1,
                print('x',end='')  # imprima o 'X' entre um resultado e outro
            else:
                print('=',end='')  # Senão imprima o '=' entre um resultado e outro
        f*=c
    return f


print(fatorial(2,show=True))
print(fatorial(8,show=True))
#Solução
#def fatorial(n, show=False):
    #'''
   # ->Calcula o fatorial de um número.
    #:param n:É o numero a ser calculado e indica o início da contagem no laço for
    #:param show:(Opcional) Mostrar ou não a conta
    #:return: Mostra o valor do fatorial de um número.
    #'''
   # f=1
 #   for c in range(n,0,-1):
 #       if show:
 #           print(f'{c}',end='')
 #           if c>1:
 #               print('x',end='')
 #           else:
 #               print('=',end='')
 #       f*=c
 #   return f



#print(fatorial(5,show=True))
#help(fatorial)
#'''