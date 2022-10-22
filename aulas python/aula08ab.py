import math
n0=int(input('Digite um número: '))
raiz=math.sqrt(n0)
s=n0+1, n0+2, n0+3, n0+4
m=n0*1, n0*2, n0*3, n0*4
d=n0/2, n0/4, n0/6, n0/8
print('A raiz quadrada de {} é: {:.2f}'.format(n0,raiz))
print('A soma de {} é: {}, a multiplicação é: {} e a divisão é: {}'.format(n0,s,m,d))
print(type(n0))
