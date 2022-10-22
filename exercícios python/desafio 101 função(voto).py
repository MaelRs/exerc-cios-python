#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado,
# opcional ou obrigatorio nas eleições.
from datetime import date
def voto(num):
    if n<16:
        print(f'Com {n} anos de idade Você ainda não tem direito ao Voto.')
    elif 16<=n<18 or n>65:
        print(f'Com {n} anos de idade Seu voto é OPCIONAL!')
    else:
        print(f'Com {n} anos de idade Seu Voto é OBRIGATÓRIO!')


an=int(input('Digite seu ano de nascimento: '))
ano=date.today().year
n=ano-an
voto(n)
#soluçao
'''def voto(ano):
    from datetime import date
    atual=date.today().year
    idade=atual-ano
    if idade<16:
        return f'com {idade} anos: NÃO VOTA.'
    elif 16<=idade<18 or idade>65:
        return f'Com a {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com a {idade} anos: VOTO OBRIGATÓRIO.'

print(voto(2004))'''

