#TP4_Estructuras_Repetitivas_Diego_Carrizo
#Alumno Diego Carrizo
titulo = '''
Tp4 Estructuras Repetitivas
Diego Carrizo
comision11 grupo2
'''
print(titulo)

#ejercicio1
for numero_impreso in range(0,101):
    print(numero_impreso)
    

#ejercicio2
numero_ingresado = int(input('Ingrese un numero: '))
valor_absoluto_numero = abs(numero_ingresado)
contador_digitos = 0

if valor_absoluto_numero == 0:
    contador_digitos = 1
else:
    while valor_absoluto_numero > 0: #metodo de division por 10
        valor_absoluto_numero = valor_absoluto_numero // 10
        contador_digitos += 1 #incrementa
print(f'El valor ingresado {numero_ingresado} contiene {contador_digitos} digitos')


#ejercicio3
sumatoria = 0
ingreso_1 = int(input('Ingrese un entero:'))
ingreso_2 = int(input('Ingrese otro entero:'))

#determino el mayor sin usar funciones especificas
if ingreso_2 == ingreso_1:
    sumatoria = 0  
elif ingreso_1 > ingreso_2:
    mayor = ingreso_1
    menor = ingreso_2
    sumatoria = 1 #valor distinto a cero
else:
    mayor = ingreso_2
    menor = ingreso_1
    sumatoria = 1 #valor distinto a cero

if sumatoria == 0:
    print(f'Los ingresos son iguales, la suma es cero.')
else:
    #cuando la sumatoria es distinta a cero
    #realizo la sumatoria sin incluir extremos
    #reseteo el contador
    sumatoria = 0
    for variable in range(menor+1, mayor):
        sumatoria += variable
    print(f'La sumatoria de los enteros comprendidos entre {menor} y {mayor} es: {sumatoria}')
    
    
#ejercicio4
ingreso = int(input('Ingrese un entero (se sale con cero): '))
suma = ingreso
while ingreso != 0:
    ingreso = int(input('Ingrese otro entero (se sale con cero): '))
    suma = suma + ingreso
print(f'La suma de los enteros ingresados es: {suma}')


#ejercicio5
import random
numero_generado = random.randint(0,9)
numero_ingresado = 10 #inicializo para ingresar al loop
contador_intentos = 0
while numero_generado != numero_ingresado:
    contador_intentos += 1
    numero_ingresado = int(input('['+str(contador_intentos)+'] Adivine el numero entre el 0 y el 9: '))
print(f'felicitaciones! El numero era el:{numero_generado}. Intentos = {contador_intentos}')


#ejercicio6
for x in range(100,-1, -1): #inicio, fin excluido, paso
    if x % 2 == 0:
        print(x)
        
#ejercicio7
acumulador_suma = 0
numero_ingresado_positivo = int(input('Ingrese un numero entero positivo (este numero no se incluira en la suma): '))
if numero_ingresado_positivo > 0:
    for x in range(0,numero_ingresado_positivo):
        acumulador_suma = acumulador_suma + x
    #imprimo resultado
    print(f'La suma de los numeros comprendidos entre el cero y el {numero_ingresado_positivo} es: {acumulador_suma}')    
        
else:
    print('El programa solo trabaja con enteros positivos.')


#ejercicio8
tamano_de_lista = 10 #poner en 100
contador_par = 0
contador_impar = 0
contador_positivo = 0
contador_negativo = 0
#procedo a cargar los 100 valores
for x in range(tamano_de_lista):
    numero_ingreso = int(input(f'Ingrese el entero ({x+1}): '))
    if numero_ingreso % 2 == 0: #par
        contador_par += 1
    else:
        contador_impar += 1
    
    if numero_ingreso > 0: #positivo
        contador_positivo += 1
    elif numero_ingreso < 0:#negativo
        contador_negativo += 1
        
print(f'pares: {contador_par}')
print(f'impares: {contador_impar}')
print(f'positivos: {contador_positivo}')
print(f'negativos: {contador_negativo}') 
    

#ejercicio9
import statistics
lista_de_cien_enteros = []
tamano_de_lista = 10
#procedo a cargar los 100 valores
for x in range(tamano_de_lista):
    numero_ingreso = int(input(f'Ingrese el entero ({x+1}): '))
    #agrego el ingreso a la lista
    lista_de_cien_enteros.append(numero_ingreso)
print('muestro la lista de numeros ingresados')
print(lista_de_cien_enteros)
print('calcula la media con la funcion mean')
media = statistics.mean(lista_de_cien_enteros)
print(f'La media de los valores ingresados es: {media}')


#ejercicio10
numero_int = int(input('Ingrese un entero distinto a cero: '))
cadena_invertida = ''
error = False #inicializo
            #al final no lo use

print('vamos a invertir los digitos convirtiendo a string y recorriendo con un for')

if numero_int == 0:
    error == True
    negativo = False

if numero_int > 0:
    negativo = False

if numero_int < 0:
    numero_int = numero_int * (-1)
    negativo = True
    
#convierto el numeroint en cadena
numero_cadena = str(numero_int)
    
for caracter in numero_cadena:
    cadena_invertida = caracter + cadena_invertida #concateno al principio
#vuelvo a reconvertir la cadena a numero
numero_int_invertido = int(cadena_invertida)    
    
if negativo == True:
    numero_int_invertido *= -1
    
print(f'El numero invertido es {numero_int_invertido}')
print('La cadena tambien se puede invertir con slicing [::-1]')
cadena_invertida_slicin = numero_cadena[::-1]
print(cadena_invertida_slicin)