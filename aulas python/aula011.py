nome='Ismael'
print('Olá \033[1;34mIsmael\033[m Seja \033[1;30;42mBEM VINDO AO TREINAMENTO DE PYTHON!\033[m ')
print('Olá!Muito prazer em te conhecer {}{}{}!'.format('\033[4;34m',nome,'\033[m'))

print('\033[1;30;42mOlá Mundo!!\033[m')
cores={'limpa':'\033[m',
       'azul':'\033[34m',
       'amarelo':'\033[33m',
       'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer {}{}{}!!!'.format(cores['pretoebranco'],nome,cores['limpa']))