#Crie um programa que elia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
frase=str(input('Digite uma frase: ')).strip().upper()
#print('Você digitou a frase: {}'.format(frase))
palavras=frase.split()
junto=''.join(palavras)
inverso=junto[::-1] #Este método dispensa o laço 'FOR'.
#inverso=''
#for letra in range(len(junto)-1,-1,-1): #este método usa o laço 'FOR'
   # inverso=inverso+junto[letra]
print('O inverso de {} é {}'.format(junto,inverso))
if inverso==junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')


