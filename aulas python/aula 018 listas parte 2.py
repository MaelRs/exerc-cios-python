dados=['Pedro',25]
pessoas=[]
pessoas.append(dados[:]) #Para fazer uma cópia dos dados de uma lista para outra basta usar a função append(xx[:])
print(pessoas)
pessoas=[['Pedro',25],['Maria',19],['João',32]]
print(pessoas)
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
