""" Realizar un examen con 3 preguntas que desees, el usuario debera Responder 
"Si" o "No" y al final otorgarle una calificación 
(la calificación se logra con una variable que inicia
en 0 y por cada respuesta correcta incrementa en 1)"""
#Funcion para hacer preguntas
def hacer_preguntas(pregunta, respuesta_correcta):
    respuesta = input(pregunta + " (Si/No): ").strip().lower()
    if respuesta == respuesta_correcta.lower():
        return 1
    else:
        return 0

#Inicializar la Calificación
calificacion = 0

#lista de preguntas y respuestas correctas
preguntas = [
    ("¿El sol es una estrell?", "Si"),
    ("¿La tierra es plana?", "No"),
    ("¿Python es un lenguaje de programación?", "Si")
]
#Bucle para hacer cada pregunta
for pregunta, respuesta_correcta in preguntas:
    calificacion += hacer_preguntas(pregunta, respuesta_correcta)

#mostrar la calificación final
print(f'Tu calificación final es: {calificacion}/{len(preguntas)}')