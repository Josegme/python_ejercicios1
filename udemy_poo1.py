#cuando creamos una clase iniciamos con Mayuscula
class Restaurant:       
    #podemos agregar el método/funciones
    def agregar_restaurant(self, nombre):   #self>se para que tome la llamada del metodo.
        self.nombre = nombre  #atributo y self es lo que requiere para guardar la infomracion de nombre

    def mostrar_informacion(self):  #hay que pasarle SELF a todos los métodos que tenga
        print(f'Nombre: {self.nombre} ')

#Instanciar la clase (nombre_variable = nombre_Clase)
restaurant = Restaurant()
#objeto         #clase
#como llamo la clase- nombre_variable.metodo
restaurant.agregar_restaurant('Pizzeria Hulk') 
restaurant.mostrar_informacion() #solamente mando a llamar ese método

restaurant2 = Restaurant()  #podemos crear multiples objetos con diferente información-
                            #cada objeto va a ser diferente, utilizamos la misma clase y forma de los datosy puedo almancenar datos diferentes
#copio entonces la misma estructura para restaurant2
restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Pizzeria Python')
restaurant2.mostrar_informacion()

restaurant3 = Restaurant()
restaurant3.agregar_restaurant('Pizzeria POO')
restaurant3.mostrar_informacion()

#SELF es una forma de referirse al objeto que se esta ejecutando
#la CLASE es la que nos da la forma, los dif atributos y los dif métodos que va a tener un objeto
#cada objeto va a tener la información única

#MOSTRAR la INFO de manera diferente

print(f'Nombre Restaurant: {restaurant.nombre}')
print(f'Nombre Restaurant: {restaurant2.nombre}')
print(f'Nombre Restaurant: {restaurant3.nombre}')

#es otra forma de acceder a la información
