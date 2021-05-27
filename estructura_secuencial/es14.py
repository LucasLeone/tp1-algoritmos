'''
    Ingresar por teclado un lado y
    la hipotenusa de un triángulo rectángulo,
    calcular e imprimir el lado restante,
    la superficie y los ángulos de dicho triángulo
'''
import math

# LADO1 ES LA ALTURA Y LADO RESTANTE LA BASE

lado1 = float(input('Un lado del triangulo: '))
hipotenusa = float(input('La hipotenusa del triangulo: '))

lado_restante = math.sqrt(hipotenusa**2 - lado1**2)
superficie = (lado1 * hipotenusa) / 2


