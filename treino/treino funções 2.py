def soma(*num):
    s=0
    for valor in num:
        s+=valor
    print(f'Somando os valores {num} temos o total de {s}')


soma(2,8,3)
soma(3,9)
soma(6,8,2,9,4)

