'''

#Alumno: Diego Carrizo
#Practico 3 Estructuras Condicionales

#ejercicio1
edad = int(input('Ingrese su edad: '))
if edad > 18:
    print('Es mayor de edad.')
    
#ejercicio2
nota = int(input('Ingrese su nota: '))
if nota >= 6:
    print('Aprobado.')
else:
    print('Desaprobado')
    

#ejercicio3
ingreso = int(input('Ingrese numero: '))
if ingreso % 2 == 0:
    print('Ha ingresado un numero par.')
else:
    print('Por favor, ingrese un numero par.')
    

#ejercicio4
edad = int(input('Ingrese edad: '))
if edad < 12:
    print('Niño')
elif edad >= 12 and edad < 18:
    print('Adolescente')
elif edad >= 18 and edad < 30:
    print('Adulto joven')
elif edad >= 30:
    print('Adulto')


#ejercicio5
paswor = input('ingrese contrasena: ')
longitud = len(paswor)
if longitud >=8 and longitud <= 14:
    print('Ha ingresado una contrasena correcta.')
else:
    print('Por favor, ingrese una contrasena de entre 8 y 14 caracteres')
    

#ejercicio6
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
print('numeros_aleatorios')
print(numeros_aleatorios)
print('ahora vamos a calcular la moda, su mediana, y la media para determinar sesgo')
moda= mode(numeros_aleatorios)
mediana= median(numeros_aleatorios)
media= mean(numeros_aleatorios)
print(f'moda:{moda}-mediana:{mediana}-media:{media}')

if moda == mediana and moda == media:
    print('No hay sesgo.')
elif media > mediana and mediana > moda:
    print('Hay sesgo positivo o a la derecha.')
elif media < mediana and mediana < moda:
    print('Hay sesgo negativo o a la izquierda.')
else:
    print('sucedio otra condicion :(')

#ejercicio7
palabra = input('Ingrese palabra en minuscula: ')
longitud = len(palabra)
ultimo_caracter = palabra[longitud-1]
if ultimo_caracter == 'a' or ultimo_caracter == 'e' or ultimo_caracter == 'i' or ultimo_caracter == 'o' or ultimo_caracter == 'u':
    palabra = palabra + '!'
    
print(f'palabra final es: {palabra}')

#ejercicio8
nombre = input('Ingrese nombre: ')
print('1: mayuscula\n2: minuscula\n3: titulo.')
opcion = int(input('ingrese opcion: '))
if opcion == 1:
    nombre = nombre.upper()
elif opcion == 2:
    nombre = nombre.lower()
elif opcion == 3:
    nombre = nombre.title()
else:
    print('opcion invalida.')
print(nombre)


#ejercicio9
magnitud_terremoto = int(input('Ingrese la magnitud del terremoto: '))
print('La magnitud es: ')
if magnitud_terremoto < 3:
    print('Muy leve (imperceptible)')
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print('Leve (ligeramente perceptible)')
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print('Moderado (sentido por personas, pero generalmente no causa danos)')
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print('Fuerte (puede causar danos en estructuras debiles)')
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print('Muy Fuerte (puede causar danos significativos)')
elif magnitud_terremoto >= 7:
    print('Extremo (puede causar graves danos a gran escala)')
else:
    print('invalida')
    

#ejercicio10
hemisferio = input('Ingrese n o s segun su hemisferio: ')
mes = int(input('Ingrese mes (1al12) : '))
dia = int(input('Ingrese dia: '))

if (mes == 12 and dia >= 21) or (mes==1) or (mes==2) or (mes==3 and dia <= 20):
    if hemisferio == 'n':
        print('Invierno')
    elif hemisferio == 's':
        print('Verano')

if (mes == 3 and dia >= 21) or (mes==4) or (mes==5) or (mes==6 and dia <= 20):
    if hemisferio == 'n':
        print('Primavera')
    elif hemisferio == 's':
        print('Otono')

if (mes == 6 and dia >= 21) or (mes==7) or (mes==8) or (mes==9 and dia <= 20):
    if hemisferio == 'n':
        print('Verano')
    elif hemisferio == 's':
        print('Invierno')

if (mes == 9 and dia >= 21) or (mes==10) or (mes==11) or (mes==12 and dia <= 20):
    if hemisferio == 'n':
        print('Otono')
    elif hemisferio == 's':
        print('Primavera')
