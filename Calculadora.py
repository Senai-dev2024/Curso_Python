# calculadora
while True:
    numero_1 = input('Digite um número: ')
    numer_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    
    numeros_validos = None
    numero_1_float = 0
    numer_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numer_2_float = float(numer_2)
        numeros_validos = True

    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('operador inválido.')

    if len(operador)>1:
        print('Digite apenas um operador.')
        continue
    print('Realizado sua conta. Confirao resutaldo abaixo:')

    if operador == '+':
        print(f'{numero_1_float} + {numer_2_float}=',numero_1_float + numer_2_float)
    elif operador == '-':
         print(numero_1_float - numer_2_float)
    elif operador == '/':
         print(numero_1_float / numer_2_float)
    elif operador == '*':
         print(numero_1_float * numer_2_float)
    else:
        print('Nunca deveria chegar aqui!')


    sair = input('Quer sair? [S]im ').lower().startswith('s')

  