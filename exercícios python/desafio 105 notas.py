# Crie um programa que tenha uma função notas() que recebe várias notas de alunos
# e vai retornar um dicionário com as seguintes informações
# -Quantidade de notas
# - A maior Nota
# - A menor nota
# - A média da turma
# - A situação opcional
# Adcione também a docstrings desta função.
def notas(*num,sit=False): #função notas
    """
    =>Função para analisar notas e situaçao de vários alunos.
    :param num: recebe várias notas a serem analisadas
    :param sit: valor opcional informando se deve ou nao adicionar a situação.
    :return: dicionário com várias informaçoes sobre a situação da turma.
    """
    r={}  # Este é o dicionário
    r['total']=len(num) #Aqui são os itens a serem inseridos no dicionário.
    r['menor']=min(num)
    r['maior']=max(num)
    r['media']=sum(num)/len(num)

    if sit:   #Essas são as condições para apresentação da situação.
        if r['media']>=7:
            r['situação']='BOA'
        elif r['media']>=5:
            r['situação']='RAZOAVEL'
        else:
            r['situação']='RUIM'
    return r


#Programa principal
resp=notas(1.5,5.5,9.5,10,6.5, sit=True) #linha digitada do programa principal
print(resp) #Linha para impressão da resposta
help(notas) #lina para leitura da Docstring
