#Solicitar Información

nombre = input("Ingrese el Nombre del Cliente: ")
valor_compra = float(input("Ingrese el valor de la compra: "))

#Establecemos los Condicionales

if valor_compra < 80:
    print(f'Hola, {nombre}. El valor a pagar es: ${valor_compra}')
elif 80 <= valor_compra <= 150:
    descuento = 0.1
elif 150 <= valor_compra <= 300:
    descuento = 0.15
elif 300 <= valor_compra <= 500:
    descuento = 0.2
else:
    descuento = 0

#formula del precio final: precio_final = valor_compra - (valor_compra*descuento)
precio_final = valor_compra - (valor_compra*descuento)

#imprimimos los resultados
print(f'Hola, {nombre}.')
print(f'La compra sin descuento: ${valor_compra: .2f}')
print(f'Compra con descuento: ${precio_final: .2f}')