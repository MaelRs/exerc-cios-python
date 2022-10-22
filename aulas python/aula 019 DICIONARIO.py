dados=dict()
dados={'nome':'Pedro ','idade':25}
#print(dados['nome'], end='')
#print(dados['idade'])
dados['sexo ']='M'
'''print(dados)'''
del dados['idade']
'''print(dados)'''

filme={'título':'Star Wars','ano':1977,'diretor':'George Lucas'
}
'''print(filme.values())
print(filme.keys())
print(filme.items())'''
for k, v in filme.items():
    print(f'O {k} é {v}.')

pessoas={'nome':'Gustavo','sexo':'M','idade':22}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#del pessoas['sexo'] # Para excluir um dos itens do dicionário, basta usar o del pessoas
# e indicar a chave a ser deletada
pessoas['nome']='Ismael' #O dicionário permite a alteração do item com o presente comando
pessoas['peso']=86
for k in pessoas.keys(): # se quiser mostrar as chaves usa se o laço em questão onde
    # para cada chave, em pessoas.keys, mostre a chave
    print(k)
for k in pessoas.values():# se quiser mostrar os valores usa se o laço em questão onde
    # para cada chave, em pessoas.values, mostre os valores.
    print(k)
for k,v in pessoas.items(): # se quiser mostrar os itens, usa se o laço em questão onde
    # para cada chave, em pessoas.items, mostre os itens.
    print(f'{k} = {v} .')
