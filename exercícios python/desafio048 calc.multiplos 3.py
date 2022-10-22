#faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que estão
#no intervalo entre 1 e 500.
soma=0
cont=0
for c in range(1,501,2):
    if c % 3==0:
        soma+=c #é o mesmo que soma=soma+c
        cont+=1 #é o mesmo que cont=cont+1
print('A Soma de todos os {} números solicitados é: {}'.format(cont,soma))
print('FIM!!')