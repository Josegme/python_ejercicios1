#Creando un Diccionario Simple
cancion = {
    'artista' : 'Metallica', #clave : valor
    'canción': 'Enter Sandman',
    'Lanzamiento': 1992,
    'likes': 3000
}

print(cancion)
#para acceder al diccionario
print(cancion['artista'])

#mezclar con un string - se recomienda crear un variable que asigne la clave-valor para que no de error
artista = cancion['artista']
print(f'Estoy escuchando a {artista}')
print(cancion)

#Agregar nuevas claves:valor en el Diccionario

cancion['playlist'] = "Heavy Metal"
print(cancion) 

#reemplazar valor existente
cancion['canción'] = 'Seek & Destroy'
print(cancion)
#si el nuevo valor no existe lo agrega pero si existe lo reemplaza

#Elimnar valor
del cancion['Lanzamiento']
print(cancion)
#Podemos manipulgar los elementos del diccionaro (objeto) 

