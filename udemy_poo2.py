#Abstracción y constructores
"""
Eel ejercicio anterior tenía esto..entonces

class Restaurant: 

    def agregar_restaurant(self, nombre):
        self.nombre = nombre #atributo

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')
"""
#cuando creo un nuevo objeto mando a llamar a la clase de ese objeto
#y despues utilizo otra funcion para agregar al atributo, en este caso "nombre"
#usualment esto se puede agregar por medio de un constructor
#¿Que es un CONSTRUCTOR? es una función que se ejecuta automáticamente al crear un nuevo objeto por medio de una clase 
#si utilizamos un constructor
class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
    
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio} ')

#Instanciamos la clase
restaurant = Restaurant('Pizzeria Hulk', 'Comida Italiana', 80)
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Pizzeria Python', 'Comida Rápida', 50)
restaurant.mostrar_informacion()

#podemos seguir agrenado argumentos y agregamos como parte de nuestra información
#como sabemos QUE DATOS VAMOS REQUERIR
#depende de lo que necesitemos programar: hay que evaluar que datos son necesarios en cada clase.
