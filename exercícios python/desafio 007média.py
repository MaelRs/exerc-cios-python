nota1=float(input('Nota 1:  '))
nota2=float(input('Nota 2:  '))
m=((nota1+nota2)/2)
print('A média entre {:.1f} e {:.1f} é: {:.1f} '.format(nota1,nota2,m))
# O trecho abaixo é complementar e não faz parte da atividade.
if m>=60:
    print('\033[1;30;107m Parabéns!\033[m Você foi aprovado.')
else:
    print('\033[1;31;40m LAMENTO!!\033[m Você foi reprovado! Boa sorte da próxima vez.')