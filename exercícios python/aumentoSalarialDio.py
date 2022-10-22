salario = int(input('Digite o salário: '))

'''if (salario <= 600):
    percentual = 17 / 100
    novo_salario = (salario * percentual+salario)
    diferenca = novo_salario - salario
    print(f'Novo salario: {novo_salario:.2f} Reajuste ganho: {diferenca:.2f} Em percentual: {percentual:.0%}')
elif (salario<=900):
    percentual = 13 / 100
    novo_salario=(salario*percentual+salario)
    diferenca=novo_salario-salario
    print(f'Novo salario: {novo_salario:.2f} Reajuste ganho: {diferenca:.2f} Em percentual: {percentual:.0%}')

elif (salario<=1500):
    percentual = 12 / 100
    novo_salario=(salario*percentual+salario)
    diferenca=novo_salario-salario
    print(f'Novo salario: {novo_salario:.2f} Reajuste ganho: {diferenca:.2f} Em percentual: {percentual:.0%}')

elif (salario<=2000):
    percentual = 10 / 100
    novo_salario=(salario*percentual+salario)
    diferenca=novo_salario-salario
    print(f'Novo salario: {novo_salario:.2f} Reajuste ganho: {diferenca:.2f} Em percentual: {percentual:.0%}')

else:
    percentual = 5 / 100
    novo_salario=(salario*percentual+salario)
    diferenca=novo_salario-salario
    print(f'Novo salario: {novo_salario:.2f} Reajuste ganho: {diferenca:.2f} Em percentual: {percentual:.0%}')

if (salario <= 600):
    percentual = 17 / 100
    novo_salario = (salario * percentual+salario)
    diferenca = novo_salario - salario
    reajustado=f'{novo_salario:.2f}'.replace('.',',')
    reajuste=f'{diferenca:.2f}'.replace('.',',')
   # print(f'Novo salario: {reajustado} Reajuste ganho: {reajuste} Em percentual: {percentual:.0} %')
    print(f'Novo salario: {novo_salario:.2f} Reajuste ganho: {diferenca:.2f} Em percentual: {percentual:.0%}')
elif (salario<=900):
    percentual = 13 / 100
    novo_salario=(salario*percentual+salario)
    diferenca=novo_salario-salario
    reajustado=f'{novo_salario:.2f}'.replace('.',',')
    reajuste=f'{diferenca:.2f}'.replace('.',',')
    #print(f'Novo salario: {reajustado} Reajuste ganho: {reajuste} Em percentual: {percentual:.0} %')
    print(f'Novo salario: {novo_salario:.2f} Reajuste ganho: {diferenca:.2f} Em percentual: {percentual:.0%}')

elif (salario<=1500):
    percentual = 12 / 100
    novo_salario=(salario*percentual+salario)
    diferenca=novo_salario-salario
    reajustado=f'{novo_salario:.2f}'.replace('.',',')
    reajuste=f'{diferenca:.2f}'.replace('.',',')
#    print(f'Novo salario: {reajustado} Reajuste ganho: {reajuste} Em percentual: {percentual:.0%} %')
    print(f'Novo salario: {novo_salario:.2f} Reajuste ganho: {diferenca:.2f} Em percentual: {percentual:.0%}')
elif (salario<=2000):
    percentual = 10 / 100
    novo_salario=(salario*percentual+salario)
    diferenca=novo_salario-salario
    reajustado=f'{novo_salario:.2f}'.replace('.',',')
    reajuste=f'{diferenca:.2f}'.replace('.',',')
    #print(f'Novo salario: {reajustado} Reajuste ganho: {reajuste} Em percentual: {percentual:.0%} %')
    print(f'Novo salario: {novo_salario:.2f} Reajuste ganho: {diferenca:.2f} Em percentual: {percentual:.0%}')
else:
    percentual = 5 / 100
    novo_salario=(salario*percentual+salario)
    diferenca=novo_salario-salario
    reajustado=f'{novo_salario:.2f}'.replace('.',',')
    reajuste=f'{diferenca:.2f}'.replace('.',',')
    #print(f'Novo salario: {reajustado} Reajuste ganho: {reajuste} Em percentual: {percentual:.0} %')
    print(f'Novo salario: {novo_salario:.2f} Reajuste ganho: {diferenca:.2f} Em percentual: {percentual:.0%}')'''
