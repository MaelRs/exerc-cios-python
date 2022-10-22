#Crie um programa que simule um funcionamento de um caixa eletronico. No início, pergunta ao usuario
# qual será o valor a ser sacado (n°inteiro) e o programa informará quantas cédulas de cada valor serão entregues.
#Obs: Considere que o caixa possui céduas de R$50, R$20, R$10,R$1.
print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
saque=int(input('Quanto quer sacar? R$ '))
total=saque
ced=50
totced=0
while True:
    if total>=ced:
        total-=ced
        totced+=1
    else:
        if totced>0:
            print(f' Você poderá retirar o total {totced} cédulas de R$ {ced}')
        if ced==50:
            ced=20
        elif ced==20:
             ced=10
        elif ced==10:
            ced=1
        totced=0
        if total==0:
            break
print('='*30)
print('Volte Sempre ao Banco CEV!')



while saque<9:
    céd=saque/9

c20=20
c10=10
c1=1


