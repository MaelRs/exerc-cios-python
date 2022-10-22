#Crie uma tupla com os 20 primeiros colocados do campeonato brasileiro de futebol na ordem de colocaçao.
# Depois mostre:
# a) Apenas os 5 primeiros colocados,
# B) os ultimos 4 colocados na tabela,
# c) uma lista dos times em ordem alfabética ,
# d) Em quel posição da tabela estáo o time da "Chapecoense".
print('=='*30)
print('                 TABELA DO BRASILEIRÃO       ')
print('=='*30)
tabela=('Atletico','flamengo','Palmeiras','Fortaleza','Corinthians','Bragantino','Fluminense','America MG','Atlético-GO',
        'Santos','Ceará SC','Internacional','São Paulo','Atletico-PR','Cuiabá','Juventude','Gremio',
        'Bahia','Esporte Recife','Chapecoense')
print(f'A) Os cinco primeiros colocados são:{tabela[0:5]}')
print(f'B) Os quatro ultimo colocados são: {tabela[-4:]}')
print(f'C)',sorted(tabela))
print('D) O time da Chapecoense está em, {}° lugar na tabela do campeonato'.format(tabela.index('Chapecoense')+1))
#print(tabela.index('Chapecoense'))