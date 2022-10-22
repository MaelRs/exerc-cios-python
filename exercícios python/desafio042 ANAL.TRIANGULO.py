#Analisador de triangulos

r1=float(input('Digite o primeiro segmento: '))
r2=float(input('Digite o segundo segmento: '))
r3=float(input('Digite o terceito segmento: '))
if r1<r3+r2 and r2<r1+r3 and r3<r1+r2:
    print('Com as medidas {},{} e {} dos segmentos apresentados, \033[1;32;107m É POSSIVEL \033[m formar um triangulo!'.format(r1,r2,r3))
    if r1==r2==r3 : #Equilátero: Todos os lados são iguais.
        print('Com as medidas de {},{} e {} dos segmentos apresentados é possivel formar um triagulo Equilátero!'.format(r1,r2,r3))
    if r1!=r2!=r3!=r1 :# Escaleno todos os lados são diferentes
        print('Com as medidas de {},{} e {} dos segmentos apresentados, é possível formar um triangulo ESCALENO'.format(r1,r2,r3))
    else:#2 lados iguais e um diferente
        print('Com as medidas de {},{} e {} dos segmentos apresentados, é possivel formar um triangulo ISÓCELES!'.format(r1,r2,r3))
else:
    print('As medidas informadas não podem formar um triangulo')