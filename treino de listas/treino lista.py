num=[9,3,8,7,6,9,0,0]
#print(num)
num.insert(0,1)
#print(num)
num[2]=5
#print(num)
num.append(4)
#print(num)
if 3 in num:
    num.remove[3]
else:
    num.append(3)
 #   print('Número 3 não existia na lista e por isso foi incluido.')
#print(num)
#num.sort()
#print(num)
#if 2 in num:
    #num.remove(2)
  #  print('Número 2 foi removido da lista!')
#else:
 #   print('Número 2 nao localizado!')
print(num)
maior=max(num)
menor=min(num)
#print(min(num))
print(f'O maior valor encontrado foi o número {maior} na(s) posição(ões)',end=' ')
for p, v in enumerate(num):
    if v == maior:
        print(f'{p}...', end=' ')
print(f'\nO menor valor digitado foi {menor} encontrado na(s) posição(ões) ', end=' ')
    #print(f'No número {v} foi encontrado na posição {p}')
for p,v in enumerate(num):
    if v==menor:
        print(f'{p}...',end=' ')
num.insert(11,30)
print(num)
