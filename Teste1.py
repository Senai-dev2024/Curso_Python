start = 0
end = 10
while start < end:
    start += 1
    print(start)
    
    linhas = 2
colunas = 2
 
linha = 1
while linha <= linhas:
    coluna = 1
    while coluna <= colunas:
        print(linha, coluna)
        coluna += 1
    linha += 1
    
    
texto = 'Python'
i = 0 
tamanho = len(texto)

while i < tamanho:
    print(texto[i])
    i += 1


senha_Salva = '123456'
senha_Digitada = ''
repeticoes = 0

while senha_Salva != senha_Digitada:
    senha_Digitada = input(f'sua senha ({repeticoes} x):')
    
    repeticoes += 1
print(repeticoes)
print('Aquele laço acima pode ter repetições infinitas')


texto1 = 'Pytho'

for letra in texto1:
    print(letra)
    


texo2 = 'Python'
novo_texto = ''
for letra in texo2:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)