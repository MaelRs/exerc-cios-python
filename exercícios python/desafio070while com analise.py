#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# a) Qual o total gasto na compra;
# b) Quantos produtos custão mais do que R$1000,00 ;
# c) Qual é o nome do produto mais barato.
barato=' '
cpm1000=preço=soma=0
pmb=0
mp=0
while True:
    produto=str(input('Nome do produto: '))
    preço=float(input('Preço do produto: R$ '))
    pmb+=1
    soma+=preço
    if preço>1000:
        cpm1000+=1
    if pmb==1:
        menor=preço
        barato=produto
    else:
        if preço<menor:
            menor=preço
            barato=produto

    r=' '
    while r not in 'Ss':
        r=str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if r in 'Nn':
            print('{:-^40}'.format('Fim do programa'))
            print(f'O valor total da compra é {soma:.2f} O total de produtos com preço maior R$1000 é:{cpm1000} ')
            print(f'O produto mais barato é o {barato} que custa R$ {menor:.2f}')
            quit()





