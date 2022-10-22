vc=float(input('Qual o valor da casa? R$ '))
vs=float(input('Qual o valor do salário do comprador? R$ '))
qa=float(input('Em quantos anos pretende financiar? '))
qp=(qa*12)
print('A quantidade de prestações a serem pagas será:{:.2f} '.format(qp))
vp=(vc/qp)
print('O valor da prestaçao será: R$ {:.2f}'.format(vp))
if vp>vs*30/100:
    print('\033[1:97:41m LAMENTO! Seu Financiamento foi negado.\033[m')
else:
    print('\033[1:30:47mPARABENS!! Você conquistou sua casa própria! \033[m')

