#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
#Para salarios superiores a R$1250,00 calcule um aumento de 10%.
#Para salários inferiores ou iguais, o aumento é de 15%.

sal=float(input('Digite o valor do salário: '))
if sal>1250.00:
    aumento= sal+(sal*10/100)
if sal<=1250.00:
    aumento= sal+(sal*15/100)
print('O valor do salario R$:{} com o aumento passa a ser de R$:{}'.format(sal,aumento))
if sal<=1250.00:
    print('\033[1;97;40mPARABENS!!\033[m Você receberá o aumento de \033[1;30;42m15%\033[m sobre o seu valor de salário!')
else:
    print('PARABÉNS!! Você receberá um aumento de 10% sobre sue salário!')