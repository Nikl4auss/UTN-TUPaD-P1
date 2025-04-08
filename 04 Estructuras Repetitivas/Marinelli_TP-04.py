#Actividad 1

# for i in range(101):
#     print(i)

#Actividad 2

# num = int(input("Ingrese un número entero: "))

# digitos = 0

# while num > 0:
#     num //= 10
#     digitos += 1

# print("La cantidad de dígitos es:", digitos)

#Actividad 3

# limite_1 = int(input("Ingrese el límite inferior: "))
# limite_2 = int(input("Ingrese el límite superior: "))

# acc = 0

# for i in range(limite_1 + 1, limite_2):
#     acc += i
# print("La suma de los números entre", limite_1, "y", limite_2, "es:", acc)

#Actividad 4

# acc = 0
# num = int(input("Ingrese un número entero: "))

# while num != 0:
#     acc += num
#     num = int(input("Ingrese un número entero (ingrese 0 para detener el programa): "))
# print("La suma de los números ingresados es:", acc)

#Actividad 5

# import random

# print("¡Bienvenido al juego de los números aleatorios!")
# print("Adivina el número entre 0 y 9")
# random_number = random.randint(0, 9)
# user_number = int(input("Ingrese un número: "))
# tries = 1

# while user_number != random_number:
#     print("El número ingresado no es correcto")
#     tries += 1
#     user_number = int(input("Ingrese un número entre 0 y 9: "))

# print("¡Felicidades! Adivinaste el número en", tries, "intentos.")

#Actividad 6

# for i in range(100, -1, -1):
#   print(i)

#Actividad 7
# acc = 0
# limite = int(input("Ingrese un número entero positivo: "))

# while limite < 0:
#     print("Ingreso un numero negativo")
#     limite = int(input("Ingrese un número entero positivo: "))

# for i in range(0, limite + 1):
#       acc += i

# print("La suma de los números entre 0 y", limite, "es:", acc)

#Actividad 8

# positivos = 0
# negativos = 0
# pares = 0
# impares = 0

# for i in range(1, 101):
#     num = int(input(f"Ingrese un número entero: (N°{i}): "))
#     if num > 0:
#         positivos += 1
#     elif num < 0:
#         negativos += 1
#     if num % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
# print(f"Números positivos: {positivos}\n" 
#       f"Números negativos: {negativos} \n"
#       f"Números pares: {pares} \n" 
#       f"Números impares: {impares}")

#Actividad 9

# media = 0

# cant_num = 100

# for i in range(1, cant_num + 1):
#     num = int(input(f"Ingrese un número entero: (N°{i}): "))
#     media += num
# media /= cant_num
# print(f"La media de los números ingresados es: {media}")

#Actividad 10

# number = int(input("Ingrese un número entero: "))

# number_reversed = ""

# while number > 0:
#     digit = number % 10
#     number_reversed += str(digit)
#     number //= 10

# number_reversed = int(number_reversed)
# print("El número invertido es:", number_reversed)