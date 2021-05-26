'''
    Dados dos lados de un triángulo,
    calcular la hipotenusa mediante Pitágoras.
'''
import math


lado1 = float(input('El lado de un triangulo: '))
lado2 = float(input('Otro lado del triangulo: '))

hipotenusa = (lado1**2) + (lado2**2)
hipotenusa = math.sqrt(hipotenusa)

print(f'La hipotenusa del triangulo con los lados {lado1} y {lado2} es: {hipotenusa}')