#trabajo_practico_5_listas-DiegoCarrizo
titulo = '''
trabajo_practico_5_listas-DiegoCarrizo
'''
print(titulo)

#1
print('ejercicio 1')
lista_multiplos = list(range(4,101,4))
print('la lista generada es: ')
print(lista_multiplos)

#2
print('ejercicio 2')
print('voy a crear una lista de cinco elementos')
lista_cinco = ['nave', 'caballo', 1, True, False]
print(lista_cinco)
print('el penultimo elemento es [-2]')
print(lista_cinco[-2])

#3
print('ejercicio 3')
print('voy a crear una lista vacia ')
lista_vacia = []
print(lista_vacia)
print('voy a agregar tres palabras con append')
lista_vacia.append('uno')
lista_vacia.append('dos')
lista_vacia.append('tres')
print(lista_vacia)

#4
print('ejercicio 4')
print('dada la lista animales')
animales = ['perro', 'gato', 'conejo', 'pez']
print(animales)
print('reemplazar el segundo elemento con loro')
print('y reemplazar el ultimo elemento con oso')
animales[1] = 'loro' 
animales[-1] = 'oso'
print(animales)

#5
print('ejercicio 5')
numeros = [8,15,3,22,7]
print('dado la lista numeros')
print(numeros)
numeros.remove(max(numeros))
print('este programa obtiene el numero de mayor valor con la funcion max')
print('y luego lo elimina de la lista con el metodo remove')
print(numeros)

#6
print('ejercicio 6')
print('voy a crear una lista con los numeros del 10 al 30 incluidos con salto de 5 ')
lista_creada = list(range(10,31,5))
print(lista_creada)
print('ahora voy a mostrar los dos primeros elementos')
print(lista_creada[0:2])

#7
print('ejercicio 7')
print('dada la lista autos')
autos = ['sedan','polo','suran','gol']
print(autos)
print('reemplazar los dos elementos del medio')
autos[1] = 'ANULADO'
autos[2] = False
print(autos)

#8
print('ejercicio 8')
print('lista vacia llamada dobles')
dobles = []
print(dobles)
print('agrego el doble de 5 , 10, 15')
dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)
print(dobles)

#9
print('ejercicio 9')
print('dada la lista compras')
compras = [
    ['pan','leche'],
    ['arroz','fideo','salsa'],
    ['agua']
    ]
print(compras)
print('a-agregar jugo al tercer cliente')
compras[2].append('jugo')
print(compras)
print('b-reemplazar fideos por tallarines en el segundo cliente')
compras[1][1]='tallarines'
print(compras)
print('c-eliminar pan del primer cliente')
compras[0].remove('pan')
print(compras)


#10
print('ejercicio 10')
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print('elaborar una lista anidada segun se indica')
print(lista_anidada)