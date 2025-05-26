#trabajo_practico_5b_funciones_DiegoCarrizo

import math

#funciones
#1
def imprimir_hola_mundo():
    print('Hola Mundo!')
#2
def saludar_usuario(nombre):
    return f'Hola {nombre}!'
#3
def informacion_personal(nombre,apellido,edad,residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} anios y vivo en {residencia}')
#4a
def calcular_area_circulo(radio):
    area = (math.pi) * (radio**2)
    return area
#4b
def calcular_perimetro_circulo(radio):
    perimetro = 2 * (math.pi) * radio
    return perimetro
#5
def segundos_a_horas(seg):
    horas = seg // 3600
    return horas
    
#6
def tabla_multiplicar(num):
    for var in range(1,11,1):
        print(f'{num} x {var} = {var*num}')

#7
def operaciones_basicas(a,b):
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    division=a/b
    return (suma, resta, multiplicacion,division)

#8
def calcular_imc(peso, altura):
    imc = peso/(altura**2)
    imc = round(imc,2)
    return imc
    
def celsius_a_fahrenheit(c):
    return (c * (9/5)) + 32

def calcular_promedio(a,b,c):
    promedio = (a+b+c) / 3
    return promedio


#ProgramaPrincipal
print('Inicio del Tp de Funciones de Diego Carrizo')
#1
print('\nEjercicio 1')
imprimir_hola_mundo()

#2
print('\nEjercicio 2')
nombre = input('Ingrese nombre: ')
print(saludar_usuario(nombre))

#3
print('\nEjercicio 3')
nombre = input('Ingrese nombre: ')
apellido = input('Ingrese apellido: ')
edad = int(input('Ingrese edad: '))
residencia = input('Ingrese residencia :')
informacion_personal(nombre, apellido, edad, residencia)

#4
print('\nEjercicio 4')
radio= int(input('Ingrese el radio de un circulo: '))
retorno_area = calcular_area_circulo(radio)
retorno_perimetro = calcular_perimetro_circulo(radio)
print(f'El area del circulo es {retorno_area}')
print(f'El perimetro del circulo es {retorno_perimetro}')


#5
print('\nEjercicio 5')
segundos = int(input('Ingrese segundos: '))
horas = segundos_a_horas(segundos)
print(f'Los segundos convertidos en horas son: {horas}')


#6
print('\nEjercicio 6')
numero_t=int(input('Ingrese un numero para generar su tabla de multiplicar del 1 al 10: '))
tabla_multiplicar(numero_t)

#7
print('\nEjercicio 7')
numero_a = int(input('Ingrese numero_a: '))
numero_b = int(input('Ingrese numero_b: '))
suma, resta, multiplicacion, division = operaciones_basicas(numero_a, numero_b)
print('resultados:')
print(f'suma: {suma}')
print(f'resta: {resta}')
print(f'division: {division}')
print(f'multiplicacion: {multiplicacion}')

#8
print('\nEjercicio 8')
peso= float(input('Ingrese peso en kg: '))
altura= float(input('Ingrese altura en m: '))
resultado_redondeado = calcular_imc(peso,altura)
print(f'El imc es de: {resultado_redondeado}')

#9
print('\nEjercicio 9')
celsius = float(input('Ingrese temperatura en celsius para convertir: '))
fah = celsius_a_fahrenheit(celsius)
print(f'La temp convertida a fah es de: {fah}')

#10
print('\nEjercicio 10')
ingreso1 = float(input('Ingrese primer numero para sacar promedio: '))
ingreso2 = float(input('Ingrese segundo numero para sacar promedio: '))
ingreso3 = float(input('Ingrese tercer numero para sacar promedio: '))
promedio = calcular_promedio(ingreso1,ingreso2,ingreso3)
print(f'El promedio de los ingresos es: {promedio}')

print('\nFin del Tp de Funciones - Diego Carrizo')
