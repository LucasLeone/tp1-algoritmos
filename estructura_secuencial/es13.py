'''
    Dadas la base y la altura da un triángulo,
    calcular la superficie. También conociendo uno de
    sus ángulos calcular los otros dos lados.

    EL TRIANGULO ES RECTANGULO
'''
import math

base = float(input('La base del triangulo: '))
altura = float(input('La altura del triangulo: '))
angulo = float(input('El angulo del triangulo: '))

superficie = (base * altura) / 2
hipotenusa = base/math.cos(angulo)
catOpuesto = hipotenusa * math.sin(angulo)

print(f'La superficie del triangulo es: {superficie}')
print(f'Los lados restante del triangulo son: {hipotenusa} y {catOpuesto}')
