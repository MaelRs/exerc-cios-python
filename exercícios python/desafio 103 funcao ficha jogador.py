#faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros:
# o nome de um jogador e quantos gols ele marcou.
# O Programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
# nao tenha sido informado corretamente

def ficha(jog='<DESCONHECIDO>',gol=0): #Aqui usamos parametros opcionais onde o dado receberá o valor
    # sugerido caso o mesmo não lhe seja atribuido
    print(f'O Jogador {jog} fez {gol} gol(s) no campeonato.')


#Programa principal.
n=str(input('Nome do Jogador: '))
g=str(input('Número de gols: '))
if g.isnumeric():# Analisa se o dado inserido em "g" como 'str' é ou náo numerico.
    g=int(g)     # Caso g seja numerico ele passa a ser entendido como número 'int' de n°inteiro.
else:
    g=0  # Então se G não for numérico ele recebe valor de zero.
if n.strip()=='': # se não houver inserção de dado em 'n'
    ficha(gol=g)  # A ficha irá retornar somente com o dado inserido em 'g'.
else:
    ficha(n,g)  #Caso ambos os dados estejam inseridos, o resultado retornará a leitura de ambos.
