#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.4

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "tololo90"
__email__ = "tololo90@gmail.com"
__version__ = "1.4"

def ej1():
    # Ejercicios de práctica numérica
    numero_1 = 5
    numero_2 = 7

    # Realizar la suma de las dos variables
    # numero_1 y numero_2
    # Almacenar el valor de la suma en una variable
    # ej:
    # operacion = .....

    # Imprimir en pantalla el resultado de la suma
    # print(....)

    # Repita el procedimiento para realizar la resta

    suma= numero_1 + numero_2

    print("el resultado de la suma entre", numero_1 , "y", numero_2,"es",suma)

    resta= numero_1 - numero_2

    print("el resultado de la resta entre", numero_1 , "y", numero_2,"es",resta)
    
def ej2():
    # Ejercicios de práctica numérica

    # Operadores con números decimales
    # Ahora los valores a operar deben ser ingresados por
    # consola con la función "input" como se ve a continuación
    print('Ingrese el primer número decimal a operar:')
    numero_1 = float(input())

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = float(input())

    # Alumno: Imprima en pantalla los dos números decimales solicitados
    # print(....)
    
    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma

    # Resta

    # División

    # Multiplicación
    print("el primer numero es",numero_1)
    print("el segundo numero es",numero_2)
    suma= numero_1 + numero_2
    resta= numero_1 - numero_2
    division= numero_1 / numero_2
    multiplicacion= numero_1 * numero_2
    print("el resultado de sumar", numero_1, "y" , numero_2, "es", suma)
    print("el resultado de restar", numero_1, "y" , numero_2, "es", resta)
    print("el resultado de dividir", numero_1, "y" , numero_2, "es", division)
    print("el resultado de multiplicar", numero_1, "y" , numero_2, "es", multiplicacion)

def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Imprima su nombre completo

    # Almacenar su nombre completo en una variable
    # nombre_completo = .....

    # Imprimir la cantidad de letras que posee su nombre completo
    print("nombre completo:", nombre, apellido)
    nombre_completo = nombre + apellido
    nombre_completolen= len(nombre_completo)
    print("el nombre" , nombre_completo, "tiene",nombre_completolen)

def ej4():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla
    acronimo = palabra_1[3] + palabra_2[1] + palabra_3[2]
    primera_letra = palabra_1[0]+palabra_2[0]+palabra_3[0]
    print(acronimo)
    print(primera_letra)

def ej5():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    # Formar una nueva palabra con los recortes solicitados
    # Imprima en pantalla los resultados
    palabra_3 = palabra_1[:3] + palabra_2[2:4]
    palabra_4 = palabra_1[2:4] + palabra_2 [:3]
    palabra_5 = palabra_2[:3] + palabra_1[2:4]
    print(palabra_3)
    print(palabra_4)
    print(palabra_5)
    palabra_6 = palabra_1[:3]
    palabra_7 = palabra_2[-3:]
    palabra_8 = palabra_6 + palabra_7
    print(palabra_8)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
