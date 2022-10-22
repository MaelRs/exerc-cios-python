#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler quantidade de gols feitos e cada partida.
# No final, tudo isso será guardado em um dicionário incluindo o total de gols feitos durante o campeonato.
jogador={}
partidas=[]
jogador['nome']=str(input('Nome do jogador:  '))
tot=int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))
for c in range(0,tot):
    partidas.append(int(input(f'Quantos Gols feitos na {c+1}ª partida: ')))
jogador['Gols']=partidas.copy()
jogador['total']=sum(partidas)

print(jogador)

print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["Gols"])} partidas.')
for i,v in enumerate(partidas):
    print(f'=> Na {i+1}ª partida o {jogador["nome"]} fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')


