"""Array - Listas"""
#list o arreglos en Python
lenguajes = ["Python", "Kotlin", "Java", "JavaScript"]
#llamamos a la lista
print(lenguajes)
#los Arrays (list) comienzan en la posición 0
print(lenguajes[0]) #python
print(lenguajes[2]) #java 

#método: Ordenar - utilizados en listas
lenguajes.sort()
print(lenguajes)

#Se puede acceder a un elemento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

#modificar un arreglo 
lenguajes[2] = "PHP"
print(lenguajes)

#Agregar elementos a un arreglo
lenguajes.append("Ruby")
print(lenguajes)

#Eliminar de un arreglo
del lenguajes[1]
print(lenguajes)

#eliminar de una arreglo (ultimo elemento de la list)
lenguajes.pop()
print(lenguajes)

#si le paso un Valor a Pop elimina una posicion. 
lenguajes.pop(0)
print(lenguajes)

#Eliminar por nombre
lenguajes.remove("PHP")
print(lenguajes)
