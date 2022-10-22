def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: Favor digitar um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('O usuário optou pela não inserção dos dados.')
            continue
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n=float(input(msg))
        except(ValueError, TypeError):
            print('\033[1;31mERRO: Favor digitar um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n