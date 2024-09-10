frase = 'Adriano Anaacleto'
i = 0

qdt_mais_vezes = 0
letra_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
    qdt_mais_Atual = frase.count(letra_atual)
    
    if qdt_mais_vezes <= qdt_mais_Atual:
        qdt_mais_vezes = qdt_mais_Atual
        letra_mais_vezes = letra_atual
    i += 1
    
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_mais_vezes}" que apareceu '
    f'{qdt_mais_vezes} x'
)