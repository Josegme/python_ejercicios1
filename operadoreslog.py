"""
Operadores lógicos : and, or, not
"""
#defino las variables booleanas
a = True # defino como verdadero
b = True # defino como verdadero

#and
print(a and b)

c = False
d = True
print(c and d)

#or
print(b or c)
print(c or not d)

print(not(c and d))

"""Operadores Relacionales"""
#declaramos las variables
a = 5
b = 8 

print(a == b) #compara si la var a es igual a la var bestos son iguales
print(a != b)  #compara si son disntintos
print(a < b)    #compara si es menor
print(a > b)   #compara si es mayor
print(a <= b)
print(a >= b)