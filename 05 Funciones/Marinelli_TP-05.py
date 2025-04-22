import math


# 1. Imprimir "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")


# 2. Saludo personalizado
def saludar_usuario(nombre):
    return f"Hola {nombre}!"


# 3. Información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# 4. Área y perímetro del círculo
def calcular_area_circulo(radio):
    return math.pi * radio**2


def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


# 5. Segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600


# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


# 7. Operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Infinito"
    return (suma, resta, multiplicacion, division)


# 8. Índice de Masa Corporal (IMC)
def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return round(imc, 2)


# 9. Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


# 10. Calcular promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3


def main():
    # 1 . Imprimir "Hola Mundo!"
    imprimir_hola_mundo()

    # 2. Saludo personalizado
    nombre = input("\nIngrese su nombre: ")
    print(saludar_usuario(nombre))

    # 3. Información personal
    nombre = input("\nIngrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

    # 4. Área y perímetro del círculo
    radio = float(input("\nIngrese el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")

    # 5. Segundos a horas
    segundos = int(input("\nIngrese la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")

    # 6. Tabla de multiplicar
    numero = int(input("\nIngrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)

    # 7. Operaciones básicas
    a = float(input("\nIngrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    suma, resta, multiplicacion, division = operaciones_basicas(a, b)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")

    # 8. Calcular IMC
    peso = float(input("\nIngrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Su índice de masa corporal es: {imc}")

    # 9. Celsius a Fahrenheit
    celsius = float(input("\nIngrese la temperatura en Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

    # 10. Calcular promedio
    num1 = float(input("\nIngrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    promedio = calcular_promedio(num1, num2, num3)
    print(f"El promedio de los tres números es: {promedio:.2f}")
