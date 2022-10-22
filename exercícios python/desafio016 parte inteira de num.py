import math
num=float(input('Digite um número: '))
print(int(num))
print('O valor digitado foi \033[1;97;46m {}\033[m e a sua porção inteira é \033[1;30;107m{} \033[m '.format(num,math.trunc(num)))


