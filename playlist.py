"""vamos a crear una playlist"""
# Generamos una variable por fuera de la función
playlist = {}  # Diccionario vacío
playlist['canciones'] = []  # Lista vacía de canciones

# Siempre es ideal tener una función principal
def app():
    # Agregar playlist
    agregar_playlist = True
    while agregar_playlist: 
        nombre_playlist = input('¿Cómo deseas nombrar la playlist?: ')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False  # Ya tenemos un nombre, desactivar el True

            # Mandar llamar la función para agregar canciones
            agregar_canciones()

# Vamos a agregar una función para agregar canciones
def agregar_canciones():
    # Estamos utilizando BANDERA para agregar canciones
    agregar_cancion = True

    while agregar_cancion:
        pregunta = f'Agrega canciones para la playlist "{playlist["nombre"]}": \r\n'
        pregunta += 'Escribe una "X" para dejar de agregar canciones: '

        cancion = input(pregunta)
        
        if cancion.lower() == 'x':  # Verificar si el usuario quiere salir
            agregar_cancion = False
        elif cancion:  # Si el usuario ingresó una canción válida
            playlist['canciones'].append(cancion)  # Agregar la canción a la lista
            print(f'Canción "{cancion}" agregada a la playlist.')
#para ir imprimiendo lo que voy agregando a la lista
    print("Playlist creada:")
    print(f'Nombre: {playlist["nombre"]}')
    print('Canciones:', playlist['canciones'])


#funcion para mostrar resumen
def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist} \r\n')
    print('Canciones: \r\n')
    for cancion in playlist['canciones']:
        print(cancion)
# Ejecutar la aplicación
app()
