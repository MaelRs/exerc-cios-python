# Faça um mini sistema que utilize o interactive help do Python. O usuário vai digitar
# o comando e o manual vai aparecer.Quando o usuário digitar 'FIM', o programa se encerrará.
#OBS:Use cores
from time import sleep
c=('\033[m',        #0-sem comres
   '\033[0;30;41m', #1-Vermelho
   '\033[0;30;42m', #2-Verde
   '\033[0;30;43m', #3-Amarelo
   '\033[0;30;44m', #4-Azul claro
   '\033[0;30;45m', #5-roxo
   '\033[0;30;46m', #6-Azul escuro
   '\033[0;30;47m', #7-cinza
   '\033[0;30;107m' #8-branco
   )
def ajuda(com):
    titulo(f'Acessando o manual do comando \"{com}\"',4)
    print(c[6],end='')
    help(com)
    print(c[0],end='')
    sleep(2)
def titulo(msg,cor=0):
    tam=len(msg)+4
    print(c[cor],end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0],end='')
    sleep(1)

#Programa Principal
comando=''
while True:
    titulo('SISTEMA DE AJUDA PyHELP',4)
    comando=str(input("Função ou Biblioteca : "))
    if comando.upper()=='FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!',8)
