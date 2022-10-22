
print('-='*20)
print('Analisador de triângulos')
# Desenvolva um programa que leia o comprimento de tres retas
# e diga ao usuário se elas podem ou não formar um triangulo.
print('-='*20)
r1=float(input('Digite o comprimento da reta 1: '))
r2=float(input('Digite o comprimento da reta 2: '))
r3=float(input('Digite o comprimento da reta 3: '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os segmentos de retas informados PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os segmentos de reta informados NÃO PODEM FORMAR UM TRIÂNGULO!')