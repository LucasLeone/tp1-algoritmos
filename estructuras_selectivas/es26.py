'''
    Leer tres números, si el segundo es negativo,
    calcular la raíz cuadrada de la suma de los
    restantes; en caso contrario imprimir un mensaje de error.
'''
import math

num1 = int(input('Ingrese el primero número: '))
num2 = int(input('Ingrese el segundo número: '))
num3 = int(input('Ingrese el tercer número: '))

if num2 < 0:
    print('La raiz cuadrada de la suma de los numeros restantes es:', math.sqrt(num1 + num3))
else:
    print('ERROR! El número 2 es positivo')