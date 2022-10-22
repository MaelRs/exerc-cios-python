c=str(input('Em que Cidade vc nasceu? ')).strip().title()
print('o Nome da Cidade começa com Santo? ','\033[1;97;40m', c[:5]=='Santo','\033[m')