print('\033[0;97;40m ANALISADOR DE NOME \033[m')
nome=str(input('Nome completo: ')).strip().title()
print('Muito Prazer em te conhecer!')
dividir=nome.split()
#print(dividir)
print('\033[1;30;107m O seu primeiro nome é {} .'.format(dividir[0]),'\033[m')
print('O seu ultimo nome é {} .'.format(dividir[len(dividir)-1]))
x='curso de python no cursoemvideo'
print(x[5])