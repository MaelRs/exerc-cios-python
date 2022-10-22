def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: Favor digitar um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;30;41mO usuário optou pela não inserção dos dados.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-'*tam


def cabeçalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opção = leiaint('Digite um comando do MENU: ')
    return opção



