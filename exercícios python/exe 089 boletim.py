# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta,
# no final mostre um boletim contendo a média de cada um e permita que o usuário possa
# mostrar as notas de cada aluno individualmente.
ficha=[]

while True:
    nome=str(input('Nome: '))
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    media=(nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    pergunta=' '
    while pergunta not in 'SsNn':
        pergunta=str(input('Deseja Continuar? [S/N]:  ')).strip().upper()
    if pergunta=='N':
        break
print('-='*30)
print(f'{"Nº.":<4} {"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
#print(ficha)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f} ')
while True:
    print('-'*35)
    opc=int(input('Mostrar nota de qual aluno? '))
    if opc==999:
        print('FINALIZANDO!!')
        break
    if opc<=len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('\033[1:97:40m<<< VOLTE SEMPRE!: >>>\033[m')

print('Fim!!')
