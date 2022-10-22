#Crie um programa que leia nome, ano de nascimento e carteria de trabalho, cadastre os (com idade)
# em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também
# o ano de contratação e o salário. Calcule e acrescente, alem da idade, com quantos anos a pessoa
# vai se aposentar, considerando a idade de aposentadoria em 35 anos.
from datetime import date
dados={}
ano=date.today().year
dados['Nome:']=str(input('Nome: '))
an=int(input('Ano de nascimento: '))
dados['Ano dn:']=an
idade= ano-an
dados['Idade:']=idade
dados['CTPS']=int(input('Número da CTPS:'))
if dados['CTPS']>0:
    dados['Contratação']=int(input('Ano de contratação: '))
   # dados['Ano cont.:']=ac
    dados['Salario:']=float(input('Valor do salário: R$'))
    dados['Prev.aposent.:']=dados['Idade:']+((dados['Contratação']+35)-date.today().year)

for k,v in dados.items():
    print(f'O {k} tem o valor {v}')
