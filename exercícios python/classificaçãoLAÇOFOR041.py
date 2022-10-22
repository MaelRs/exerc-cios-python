from datetime import date
an=int(input('Digite o ano de Nascimento: '))
ano=date.today().year
id=ano-an
print(id)
if id<=9:
    print('A categoria de classificação para a idade de {} anos é MIRIM!!'.format(id))
elif id<=14:
    print('A categoria de classificação para a idade de {} anos é INFANTIL!!'.format(id))
elif id<=19:
    print('A categoria classificada para a idade de {} anos é: JUNIOR!!'.format(id))
elif id<=25:
    print('A categoria de classificação para a idade entre 19 e 25 anos é:SENIOR !')
elif id>25:
    print('A categoria de classificação para idade acima de 25 anos é: MASTER!!')