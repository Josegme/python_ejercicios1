"""En Python no se puede colocar comillas a los numeros"""
print(2)
print(4)

print(2.5)

print( 2 + 3 )
print( 8 - 4 )
print( 8 * 4 )
print( 10 / 2 )

print( 2 ** 2)
print( 5 ** 2 )

#funciona con las reglas de matemáticas
#en el caso que coloque print( 8 - "4") me va a dar un error
numero = 20 
print(numero)
numero +=1 
print(numero)
numero +=5
print(numero)

print("===Numeros con Funciones===")

def suma(a = 0, b = 0):
    print(a + b)

suma(2 , 3)

def resta(c = 0 , d = 0):
    print(c - d)

resta(3 , 2)
resta(20 , 45)

def multiplicacion(e , f):
    print(e * f)

multiplicacion(2 , 6)

def division(g , h):
    print(g / h)

division(10, 2)
