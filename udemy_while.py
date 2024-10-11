"""EL WHILE SE EJECUTA MIENTRAS LA CONDICIÓN SEA VERDADERA"""
"""
pregunta = "Agrega un número y te diré si es par o impar \r\n"
#podemos concatenar texto
pregunta += "(Escribe 'Cerrar' para salir de la apliación): "


preguntar = True

while preguntar:
    numero = input(pregunta)
    
    if numero == 'cerrar':
        preguntar = False
    else:
        numero = int(numero)
        if numero % 2 == 0 :
            print(f'El número {numero} es par.')
        else:
            print(f'El número {numero} es impar')
"""

#Incrementos con el WHILE - contador += 1 (incrementa en uno)

numero = 0

while numero <= 10: #mientras la variable numero sea menor o igual a 10
    print(numero)   #imprime el numero 
    numero += 1     #para que vaya contando la cantidad de numeros y corte el bucle

contador = 0

while contador <= 8:
    if contador == 5:
        print('Cincoooooo!!')
    else:
        print(contador)
    contador += 1


#tambien podemos utilizar un break para cortar el bucle   