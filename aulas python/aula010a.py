np=60
n1=float(input('Digite a nota 1: '))
n2=float(input('Digite a nota 2: '))
m=(n1+n2)/2
print('A sua média foi {}. '.format(m))
if m>=60:
    print('Parabens,Você foi aprovado!')
else:
    print('Lamento!Você foi reprovado! Boa sorte da Proxima vez!')

print('Parabens!'if m>=60 else 'Estude Mais!')
