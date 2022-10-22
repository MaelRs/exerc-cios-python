from datetime import date
dn=(int(input('Qual o seu ano de nascimento? ')))
ano= date.today().year
tempo=ano-dn-18
id=ano-dn
print('Quem nasceu em {} tem {} anos no ano de {}.'.format(dn,id,ano))


if id==18:
    print('\033[1;30;41m ATENÇÃO!!! Está na hora de se alistar ao Serviço Militar Obrigatório! \033[m')
elif id<18:
    tf=18-id
    al=ano+tf
    print('Você deverá se alistar no ano de {}!'.format(al))
    print('\033[1;30;107m ATENÇÃO!! Em {} ano(s) Você deverá se alistar ao Serviço Militar Obrigatório!! \033[m'.format(tf))
elif id>18:
    tf=id-18
    al=ano-tf
    print('Você deveria ter se alistado em {}'.format(al))
    print('\033[1;37;40m Já passou em {} ano(s) do tempo do seu alistamento ao Serviço Militar Obrigatório! \033[m'.format(tf))
