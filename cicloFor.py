"""
FOR

for i in elemento:
    instrucciones
    print("hola", ¡)
# i= variable de iteración
# elemento = lista, secuencia de números, etc

word = input("Ingresa una palabra: ")

for i in range(10):
    print(word)

print("Comienzo")
contador = 1

for i in [3, 4, 5, 6, 7, 8]:
    print(f'Vuelta número: {contador}')
    print(f'Hola, ahora i vale {i} y su cuadrado es {i ** 2}')
    contador +=1

print('Final')

"""
numero = int(input("¿En que número quieres la tabla de mulitplicar?"))
print("")

print(f'Tabla de Multiplicar del número: {numero}')

for i in range(1, 11):
    print(f'{i} x {numero} = {i*numero}')
