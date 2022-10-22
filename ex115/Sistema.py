from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq='Cursoemvideo.txt'
if not arquivoExiste(arq):
   criarArquivo(arq)
while True:
    resp=menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa','Sair do Sistema'])
    if resp == 1:
        #Opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade= leiaint('Idade: ')
        cadastrar(arq,nome,idade)

    elif resp == 3:
        linha()
        print('Finalizando...',end=' ')
        sleep(1)
        print('Volte', end=' ')
        sleep(1)
        print('Sempre!')
        sleep(1)
        linha()
        break
    else:
        print('\033[1;30;41mERRO!! Digite uma opção válida.\033[m')
    sleep(1.5)