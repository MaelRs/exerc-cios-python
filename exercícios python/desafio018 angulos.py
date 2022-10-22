import math
a = float(input('Digite um ângulo: '))
s=math.sin(math.radians(a))
c=math.cos(math.radians(a))
t=math.tan(math.radians(a))
print('\033[1;30;107mO Angulo de {}° tem o SENO de {:.2f}°,\nO Angulo de {}° tem o COSSENO de {:.2f}°\nO Angulo de {}° tem a tangente de {:.2f}°\033[m'.format(a,s,a,c,a,t))
