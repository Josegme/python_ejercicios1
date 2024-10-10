#IF anidados 

usuario_autenticado = True
usuario_admin = True

if usuario_autenticado:
    if usuario_admin:
        print("Acceso total")
    else:
        print("Acceso al Sistema")
else:
    print("Debes inciar sesión")

#en este caso para que nos de acceso total
#las primeras condiciones deben ser TRUE
#es decir, que evalúa ambas condiciones sino "Debe inciar Sesion"(si alguna da False)

#IF ..ELIF ... ELSE

ocupacion = "Estudiante"

if ocupacion == "Jubilado":
    print("Tienes un descuento del 75%")
elif ocupacion == "Estudiante":
    print("Tienes un 50% de Descuento")
elif ocupacion == "Desempleado":
    print("Tienes un 10% de descuento")
else: 
    print("Debes pagar el 100%")

#Podemos agregar todos los elif que necesitemos cuando queremos evaluar varias condiciones.

#Cuando queremos que se cumplan dos o mas condiciones 
#o almenos una de las condiciones utilizamos los Operadores logicos
#AND y OR con los IF o ELIF ..
#como sabemos para que AND se Verdadero true and true = V , de lo contrario siempre es falso
usuario_logueado = True
usuario_admin2 = False
#para que ingrese al sistema ambos tiene que ser verdadero
if usuario_logueado and usuario_admin2:
    print("Administrador")
elif usuario_logueado:
    print("Acceso al sistema")
else: 
    print("Debe iniciar Sesión")

#entonces tanto AND y OR me sirven para evaluar las condiciones
#Operan según será true o false basado en las operaciones lógicas.
