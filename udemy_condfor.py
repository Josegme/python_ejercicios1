lenguajes = ["Python", "Kotlin", "Java", "JavaScript"]

#Podemos utilizar un FOR para recorrer la lista pero si quiero interceptar
#algun elemento por ejemplo para hacer un cambio puedo agregar otra instruccion dentro del FOR como un IF (o un For dentoro de otro for etc)
for lenguaje in lenguajes:
    if lenguaje == "Python":
        print(lenguaje.upper())
    else:
        print(lenguaje)