"""Iteradores"""
lenguajes = ["Python", "Kotlin", "Java", "JavaScript"]

#como acceder a la lista de manera mas rápida. 
#Iterador
for lenguaje in lenguajes: #Se recomienda cuando usamos iteradores que coloquemos en Singular el Iterador que va a recorrer la lista de variable en Plural.
    print(lenguaje)

#En este caso recorre la lista completa, uno por uno y no tengo que escribir tantas líneas de código.
#Si le quiero agregar un texto adentro del FOR
for lenguaje2 in lenguajes:
    print(f'Estoy aprendiendo a aplicar for, y estudiando {lenguaje2}')

#tenemos que tener cuidado con la Identación, ya que todo lo que este identado debajo del For ser´parte del interador.

#For que escriba números, podemos utilzar RANGE
for numero in range(0, 20):
    print(numero)

#va a imprimir hasta la posición 20 (es decir, imprime de 0 ...a...19) y se corta.
