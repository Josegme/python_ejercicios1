#Calculadora de indice de masa corporal

contador = 0

print("CALCULADORA DE INDICE DE MASA CORPORAL (IMC) \n")
while contador != 2: 
    contador = int(input("¿Quieres seguir calculando el IMC? 1.SI 2.No \n"))

    if contador == 1: #el usuario quiere calcular el IMC
        estatura = float(input("Ingrese su estatura en mts: "))
        peso = float(input("Ingrese su peso en Kilogramos: "))
        resultado = round(peso/(estatura**2), 2)

        if resultado < 18.5:
            print(f'IMC {resultado} = BAJO DE PESO.')
        elif 18.5 < resultado < 24.99:
            print(f'IMC {resultado} = PESO NORMAL')
        elif 25 < resultado < 30:
            print(f'IMC {resultado} = SOBREPESO')
        elif resultado > 30:
            print(f'IMC {resultado} = OBESIDAD')
    elif contador == 2:
        print("Hasta pronto.")  

print("Gracias por utilizar la calculadora de IMC")      