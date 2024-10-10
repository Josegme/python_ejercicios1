"""INPUT () para entrada de datos del usuario"""

#nombre = input("Cual es tu nombre: ") #Para que haga un salto de línea \r\n
#print(f'Hola {nombre}')


#Leer datos que serán números
edad = int(input('Cual es tu edad? '))

if edad >= 18:
    print('Ya puedes votar')
else:
    print('Aún no puedes votar')

#Mezclar con operadores 
numero = int(input("Agrega un número y te diré si es par o non \r\n"))

if numero % 2 == 0:
    print(f'El número {numero} es par')
else:
    print(f'El número {numero} es impar')



