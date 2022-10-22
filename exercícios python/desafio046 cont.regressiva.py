# contagem regressiva para estouro de fogos de artifício de 10 até 0 com pausa de 1 segundo entre eles
from time import sleep
from emoji import emojize
for c in range(10,0-1,-1):
    sleep(1)
    print(c)
print('FOGO!!')