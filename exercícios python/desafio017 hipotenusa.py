from math import hypot
co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjacente: '))
h=hypot(co,ca)
print('A hipotenusa vai medir \033[1;30;107m  {:.2f}  \033[m'.format(h))