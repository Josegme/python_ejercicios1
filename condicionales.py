"""Condicionales

#primer ejemplo
#Crear un programa que reciba el numero de años que tiene nuestra computadora
#Decir si es viejo o es nuevo
#Condicion: si es menor a 2 años es nuevo y si es mayor es viejo 

anios = int(input("Cuantos tiene tu computador: "))

if anios >= 0 and anios <= 2:
    print("Tu computadora es nueva")
else:
    print("Tu computadora es vieja")


edad = int(input("Cuantos años tienes? "))

if edad >= 18:
    print("Es usted mayor de edad.")
else: 
    print("Es usted menor de edad")

print("Hasta la proxima.") 

#Condicionales con elif (varias condiciones)
#En una escuela de conducción que dependiendo de la edad del usuario
#debe mostrar diferenes situaciones 
#Condición 1: Si es menor a 16 no puede conducir
#Condición 2: Si es menor a 18 obtiene una licencia de conducir
#Condición 3: Si es menor a 70 puede obtener una lic estandar
#Condición 4: Si es mayor a 70 necesita una licencia especial

edad = int(input("Digita tu edad"))

if edad < 16: 
    print("No tienes edad para conducir") 
elif edad < 18:
    print("Puedes obtener permiso para conducir")
elif edad < 70:
    print("Puedes obtener una licencia estandar")
else:
    print("Necesita una licencia Especial") 

#Condicionales ANIDADOS (IF DENTRO DE OTRO IF)
edad = int(input("¿Cuántos años tienes? "))
graduacion = input("¿Ya te has graduado? (si) o (no) ").lower()

if edad >= 18:
    print("Felicidades, ya eres mayor de edad.")
    if graduacion == "si":
        print("¡Felicidades por tu graduación!")
    else:
        print("¡Pues ponte a ello!")
else:
    print("Aún no eres mayor de edad. ¡Sigue estudiando!")
"""

password = input("Ingrese la contraseña: ")

if (len(password) >= 8) :
    print("Muy bien, contraseñan suficientemente larga")

    if (password == "Prueba12345"):
        print("Ademas, es la contraseña correcta")
    else: 
        print("Pero es incorrecta")
else:
    print("Tu contraseña es incorrecta e insegura")


