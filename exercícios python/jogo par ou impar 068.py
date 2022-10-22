#faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador
# perder, mostrando o total de vitórias consecutivas que ele conquistou.
from random import randint
print('=='*30)
print('VAMOS JOGAR PAR OU IMPAR?')
print('=='*30)
vitoria=0

jogador=int(input('Digite um valor: '))
opção=str(input('PAR ou IMPAR? [P/I]: ').strip().upper())
print('=='*30)
computador=randint(0,10)
soma=computador+jogador
if soma%2==0:
    result='PAR'
else:
    result='IMPAR'
if result=='PAR' and opção=='P':
    vitoria+=1
    print('Você Venceu!!')

elif result=='IMPAR'and opção=='I':
    vitoria+=1
    print('Você Venceu!')
else:
    print('Você perdeu!')
    quit()
print(f'Você venceu por {vitoria} vezes ')
print(f'Você jogou {jogador} e o computador jogou {computador} e a soma é:{soma}')
print(f'A soma resultou em um número {result}')

