'''
    Dado un vehículo de cuatro ruedas;
    cada una con un radio de cincuenta
    centímetros, calcular e imprimir 
    cuántas vueltas dará cada rueda 
    para desplazarse un kilómetro
'''
import math

rueda = 0.5
radio = rueda

una_vuelta = (2 * math.pi) * radio

resultado = 1000 * (1 / una_vuelta)

print(f'La rueda da un total de {resultado} vueltas')