#for c in range(0,5):
salario=float(input('Digite o salario: '))
if (salario<=600):
    porcentagem=1.17
    novo_salario = (salario * porcentagem)
    valor = (novo_salario - salario)
    print(f'Novo salário: {novo_salario:.2f}')
    print(f'Reajuste ganho: {valor:.2f}')
    print(f'Em percentual: 17 %')
elif (salario<=900):
    porcentagem=1.13
    novo_salario = (salario * porcentagem)
    valor = (novo_salario - salario)
    print(f'Novo salário: {novo_salario:.2f}')
    print(f'Reajuste ganho: {valor:.2f}')
    print(f'Em percentual: 13 %')
elif (salario<=1500):
    porcentagem=1.12
    novo_salario = (salario * porcentagem)
    valor = (novo_salario - salario)
    print(f'Novo salário: {novo_salario:.2f}')
    print(f'Reajuste ganho: {valor:.2f}')
    print(f'Em percentual: 12 %')
elif (salario<=2000):
    porcentagem=1.10
    novo_salario = (salario * porcentagem)
    valor = (novo_salario - salario)
    print(f'Novo salário: {novo_salario:.2f}')
    print(f'Reajuste ganho: {valor:.2f}')
    print(f'Em percentual: 10 %')
else:
    porcentagem=1.05
    novo_salario = (salario * porcentagem)
    valor = (novo_salario - salario)
    print(f'Novo salário: {novo_salario:.2f}')
    print(f'Reajuste ganho: {valor:.2f}')
    print(f'Em percentual: 5 %')

'''if (salario <= 600):
    print(f'Novo salario:{(salario * 1.17):.2f}')
    print(f'Reajuste ganho:{((salario * 1.17) - salario):.2f}')
    print(f'Em percentual: 17 %')
elif (salario <= 900):
    print(f'Novo salario:{(salario * 1.13):.2f}')
    print(f'Reajuste ganho:{((salario * 1.13) - salario):.2f}')
    print(f'Em percentual: 13 %')

elif (salario <= 1500):
    print(f'Novo salario:{(salario * 1.12):.2f}')
    print(f'Reajuste ganho:{(salario * 1.12 - salario):.2f}')
    print(f'Em percentual: 12 %')
elif (salario <= 2000):
    print(f'Novo salario:{(salario * 1.10):.2f}')
    print(f'Reajuste ganho:{(salario * 1.10 - salario):.2f}')
    print(f'Em percentual: 10 %')
else:
    print(f'Novo salario:{(salario * 1.05):.2f}')
    print(f'Reajuste ganho:{(salario * 1.05 - salario):.2f}')
    print(f'Em percentual: 5 %')'''
'''if (salario<=600):
    percentual=17/100
    porcentagem=17
    novo_salario=(salario*percentual)+salario
    novoSalario=f'{novo_salario:_.2f}'
    valor=novo_salario-salario
    reajustado=novoSalario.replace('_','').replace('.',',')
    valorA=f'{valor:.2f}'
    Reajuste=valorA.replace('.',',')
    print(f'Novo salário: {reajustado} Reajuste ganho: {Reajuste} Em percentual: {porcentagem} %')
elif (salario<=900):
    percentual = 13 / 100
    porcentagem=f'percentual:.0%'
    novo_salario = (salario * percentual) + salario
    novoSalario = f'{novo_salario:_.2f}'
    valor = novo_salario - salario
    reajustado = novoSalario.replace('_', '').replace('.', ',')
    valorA = f'{valor:.2f}'
    Reajuste = valorA.replace('.', ',')
    print(f'Novo salário: {reajustado} Reajuste ganho: {Reajuste} Em percentual: {porcentagem} %')
elif (salario<=1500):
    percentual=12/100
    porcentagem=12
    novo_salario = (salario * percentual) + salario
    novoSalario = f'{novo_salario:_.2f}'
    valor = novo_salario - salario
    reajustado = novoSalario.replace('_', '').replace('.', ',')
    valorA = f'{valor:.2f}'
    Reajuste = valorA.replace('.', ',')
    print(f'Novo salário: {reajustado} Reajuste ganho: {Reajuste} Em percentual: {porcentagem} %')
elif (salario<=2000):
    percentual=10/100
    porcentagem=10
    novo_salario = (salario * percentual) + salario
    novoSalario = f'{novo_salario:_.2f}'
    valor = novo_salario - salario
    reajustado = novoSalario.replace('_', '').replace('.', ',')
    valorA = f'{valor:.2f}'
    Reajuste = valorA.replace('.', ',')
    print(f'Novo salario: {reajustado} Reajuste ganho: {Reajuste} Em percentual: {porcentagem} %')
else:
    percentual=5/100
    porcentagem=5
    novo_salario = (salario * percentual) + salario
    novoSalario = f'{novo_salario:_.2f}'
    valor = novo_salario - salario
    reajustado = novoSalario.replace('_', '').replace('.', ',')
    valorA = f'{valor:.2f}'
    Reajuste = valorA.replace('.', ',')
    print(f'Novo salário: {reajustado} Reajuste ganho: {Reajuste} Em percentual: {porcentagem} %')

if (salario<=600):
    reajuste=17/100
    novo_salario=(salario*reajuste)+salario
    novoSalario=f'{novo_salario:_.2f}'
    valor=novo_salario-salario
    novo_Salario=novoSalario.replace('_','').replace('.',',')
    valorA=f'{valor:.2f}'
    valorC=valorA.replace('.',',')
    print(f'O novo salário é {novo_Salario} reajuste ganho: {valorC} Em percentual: {reajuste:.0%}')
elif (salario<=900):
    reajuste = 13 / 100
    novo_salario = (salario * reajuste) + salario
    novoSalario = f'{novo_salario:_.2f}'
    valor = novo_salario - salario
    novo_Salario = novoSalario.replace('_', '').replace('.', ',')
    valorA = f'{valor:.2f}'
    valorC = valorA.replace('.', ',')
    print(f'O novo salário é {novo_Salario} reajuste ganho: {valorC} Em percentual: {reajuste:.0%}')
elif (salario<=1500):
    reajuste=12/100
    novo_salario = (salario * reajuste) + salario
    novoSalario = f'{novo_salario:_.2f}'
    valor = novo_salario - salario
    novo_Salario = novoSalario.replace('_', '').replace('.', ',')
    valorA = f'{valor:.2f}'
    valorC = valorA.replace('.', ',')
    print(f'O novo salário é {novo_Salario} reajuste ganho: {valorC} Em percentual: {reajuste:.0%}')
elif (salario<=2000):
    reajuste=10/100
    novo_salario = (salario * reajuste) + salario
    novoSalario = f'{novo_salario:_.2f}'
    valor = novo_salario - salario
    novo_Salario = novoSalario.replace('_', '').replace('.', ',')
    valorA = f'{valor:.2f}'
    valorC = valorA.replace('.', ',')
    print(f'O novo salário é {novo_Salario} reajuste ganho: {valorC} Em percentual: {reajuste:.0%}')
elif (salario>2000):
    reajuste=5/100
    novo_salario = (salario * reajuste) + salario
    novoSalario = f'{novo_salario:_.2f}'
    valor = novo_salario - salario
    novo_Salario = novoSalario.replace('_', '').replace('.', ',')
    valorA = f'{valor:.2f}'
    valorC = valorA.replace('.', ',')
    print(f'O novo salário é {novo_Salario} reajuste ganho: {valorC} Em percentual: {reajuste:.0%}')
else:
    print(f'O novo salário é {salario}')'''
