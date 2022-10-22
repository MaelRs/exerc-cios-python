#Faça um programa que tenha uma função chamada escreva(). que receba um texto como parametro
# e mostre uma mensagem com tamanho adaptável. Ex: escreva('Olá, Mundo!') e na saida ela apareça ente linhas.
def escreva(txt):
    print('-'*len(txt))
    print(txt)
    print('-'*len(txt))


escreva('Olá, Mundo!')
escreva('Constuindo um futuro melhor! Vem comigo')