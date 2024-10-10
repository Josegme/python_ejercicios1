#Solicitar Información
# Declaramos la variable "nombre" que almacena el nombre del usuario
# y la de "materias" que inicializamos con 5
print("**** Promedio del Semestre ****")
print("")
nombre = input("Nombre Completo: ")
materias = 5

# Definimos: variable "contador" que se encarga de iterar
# "sumatoria" para sumar las calificaciones ingresadas
contador = 1
sumatoria = 0

# Creamos el ciclo While (dentro va a solicitar el nombre de la materia y la calificación)
# Se sumará cada calificación y se incrementará el contador
while contador <= materias:
    nombre_materia = input("Ingresa el nombre de la materia " + str(contador) + ": ")
    calificacion = float(input("Calificación obtenida en " + str(nombre_materia) + ": "))

    # Sumar la calificación a la sumatoria
    sumatoria += calificacion #sumatoria = sumatoria + calificación
    # Aumentar el contador para no hacer el ciclo infinito
    contador += 1 #contador = contador + 15

# Realizamos el cálculo del promedio e imprimimos el resultado
promedio = sumatoria / materias
print("***** Resultados *****")
print(f'Hola, {nombre}. Tienes un promedio de {promedio:.2f} en el 5to Semestre.')



