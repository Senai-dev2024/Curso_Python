import re
import sys
cpf_enviado_client = '003.515.779-80'.replace('.',' ').replace(' ','').replace('-','') #replace retira os pontos, traços ou espaços

nove_digito = cpf_enviado_client[:9]
#print(nove_digito)
contador_reg1 = 10
resultado1 = 0

entrada = input('CPF [003.515.779-80]: ')
cpf_enviado_client = re.sub(r'[^0-9]', '',entrada)

entrada_Seq = entrada == entrada[0] * len(entrada)
 
if entrada_Seq:
     print('Você enviou dados sequenciais')
     sys.exit()

for digito in nove_digito:
    resultado1 += int(digito)*contador_reg1
    contador_reg1 -=1
digito1=(resultado1 * 10) % 11
digito1 = digito1 if digito1 <=9 else 0
print(digito1)


dez_digitos = nove_digito + str(digito1)

contador_reg2 = 11

resultado_dig2 = 0

for digito in dez_digitos:
    #print(int(digito)*contador_reg2)
    resultado_dig2 += int(digito)*contador_reg2
    contador_reg2 -= 1
digito2 = (resultado_dig2 * 10) % 11
digito2 = digito2 if digito2<=9 else 0
print(digito2)

cpf_gerado_calulo = f'{nove_digito}{digito1}{digito2}'
if cpf_enviado_client == cpf_gerado_calulo:
    print(f'{cpf_enviado_client} é valido')
else:
    print('CPF inválido')