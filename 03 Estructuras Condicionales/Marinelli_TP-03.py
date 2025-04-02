#Actividad 1

# edad = int(input("Ingrese su edad: "))

# if edad < 0:
#     print("Usted ingresó una edad negativa")
# else:
#   if edad >= 18:
#     print("Es mayor de edad")
#   
#Actividad 2

# nota = float(input("Ingrese su nota: "))

# if nota < 0 or nota > 10:
    # print("Ingresó una nota incorrecta")
# else:
    # if nota >= 6:
        # print("Aprobado")
    # else:
        # print("Desaprobado")

#Actividad 3

# num = int(input("Ingrese un número: "))

# if num % 2 == 0:
#     print("Ha ingresado un número par")
# else:
#     print("Por favor, ingrese un número par")

#Actividad 4

# edad = int(input("Ingrese su edad: "))

# if edad >= 0 and edad < 12:
    # print("Es un/a niño/a")
# elif edad >= 12 and edad < 18:
    # print("Es un adolescente")
# elif edad >= 18 and edad < 30:
    # print("Es un/a adulto/a joven")
# elif edad >= 30:
    # print("Es un/a adulto/a")
# else:
    # print("Ha ingresado una edad incorrecta")
# 
# 

#Actividad 5

# contraseña = input("Ingrese su contraseña: ")
# largo_contraseña = len(contraseña)
# if largo_contraseña >= 8 and largo_contraseña <= 14:
    # print("Ha ingresado una contraseña correcta")
# else:
    # print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Actividad 6

# from statistics import mode, median, mean
# import random

# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# print(numeros_aleatorios)

# moda = mode(numeros_aleatorios)
# print(moda)
# mediana = median(numeros_aleatorios)
# print(mediana)
# media = mean(numeros_aleatorios)
# print(media)

# if media > mediana and mediana > moda:
#   print("Sesgo positivo")
# if media < mediana and mediana < moda:
#   print("Sesgo negativo")
# if media == mediana and mediana == moda:
#   print("No hay sesgo")

#Actividad 7

# palabra = input("Ingrese una frase o palabra: ")

# if palabra.endswith(("a", "e", "i", "o", "u")):
#     print(palabra + "!")
# else:
#     print(palabra)

#Actividad 8

# nombre = input("Ingrese su nombre: ")
# opcion = input("Ingrese alguna de las siguientes opciones: "
# "\n 1. Si quiere que su nombre se muestre en mayúsculas "
# "\n 2. Si quiere que su nombre se muestre en minúsculas "
# "\n 3. Si quiere que su nombre se muestre con la primera letra en mayúscula "
# "\n"
# )

# if opcion == "1":
#     print(nombre.upper())
# elif opcion == "2":
#     print(nombre.lower())
# elif opcion == "3":
#     print(nombre.capitalize())
# else:
#     print("Ha ingresado una opción incorrecta")

#Actividad 9

# escala = int(input("Ingrese la escala del Terremoto: "))

# if escala < 3:
#   print("Muy leve")
# if escala >= 3 and escala < 4:
#   print("Leve")
# if escala >= 4 and escala < 5:
#   print("Moderado")
# if escala >= 5 and escala < 6:
#   print("Fuerte")
# if escala >= 6 and escala < 7:
#   print("Muy fuerte")
# if escala >= 7:
#   print("Extremo")

#Actividad 10
from datetime import date

hemisferio = input("Ingres el emisferio en el que se encuentra: (N para Norte, S para Sur) ").upper()

mes = int(input("Ingrese el mes en el que se encuentra: \n "
"1. Enero \n "
"2. Febrero \n "
"3. Marzo \n "
"4. Abril \n "
"5. Mayo \n "
"6. Junio \n "
"7. Julio \n "
"8. Agosto \n "
"9. Septiembre \n "
"10. Octubre \n "
"11. Noviembre \n "
"12. Diciembre \n "
))

dia = int(input("Ingrese el día en el que se encuentra: "))

fecha_usuario = date(2025, mes, dia)

fecha_inicio_septiembre_diciembre = date(2025, 9, 21)
fecha_fin_septiembre_diciembre = date(2025, 12, 20)

fecha_inicio_diciembre_marzo = date(2025, 12, 22)
fecha_fin_diciembre_marzo = date(2025, 3, 20)

fecha_inicio_marzo_junio = date(2025, 3, 21)
fecha_fin_marzo_junio = date(2025, 6, 20)

fecha_inicio_junio_septiembre = date(2025, 6, 21)
fecha_fin_junio_septiembre = date(2025, 9, 20)

if hemisferio == "N":
  if fecha_inicio_diciembre_marzo <= fecha_usuario <= fecha_fin_diciembre_marzo:
    print("Es invierno")
  elif fecha_inicio_marzo_junio <= fecha_usuario <= fecha_fin_marzo_junio:
    print("Es primavera")
  elif fecha_inicio_junio_septiembre <= fecha_usuario <= fecha_fin_junio_septiembre:
    print("Es verano")
  elif fecha_inicio_septiembre_diciembre <= fecha_usuario <= fecha_fin_septiembre_diciembre:
    print("Es otoño")

elif hemisferio == "S":
  if fecha_inicio_diciembre_marzo <= fecha_usuario <= fecha_fin_diciembre_marzo:
    print("Es verano")
  elif fecha_inicio_marzo_junio <= fecha_usuario <= fecha_fin_marzo_junio:
    print("Es otoño")
  elif fecha_inicio_junio_septiembre <= fecha_usuario <= fecha_fin_junio_septiembre:
    print("Es invierno")
  elif fecha_inicio_septiembre_diciembre <= fecha_usuario <= fecha_fin_septiembre_diciembre:
    print("Es primavera")
else:
  print("Ha ingresado un hemisferio incorrecto")