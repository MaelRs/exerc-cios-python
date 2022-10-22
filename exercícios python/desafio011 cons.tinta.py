print('\033[1;30;107m CALCULADORA DE CONSUMO DE TINTA \033[m')
l=float(input('Largura da parede:  '))
a=float(input('Altura da parede: '))
at= l * a
qt= at / 2
print('Sua parede mede \033[1;30;107m{}m por {}m \033[m e tem uma area total de \033[1;31;40m {}m² \033[m.'.format(l,a,at))
print('A quantidade de tinta necessária para efetuar a pintura de toda a área de {}m² é de \033[1;32;40m {} litros de tinta \033[m '.format(at,qt))
