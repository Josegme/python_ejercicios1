"""Funciones"""

def mi_funcion() :
    print('inst 1')
    print('inst 2')
    print('inst 3')

#Programa 1
mi_funcion()
print('inst 4')
mi_funcion()
print('inst 4')
print('inst 5')
print('inst 6')
mi_funcion()
print('inst 4')
print('inst 5')
print('inst 6')
print('inst 7')

#Mas ejemplos

def saludar():
    print('Hola Programador')
    print('Cual es tu nombre?')

saludar()
#De esta manera podemos llamar a la funcion cuando necesite

def suma():
    print(f'La seuma es: {5 + 7}')

suma()

saludar()
suma()
#para que se muestre la función se debe invocar a dicha función

#Funciones con PARAMETROS

def es_par(numero):
    if numero % 2 == 0:
        print(f'El número {numero} es par')
    else:
        print(f'El número {numero} es impar')

es_par(5) #recordar que hay que incorporar el argumento solicitado para que la funcion opere.
es_par(10)
es_par(7.5)

#Ejemplo funcion con PArametros.
def saludar(nombre):
    print('Hola,' + nombre + ' eres el mejor programador')

saludar("Jose")

#Ejemplo 3

def resta(a = None, b = None):
    if a == None or b == None:
        print('Error, debes enviar números a la función')
        return
    return a-b
#recordar de colocar el return cuando estoy haciendo operaciones aritemeticas
#luego llamo a la función pero para poder ver el resultado debo colocar una variable e Imprimir
#llamando a la variable que contiene a la función con sus argumentos.
resta()

resultado = resta(9 , 5)
print(resultado)

#Ejemplo de función: Tabla de multipicar

def multiplicacion(numero = None):
    if numero == None:
        print("Por favor, introduce un número")
    else:
        print(f'Tabla de Multiplicar del {numero}')
        for i in range(1 , 11):
            print(f'{numero} x {i} = {numero * i}')
    

multiplicacion()
multiplicacion(2)
multiplicacion(7)