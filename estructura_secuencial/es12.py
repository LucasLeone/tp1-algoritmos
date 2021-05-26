'''
    Teniendo como dato la hipotenusa y 
    el ángulo que forma ésta con la base
    de un triángulo rectángulo. calcular
    e imprimir los datos y ángulos restantes.
'''
import math


hipotenusa = float(input('El valor de la hipotenusa: '))
angulo = float(input('El valor del angulo: '))

if angulo > 90:
    print('El angulo no puede ser mayor a 90°')

angulo_restante = 180 - (angulo + 90)
print(f'El angulo restante es de {angulo_restante}°')

lado_base = hipotenusa * math.cos(angulo)
lado_restante = hipotenusa * math.sin(angulo)
print(f'El lado de la base es de {lado_base} y el otro lado es de {lado_restante}')