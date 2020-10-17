#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "tololo90"
__email__ = "tololo90@gmail.com"
__version__ = "1.3"


def ej1():
    # Ejercicios de práctica con números
    print('Nuestra primera calculadora')
    '''
    Realice un calculadora, se ingresará por línea de comando dos
    números reales y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia

    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números
      se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7

    '''
    print("ingrese un numero real")
    x = int(input())
    print("ingrese otro numero real")
    y = int(input())

    suma = x + y
    resta = x - y
    resta_2 = y - x
    multiplicacion = y * x
    division = y / x
    division_2 = x / y
    potencia = x**y
    potencia_2 = y**x

    print("el resultado de sumar",x,"y",y,"es:",suma)
    print("el resultado de restar",x,"y",y,"es:",resta)
    print("el resultado de restar",y,"y",x,"es:",resta_2)
    print("el resultado de multiplicar",x,"y",y,"es:",multiplicacion)
    print("el resultado de dividir",y,"y",x,"es:",division)
    print("el resultado de dividir",x,"y",y,"es:",division_2)
    print("el resultado de la potencia",x,"al",y,"es:",potencia)
    print("el resultado de la potencia",y,"al",x,"es:",potencia_2)

def ej2():
    print('Ejercicios de práctica numérica y cadenas')
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona

    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre aclarando de que
      campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y
      altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea
      entienda de que se está hablando.

    '''
    print("ingrese su nombre completo")
    a = str(input())
    print("ingrese su numero de documento")
    b = int(input())
    print ("ingrese su edad")
    c = int(input())
    print("ingrese su altura en cm")
    d = int(input())
    print("nombre completo:",a,"dni:",b)
    print("nombre completo:",a,"edad:",c, "altura en cm:",d)

def ej3():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos
      de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar
    el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método
    que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus

    '''
    print("ingrese nombre y apellido de su padre")
    padre = str(input())
    print("ingrese nombre y apellido de su madre")
    madre = str(input())
    print("ingrese su nombre")
    hijo = str(input())
    padre_2 = padre.split()
    madre_2 = madre.split()
    nombre_completo = hijo + " " + padre_2[-1] + " " + madre_2[-1]
    print("su nombre completo es ", nombre_completo)
    

def ej4():
    # Ejercicios de práctica con cadenas
    print('Comencemos a ponernos serios')
    '''
    Realice un programa que determine si una persona_2
    es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre
    y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir,
    primero el nombre y luego el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido
      en el nombre completo de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos
    usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca
    de este método que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    '''
    print("ingrese nombre y apellido de la primer persona")
    persona_1 = str(input())
    print("ingrese nombre y apellido de la segunda persona")
    persona_2 = str(input())
    apellido_persona_2 = persona_2.split()
    parientes = apellido_persona_2[-1] in persona_1
    print("son parientes",persona_1, "y",persona_2,"?",parientes)
def ej5():
    # Ejercicios de práctica con cadenas
    print('Ahora si! buena suerte!')
    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    '''
    print("ingrese su nombre y apellido")
    nombre = str(input())
    print(nombre.lower())
    print(nombre.upper())
    print(nombre.capitalize())
if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
