'''
    Sabiendo el perímetro de un
    círculo calcular su radio
'''
import math


perimetro = float(input('Cual es el perimetro del circulo? '))

radio = perimetro / (2 * math.pi)

print(f'El radio del circulo es {radio}')