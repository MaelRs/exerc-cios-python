# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from time import sleep
def linha():
    print('-'*40)


def titulo(msg):
    print(msg.center(40))


def arquivo(nome=0, idade=0):
    titulo('CADASTRADOS')
    print('nome','\t idade')


#dados=[]
#arquivo={}

while True:
    linha()
    titulo('MENU PRINCIPAL')
    linha()
    print('\033[33m1-\033[m\t\033[34mVer pessoas cadastradas \n\033[33m2-\033[m\t\033[34mCadastrar nova Pessoa \n\033[33m3-\033[m\t\033[34mSair do Sistema\033[m')
    linha()
    opção=int(input('Digite um comando do MENU: '))
    if opção==1:
        arquivo()
    if opção==2:
        #arquivo['nome']=str(input('Nome:'))
        #arquivo['idade']=int(input('Idade: '))
        linha()
        titulo('Opção 2')
        linha()
        print(arquivo)

    if opção==3:
        print('Finalizando...',end=' ')
        sleep(1)
        print('Volte',end=' ')
        sleep(1)
        print('Sempre!')
        sleep(1)
        linha()
        break
    #else:
        #print('\033[31mErro!! Digite uma opção válida!\033[m')


