'''teste=[]
teste.append('Gustavo')
teste.append(40)
galera=[]
galera.append(teste[:])
teste[0]='Maria'
teste[1]=22
galera.append(teste[:])
print(galera)'''
#galera=[['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera)
#print(galera[0][0])
#print(galera[2][1])
#for p in galera:
    #print(p[1])
 #   print(f'{p[0]} tem {p[1]} anos de idade.')
galera=[]
dado=[]
totmaior=0
totmenor=0
for c  in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1]>=21:
        totmaior+=1
        print(f'{p[0]} é maior de idade.')
    else:
        totmenor+=1
        print(f'{p[0]} é menor de idade.')

print(f'A lista contem {totmaior} pessoas maior(es) de idade e {totmenor} pessoa(s) menor(es) de idade.')