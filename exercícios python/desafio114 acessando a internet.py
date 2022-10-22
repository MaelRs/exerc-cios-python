# Crie um código em python que testa se o site Pudim esta acessivel pelo computador usado.
import urllib
import urllib.request

try:
    site=urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[1;30;41mO Site não está acessivel no momento.\033[m')
else:
    print('Consegui acessar o Site normalmente!!')
    #print(site.read()) #este comando mostra todo detalhamento do site.