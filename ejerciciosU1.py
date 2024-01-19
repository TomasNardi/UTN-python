"Tomas Martin Nardi"

"""Ejercicio 1:
Cree un programa que tome tres valores por consola multiplique el primero por el segundo
y le sume el tercero. Presente el resultado en la terminal"""

num1 = float(input("Ingrese el primer valor : "))
num2 = float(input("Ingrese el segundo valor : "))
num3 = float(input("Ingrese el tercer valor : "))

print("La multiplicacion del primer valor por el segundo + el tercero es igual a :",(num1*num2)+num3)

print("----------------------------------------")

"""Ejercicio 2:
Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
son múltiplos de dos."""

import sys

num1 = int(input("Ingrese el primer valor : "))
num2 = int(input("Ingrese el segundo valor : "))
num3 = int(input("Ingrese el tercer valor : "))

if num1 % 2 == 0:
    print (num1,"es múltiplo de dos.")
else: 
    print(num1,"no es múltiplo de dos.")

if num2 % 2 == 0:
    print (num2,"es múltiplo de dos.")
else: 
    print(num2,"no es múltiplo de dos.")

if num3 % 2 == 0:
    print (num3,"es múltiplo de dos.")
else: 
    print(num3,"no es múltiplo de dos.")

print("----------------------------------------")

"""Ejercicio 3:
Escriba un programa que solicite el radio de una circunferencia y permita calcular el perímetro. 
Presente el resultado en la terminal del editor
perímetro. 

Utilice la siguiente fórmula:
L = 2 · π · r
L = Longitud de perímetro
π = Número pí igual a 3.1416
r = Radio """

num1 = (float(input("Ingrese el radio de una circunferencia para que pueda calcular el perímetro :")))

resultado = (2*3.1416*num1)

print ("El perimetro de una circunferencia de radio ", num1,"es igual a :", (resultado))

print("----------------------------------------")

"""Ejercicio 4:
Escriba un programa que solicite el radio de una circunferencia y permita calcular el
área. Presente el resultado en la terminal del editor.
Utilice la siguiente fórmula:
𝐴 = 𝜋. 𝑟2
A = Área
π = Número pi igual a 3.1416
r = Radio """

num1 = (float(input("Ingrese el radio de una circunferencia para que pueda calcular el área :")))

resultado = (3.1416*((num1)*2))

print ("El área de una circunferencia de radio ", num1,"es igual a :", (resultado))

print("----------------------------------------")

"""Ejercicio 5:
solicite un valor entero por pantalla y presente en la terminal
el valor incrementado en un 10%.
"""
num1 = (int(input("Ingrese un valor entero :")))
resultado = (num1*1.1)

print("El valor ingresado es ",num1, "+ el 10% : ",resultado)

print("----------------------------------------")