"""
Actividad Operadores Edutin
"""
# primero debo Solicitar los números al usuario
primer_numero = int(input("Ingresa el primer número: ")) #solicita ingresar el primer numero
segundo_numero = int(input("Ingresa el segundo número: ")) #solicita ingresar el segundo numero

# Realizar las operaciones #
suma = primer_numero + segundo_numero
multiplicacion = primer_numero * segundo_numero
igualdad = primer_numero == segundo_numero
menor_que = primer_numero < segundo_numero
mayor_o_igual = segundo_numero >= primer_numero

# Imprimir los resultados #
print(f"{primer_numero} + {segundo_numero} = {suma}")
print(f"{primer_numero} * {segundo_numero} = {multiplicacion}")
print(f"{primer_numero} == {segundo_numero} : {igualdad}")
print(f"{primer_numero} < {segundo_numero} : {menor_que}")
print(f"{segundo_numero} >= {primer_numero} : {mayor_o_igual}")
