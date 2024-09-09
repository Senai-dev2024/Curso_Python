nome = 'Adriano Anacleto'
altura = 1.79
peso = 95
imc = peso/(altura*altura)   # IMC = peso/(altura x altura)
# f f-strings
linha_1 = f'{nome}, Tem {altura:.2f},de altura'
linha_2 = f'Pesa {peso:.2f} quilos e seu IMC é {imc:.2f}'
print(nome, 'Tem', altura,'de altura')
print('Pesa', peso,  'quilos e seu IMC é',imc) 
print(linha_1)
print(linha_2)

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))

nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))

nome = "Luiz"
idade = 23
formato = f'{nome} tem {idade:.2f} anos'

numero_1 = 10
numero_2 = 20
resultado = numero_1 * numero_2
print(resultado)

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor=} é maior ou igual'
    f'ao que {segundo_valor=}')
else:
    print(f'{segundo_valor=} é maior'
    f'do que {primeiro_valor}')


