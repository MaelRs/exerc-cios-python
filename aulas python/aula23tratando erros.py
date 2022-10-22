try:
    a=int(input('Numerador: '))
    b=int(input('Denomiador: '))
    r=a/b
except (ValueError,TypeError):
    print('Problema relacionado ao tipo de dado digitado')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu nao informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado da operação {a}/{b} é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado.')