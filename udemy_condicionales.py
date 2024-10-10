"""Condicionales en Python"""
#Revisar si una condiciones es mayor a
balance = 500
if balance > 0:
    print("Puedes pagar")

#Condición IF ..ELSE
#Si la condicion se evalua como Verdadera se ejecuta el código/innstruccion
#Si no (else) ocurre otra cosa: se da un aviso (o se ejecuta otra instrucción)

balance2 = 0
if balance2 > 0:
    print("Puedes Pagar")
else:
   print("No tienes Saldo")
#si la condición es F entonces, se corre el ELSE

#LIKES
likes = 200
#si queremos saber si es exactemente igual
if likes == 200:
    print("Excelente, 200 Likes exactos")

#Comparación IF con TEXTO
lenguaje = "Python"

if lenguaje == "Python":
    print("Excelente Decisión")


#En python podemos negar una Codición
lenguaje2 = "PHP"
if not lenguaje2 == "Python":
    print("Estas usando otro lenguaje")

#If para evaluar Boolean
usuario_autenticado = True

if usuario_autenticado == False:
    print("Acceso al Sistema")
else: 
    print("Debes iniciar sesión")

#en Python el booleano en IF no hace falta colocar el operador para que evalue True o False

tiene_ticket = True

if tiene_ticket:
    print("Puede Ingresar")
else:
    print("Debe comprar en Boleteria")

#sirve para evaluar boolean y no escribir tanto código.
