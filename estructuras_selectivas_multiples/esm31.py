'''
    Leer tres números, si el primero es uno, sumar el segundo y el tercero; si es dos.
    multiplicarlos, si es tres, dividirlos, si es cuatro, la raíz cuadrada de la suma de sus cuadrados
    y cualquier otro valor indicar que se trata de un error
'''
import math

num1 = int(input('Ingrese el primero número: '))
num2 = int(input('Ingrese el segundo número: '))
num3 = int(input('Ingrese el tercer número: '))

if num1 == 1:
    print(num2 + num3)
elif num1 == 2:
    print(num2 * num3)
elif num1 == 3:
    print(num2 / num3)
elif num1 == 4:
    print(math.sqrt(num2**2 + num3**2))
else:
    print('VALOR ERRONEO!')