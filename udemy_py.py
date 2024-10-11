"""Python Curso Udemy"""

libro_favorito = "100 años de Soledad - Gabriel Garcia Marquez"

merienda = "Facturas con Mate"

print(libro_favorito)
print(merienda)

nombre = "Juan Pablo" #"entre comillas es string"
print(nombre)

edad = 18 #sin comillas es numero 
print(edad) #si reasigno el valor siempre toma el ultimo valor

cantidad_pagar = 10.5 #float - decimal 
print(cantidad_pagar)

#para valores booleanos True o False
pagado = True
print(pagado) 


#Funciones

def my_funcion(): 
    print("Es mi primera función") #en python autmaticamente me identa para todo quede dentro de la función

my_funcion() #la funcion puede ser llamada cuando la necesite, cuantas veces quieras

#se pueden agregar parametros dentro del ()

#Defino una segunda funcion con parametros
def informacion(nombre, puesto = "Desconocido"):
    print(f'Soy {nombre} y soy {puesto}')
#Si escribo 2 parametros, cuando llame a la Función van a tener que tener dos argumentos
#de lo contrario me va a dar un error - Para resolver se puede agregar un parametro por default con =
informacion('Pedro', 'Programador')
informacion('Itzel', 'Diseñadora')
informacion('Juan')

#es decir que si falta algun Argumento lo puedo resolver con la asignacion de parametros por Defoult

