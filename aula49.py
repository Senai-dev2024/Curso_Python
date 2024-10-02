lista = ['Maria','Helena','Luiz']
lista.append('João')
indeces = range(len(lista))
print (indeces)
for indice in indeces:
    print(indice,lista[indice], type(lista[indice]))