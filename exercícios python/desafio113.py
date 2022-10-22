#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade de digitação
# de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
from ex113.leianum import leiaint, leiafloat


num=leiaint('Digite um número inteiro: ')
n=leiafloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {num} e o número real {n}.')
