"""
Ejercicio:
Crea un programa en Python que haga las siguientes 4 preguntas al usuario, 
y que responda con "Verdadero" o "Falso". Al final, el programa debe calcular 
la calificación sobre 4.

Preguntas:
¿El agua hierve a 100 grados Celsius?
¿Un kilobyte tiene 1000 bytes?
¿El planeta Marte tiene 2 lunas?
¿El Monte Everest es la montaña más alta del mundo?
Requisitos:
El usuario debe responder con "Verdadero" o "Falso".
La calificación se debe incrementar en 1 por cada respuesta correcta.
Al final, muestra la calificación del usuario sobre el total de preguntas.
"""
print("===Este es el primer ejercicio ===")
#creamos una función para hacer preguntas
def hacer_pregunta(pregunta, respuesta_correcta):
    respuesta = input(pregunta + " (Verdadero/Falso): ").strip().lower()
    if respuesta == respuesta_correcta.lower():
        return 1
    else:
        return 0
#inicializamos el contador de la calificación  
calificacion = 0

#lista de preguntas y respuestas correctas
preguntas = [
    ("¿Un kilobyte tiene 1024 bytes?", "verdadero"),
    ("¿El agua hierve a 100 grados celsius?", "verdadero"),
    ("¿El planeta Marte tiene dos lunas?", "falso"),
    ("¿El Monte Everest es la montaña mas alta del mundo", "verdadero")
]
#utilizo el bucle para hacer las preguntas
for pregunta, respuesta_correcta in preguntas:
    calificacion += hacer_pregunta(pregunta, respuesta_correcta)

print(f"Tu calificación final es: {calificacion}/{len(preguntas)}")
print("")
print("===Este es el segundo ejercicio===")
print("")
#Primero creamos una función que realice las preguntas
def hacer_preguntas1(pregunta1, respuesta_correcta1):
    respuesta1 = input(pregunta1 + " (Si/No) ").strip().lower()
    if respuesta1 == respuesta_correcta1.lower():
        return 1
    else:
        return 0
#Inicializar el contador
calificacion1 = 0
#Realizo las preguntas con las respuesta correctas en una lista
preguntas1 = [
    ("¿La capital de Brasil es Río de Janeiro?: ", "No"),
    ("¿El río Nilo es el mas largo del Mundo?: ", "Si"),
    ("¿Australia es el continente mas grande?: ", "No"),
    ("¿El monte Kilimanjaro está en África?: ", "Si"),
    ("¿El desierto del Sahara es el mas grande el mundo?", "Si"),
]
#utilizamos el bucle para realizar las preguntas e ir contando las respuestas
for pregunta1, respuesta_correcta1 in preguntas1:
    calificacion1 += hacer_preguntas1(pregunta1, respuesta_correcta1)

print(f'Tu calificación final es {calificacion1}/{len(preguntas1)}')


