# Desenvolva um programa que leia 4 valores pelo teclado e no final mostre:
# A) quantas vezes apareceu o valor 9,
# B) em que posição foi digitado o primeiro valor 3 ,
# C) Quais foram os números pares.
num=(int(input('Digite um Número: ')),int(input('Digite um Número: ')),int(input('Digite um Número: ')),
    int(input('Digite um Número: ')))

print(f'Você digitou os valores :{num}.')
print(f'a) O número 09 aparece {num.count(9)} vezes .')
if 3 in num:
    print(f'b) O número 3 foi digitado na {num.index(3)+1}ª posição .')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'c) Os números pares digitados foram:' ,end='')
for n in num:
    if n%2==0:
        print(n,end='-')
    #else:
        #print('d) Não houve digitação de nenhum número PAR.')