if (salario <= 600):
    percentual = 17 / 100
    porcentagem=17
    novo_salario = (salario * percentual+salario)
    diferenca = novo_salario - salario
    reajustado=f'{novo_salario:.2f}'.replace('.',',')
    reajuste=f'{diferenca:.2f}'.replace('.',',')
   # print(f'Novo salario: {reajustado} Reajuste ganho: {reajuste} Em percentual: {percentual:.0} %')
    #print(f'Novo salario: {novo_salario:.2f} Reajuste ganho: {diferenca:.2f} Em percentual: {percentual:.0%}')
    print(f'Novo salario: {"{:.2f}".format(novo_salario)}\nReajuste ganho: {"{:.2f}".format(diferenca)}\nEm percentual: {porcentagem} %')

elif (salario<=900):
    percentual = 13 / 100
    porcentagem = 13
    novo_salario=(salario*percentual+salario)
    diferenca=novo_salario-salario
    reajustado=f'{novo_salario:.2f}'.replace('.',',')
    reajuste=f'{diferenca:.2f}'.replace('.',',')
    #print(f'Novo salario: {reajustado} Reajuste ganho: {reajuste} Em percentual: {percentual:.0} %')
    #print(f'Novo salario: {novo_salario:.2f} Reajuste ganho: {diferenca:.2f} Em percentual: {percentual:.0%}')
    print(f'Novo salario: {"{:.2f}".format(novo_salario)}\nReajuste ganho: {"{:.2f}".format(diferenca)}\nEm percentual: {porcentagem} %')
elif (salario<=1500):
    percentual = 12 / 100
    porcentagem = 12
    novo_salario=(salario*percentual+salario)
    diferenca=novo_salario-salario
    reajustado=f'{novo_salario:.2f}'.replace('.',',')
    reajuste=f'{diferenca:.2f}'.replace('.',',')
#    print(f'Novo salario: {reajustado} Reajuste ganho: {reajuste} Em percentual: {percentual:.0%} %')
    #print(f'Novo salario: {novo_salario:.2f} Reajuste ganho: {diferenca:.2f} Em percentual: {percentual:.0%}')
    print(f'Novo salario: {"{:.2f}".format(novo_salario)}\nReajuste ganho: {"{:.2f}".format(diferenca)}\nEm percentual: {porcentagem} %')
elif (salario<=2000):
    percentual = 10 / 100
    porcentagem= 10
    novo_salario=(salario*percentual+salario)
    diferenca=novo_salario-salario
    reajustado=f'{novo_salario:.2f}'.replace('.',',')
    reajuste=f'{diferenca:.2f}'.replace('.',',')
    #print(f'Novo salario: {reajustado} Reajuste ganho: {reajuste} Em percentual: {percentual:.0%} %')
    #print(f'Novo salario: {novo_salario:.2f} Reajuste ganho: {diferenca:.2f} Em percentual: {percentual:.0%}')
    print(f'Novo salario: {"{:.2f}".format(novo_salario)}\nReajuste ganho: {"{:.2f}".format(diferenca)}\nEm percentual: {porcentagem} %')
else:
    percentual = 5 / 100
    porcentagem= 5
    novo_salario=(salario*percentual+salario)
    diferenca=novo_salario-salario
    reajustado=f'{novo_salario:.2f}'.replace('.',',')
    reajuste=f'{diferenca:.2f}'.replace('.',',')
    #print(f'Novo salario: {reajustado} Reajuste ganho: {reajuste} Em percentual: {percentual:.0} %')
    print(f'Novo salario: {novo_salario:.2f} Reajuste ganho: {diferenca:.2f} Em percentual: {percentual:.0%}')
    print(f'Novo salario: {"{:.2f}".format(novo_salario)}\nReajuste ganho: {"{:.2f}".format(diferenca)}\nEm percentual: {porcentagem} %')

