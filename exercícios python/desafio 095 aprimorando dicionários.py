# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.
jogador=dict()
partidas=list()
time=[]
while True:
    jogador.clear()
    jogador['nome']=str(input('Nome do Jogador: '))
    tot=int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantidade de gols  que o {jogador["nome"]} fez na {c+1}ª partida:')))
    jogador['gols']=partidas.copy()
    jogador['total']=sum(partidas)
    time.append(jogador.copy())
    perg = ' '
    while perg not in 'SsNn':
        perg = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if perg not in 'SsNn':
            print('\033[1:30:41m ERRO! Responda apenas S ou N \033[m')
    if perg == 'N':
        break
print('-='*30)
print('cod',end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k,v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)
while True:
    busca=int(input('Mostrar dados de qual jogador:(999 para parar) '))
    if busca==999:
        break
    if busca>len(time):
        print(f'ERRO! Não existe jogador com o código {busca}.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'      No jogo {i+1} fez {g} gol(s).')
    print('-'*40)
print('<< VOLTE SEMPRE" >>')
#print('--'*30)
#print(jogador)
#for k, v in jogador.items():
 #   print(f'O {k} tem valor: {v}')
#print('--' * 30)
#print(f'O {jogador["nome"]} jogou {len(jogador["gols"])} partidas e fez {jogador["total"]} gol(s).')
#print('--'*30)
#for i,v in enumerate(partidas):
 #   print(f'=> Na {i+1}ª partida o {jogador["nome"]} fez {v} gol(s).')

#print('--' * 30)