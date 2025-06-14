#TrabajoPractico Recursividad Diego Carrizo

#funciones
#ejercicio1
def factorial(n):
    if n == 0: #caso base factorial de 0
        return 1
    else:
        return n * factorial(n-1) #paso recursivo

#ejercicio2
def fibonacci(n):
    if n == 0 or n == 1: #caso base
        return n
    else:#paso recursivo
        return fibonacci(n - 1) + fibonacci(n - 2)

#ejercicio3
def potencia(n, m):
    # Caso base: cualquier número elevado a 0 es 1
    if m == 0:
        return 1
    # Caso recursivo: n^m = n * n^(m-1)
    else:
        return n * potencia(n, m - 1)

#ejercicio4
def decimal_a_binario(n):
    if n == 0:
        return "0"  # Caso base para 0
    elif n == 1:
        return "1"  # Caso base para 1
    else:
        return decimal_a_binario(n // 2) + str(n % 2) #concatena el ultimo resuelto es es msb

#ejercicio5
def es_palindromo(palabra):
    # Casos base
    if len(palabra) <= 1:
        return True
    # Comparar primer y último carácter
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva con la palabra sin los extremos
    return es_palindromo(palabra[1:-1])    
    
#ejercicio6
def suma_digitos(n):
    if n < 10:#caso base 
        return n
    return n % 10 + suma_digitos(n // 10) #recursion - con % obtengo digito de la derecha; con // elimino la unidad el de la

#ejercicio7
def contar_bloques(n): #recibe el nivel base de ladrillos
    if n == 1: #caso base  es la parte de arriba con un solo ladrillo
        return 1
    return n + contar_bloques(n - 1) #recursividad - va contando desde la base y el nivel que le sigue para arriba

#ejercicio8
def contar_digito(numero, digito):
    if numero < 10: #caso base
        if numero == digito:
            return 1 #coincidencia
        else:
            return 0 #digito no coincide
    
    ultimo_digito = numero % 10  #analizo el ultimo digito
    if ultimo_digito == digito:
        return 1 + contar_digito(numero//10, digito)
    else:
        return 0 + contar_digito(numero//10, digito)
    


#programa principal

titulo = '''
##################################
Trabajo Practico de Recursividad
Alumno: Diego Matias Carrizo
##################################
'''
print(titulo)

#ejercicio1
print('\nejercicio 1')
ingreso1 = int(input('Ingrese un numero para mostrar el factorial de todos los comprendidos entre 1 y ese: '))
for i in range(1,ingreso1 + 1):
    print(f'factorial de {i}: {factorial(i)}')

#ejercicio2
print('\nejercicio 2')
ingreso2 = int(input('Ingrese un numero para indicar la posicion de la serie fibonacci a mostrar: '))
print(f'Valor de la serie fibonacci en posicion {ingreso2}: {fibonacci(ingreso2)}')
print('ahora muestro la serie completa:')
for i in range(ingreso2 + 1):
    print(f'{fibonacci(i)}, ', end='')


#ejercicio3
print('\nejercicio 3')
base = int(input('Ingrese base n: '))
exponente = int(input('Ingrese exponente m: '))
print(potencia(base, exponente))

#ejercicio4
print('\nejercicio 4')
decimal = -1
while decimal < 0:
    decimal = int(input('Ingrese un decimal positivo para convertir a binario: '))
binario = decimal_a_binario(decimal)
print(f'El decimal {decimal} en binario es: {binario}')

#ejercicio5
print('\nejercicio 5')
palabra = input('ingrese una palabra para analizar si es palindromo: ')
respuesta = es_palindromo(palabra)
if respuesta:
    print(f'la palabra {palabra} Si es palindromo.')
else:
    print(f'la palabra {palabra} No es palindromo.')

#ejercicio6
print('\nejercicio 6')
numero = int(input('Ingrese un entero positivo para sumar sus digitos: '))
print(f'Dado el numero {numero} la suma de sus digitos da: {suma_digitos(numero)}')


#ejercicio7
print('\nejercicio 7')
ladrillos_base = int(input('Ingrese la cantidad de ladrillos que tiene la base de la piramide: '))
cantidad_ladrillos = contar_bloques(ladrillos_base)
print(f'Para una piramide con base de {ladrillos_base} ladrillos se emplearan un total de {cantidad_ladrillos} ladrillos.')

#ejercicio8
print('\nejercicio 8')
digito = 11
while (0 > digito or digito > 9):
    digito = int(input('Ingrese un digito del 0 al 9: '))

numero = int(input('Ingrese un entero para contar la presencia del digito: '))
respuesta = contar_digito(numero, digito)
print(f'El digito {digito} se encuentra {respuesta} veces en el numero {numero}.')

print('\nFin del tp de recursividad de Diego Carrizo.')