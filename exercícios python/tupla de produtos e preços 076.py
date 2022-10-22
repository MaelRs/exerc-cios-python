#Crie um programa com uma tupla única com nomes de produtos e seus respectivos preços. Na sequencia.
#No final mostre uma listagem de preços, organizando os dados em forma tabular.

produtos=(('Feijão',7.89,'Arroz',25.98,'Açucar',16.98,'Macarrão',5.63,'Oleo de soja',8.49,'Azeite',32.55))
print('=='*30)
print('\033[1;30;107m LISTA DE PRODUTOS \033[m')
print('=='*30)
for pos in range(0,len(produtos)):
    if pos%2==0:
        print(f'{produtos[pos]:.<50}',end='') #Alinhamento a esquerda em 50 caracteres separados por "."
    else:
        print(f'R${produtos[pos]:>8.2f}')  #Alinhamento à direita com 7 caracteres e duas casas decimais apos a virgula
print('=='*30)