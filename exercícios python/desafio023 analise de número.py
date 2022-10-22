n=int(input('Digite um número: '))
u=n//1%10
d=n//10%10
c=n//100%10
m=n//1000%10
#b=n//10000%10

print('Analisando o número: \033[1;30;107m {}\033[m'.format(n))
print('Unidade: {} '.format(u))
print('Dezenas: {} '.format(d))
print('Centenas :{} '.format(c))
print('Milhar(es) : {} '.format(m))
#print('Bilhar(es): {} ' .format(b))