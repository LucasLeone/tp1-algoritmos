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

angulo1 = math.asin(lado_restante / hipotenusa)
angulo2 = 180 - (angulo1 + 90)

print(f'El lado restante es de: {lado_restante}')
print(f'El angulo que se forma con la base y la hipotenusa es de: {angulo1}')
print(f'El angulo que se forma con el lado restante y la hipotenusa es de: {angulo2}')