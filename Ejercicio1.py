"""
Consigna: ✍️
Crear un pequeño programa que realice una función aritmética que permita al usuario ingresar 
datos por la terminal acorde a distintas opciones.  
Para ellos debemos definir una función que reciba parámetros:
Combinar funciones nativas y funciones definidas,
condicionales, y bucles.
Si el usuario ingresa el nro 1, realiza la acción A.
Si el usuario ingresa el nro 2, realiza la acción B.
"""

importe = 1000

tipoConsumidor = input((f"Buenos dias, indique (1) si es Consumidor Final o (2) si es Responsable Inscripto: "))
#print(tipoConsumidor)


def totalCompra(importe, tipoConsumidor):
    if tipoConsumidor == "1":
        total = importe
    else:
        total = importe * 1.21

    return print(f"El total de su compra son {total} pesos")    

totalCompra(importe, tipoConsumidor)