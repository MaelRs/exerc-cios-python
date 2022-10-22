#crie um programa que leia o ano de nascimento de 7 pessoas. No final,
# mostre quantas delas ainda nao atingiram a maioridade e quantas já são maiores considere a maioridade com 21 anos
from datetime import date
totmaior=0
totmenor=0
for pess in range (1,8):
    nasc=int(input('Ano de nascimento da {}ª pessoa: '.format(pess)))
    ano=date.today().year
    idade=ano-nasc
    if idade>=21:
        totmaior=totmaior+1
    else :
        totmenor=totmenor+1
print('Neste grupo temos {} pessoas MENORES DE IDADE e {} pessoas MAIORES DE IDADE.'.format(totmenor,totmaior))