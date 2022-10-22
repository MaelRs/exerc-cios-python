n=cont=impar=par=0
soma=n
#n=int(input('Digite um número: '))
while n!=99:
    n=int(input('Digite um número: '))
    soma=soma+n
    cont+=1
    if n%2==0:
        par+=1
    else:
        impar+=1
    if n==99:
        break
print(f'Foram digitados {par} números pares e {impar} números impares.')
print(f'A quantidade de números digitados foi {cont}')
print(f'O somatório total dos números digitados é: {soma} ')
print('FIM!')