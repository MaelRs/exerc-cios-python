distancia = float(input('Digite a distancia em metros: '))
c=distancia*100
mm=c*10
dm=mm*10
km=distancia/1000

print('A distancia informada de \033[30;107m{}\033[m metro(s) equivale a: \033[1;33;40m{} cm \033[m, \033[1;32;40m{} mm\033[m, \033[1;33;40m{} dm\033[m e \033[1;34;40m{} km\033[m'.format(distancia,c,mm,dm,km))
