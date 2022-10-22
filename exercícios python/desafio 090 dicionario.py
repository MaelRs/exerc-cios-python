#faça um programa que leia o nome e média de (1)um aluno e informe se ele
# está aprovado ou reprovado considerando a média de aprovação como nota 7, guardando também a situação
# em um dicionário. No final mostre o conteudo da estrutura na tela.
ficha={}
boletim=[]

ficha['nome']=str(input('Nome: '))
ficha['media']=float(input(f'Média de {ficha["nome"]} foi: '))
boletim.append(ficha.copy())

if ficha['media']>=7:
    ficha['Situação']= 'APROVADO!'
elif 5<=ficha['media']<7:
    ficha['Situação']='EM RECUPERAÇÃO'
elif ficha['media']<5:
    ficha['Situação']='REPROVADO'
for k,v in ficha.items():
    print(f'{k} é igual a {v}.')
