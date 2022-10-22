p=float(input('Qual é seu peso?  '))
a=float(input('Qual é a sua altura? '))
imc=p/(a**2)
print(imc)
if imc<18.5:
    print('Você está abaixo do seu peso ideal!')
elif imc<=25.0:
    print('Você está em seu peso ideal.')
elif imc<30.0:
    print('ATENÇÂO!! Você está com sobrepeso!')
elif imc<40.0:
    print('URGENTE!! Você está com obesidade!!')
elif imc>40.0:
    print('PERIGO!! Você Possui obesidade MÓRBIDA!!!!')
