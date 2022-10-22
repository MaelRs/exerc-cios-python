#Faça um programa que leia o sexo de uma pessoa mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado peça a digitação novamente.

#while r=='M':
sexo=str(input(' Informe seu Sexo:[M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo=str(input('Opção inválida! digite novamente:[M/F]  ')).strip().upper()[0]
print('Sexo registrado com sucesso!' )