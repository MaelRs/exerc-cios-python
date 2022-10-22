print('{:=^40}'.format('LOJAS GUANABARA'))
print('''FORMAS DE PAGAMENTO
[1] À vista dinheiro ou cheque
[2] À vista Cartão
[3] 2x no cartão
[4] 3x ou mais no cartão ''')
p=float(input('Digite o valor do produto: R$ '))
opção=int(input('Digite sua opção de pagamento: '))

if opção==1:
    pv = p - (p * 10 / 100)
    print('Para pagamento a vista em dinheiro ou cheque o valor do produto terá 10% de desconto e sairá por R$ {:.2f}'.format(pv))
elif opção==2:
    pvc=p-(p*5/100)
    print('Para pagamento a vista no cartão, o valor do produto terá 5% de desconto e sairá a R${:.2f}'.format(pvc))
elif opção == 3:
    print('Para pagamento em até 2 vezes no cartão, o produto sairá pelo preço normal que é R${:.2f}'.format(p))
elif opção==4:
    pdc=p+(p*20/100)
    print('Para pagamento parcelado em 3 vezes ou mais no cartão será aplicado uma taxa de juro de 20% e o preço será: R${:.2f}'.format(pdc))
else:
    print('Opção inválida!! Tente novamente.')