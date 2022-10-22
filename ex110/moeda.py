def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobrar(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)  # É o mesmo que return res is formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:8.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESEUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:\t {moeda(preço)}')
    print(f'O dobro do preço:\t {dobrar(preço,True)}')
    print(f'A metade do preço:\t {metade(preço,True)}')
    print(f'Com {taxaa}% de aumento:\t {aumentar(preço,taxaa,True)}')
    print(f'Reduzindo {taxar}% temos:\t {diminuir(preço,taxar,True)}')
    print('-' * 30)

