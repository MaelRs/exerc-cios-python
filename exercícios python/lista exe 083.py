#Crie um programa onde o usuário digite uma expressão qualquer que use parenteses.
# Seu aplicativo deverá analisar se a expressão passada está com parenteses abertos e fechados na ordem correta.
exp=input('Digite um expressão numérica: ')
pilha=[]
for simb in exp:
    if simb=='(':
        pilha.append('(')
    elif simb==')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')


