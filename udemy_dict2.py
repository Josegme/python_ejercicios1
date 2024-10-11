#Iniciar un Diccionario vacío
jugador = {}
print(jugador)

#se une un jugador (le tengo que asignar una clave valor)
jugador['nombre'] = 'Juan'
jugador['puntaje'] = 0
print(jugador)

#que pasa si el puntaje se incrementa a medida que el jugador avanza
jugador['puntaje'] = 200
print(jugador)

#Acceder a un jugar / Acceder a un diccioario/obejeto
print(jugador.get('consola', 'No existe ese valor'))
#esta es una forma de manipular los elementos del diccionario

#Iterar en el diccionario
for llave, valor in jugador.items():
    print(llave) #si no coloca la llave solo me da nombre y el puntaje es decir los valores
    print(valor)
#ejemplo
for llave, valor in jugador.items():
    print(valor)
#en este caso no solicito la llave asi que me da solo los valores

#si el jugador sale del juego y quiero ELIMINAR todo
#utilizo DEL
del jugador['nombre']
del jugador['puntaje']
