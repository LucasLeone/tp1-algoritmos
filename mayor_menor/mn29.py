'''
    Leer tres números y sumarlos, si la suma es mayor que 10,
    calcular la raíz cuadrada de la suma e imprimirla, de lo
    contrario, leer dos números más y sumarios junto a los primeros,
    luego imprimir la suma.
'''
import math

num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
num3 = int(input('Ingrese el tercer número: '))
suma = (num1 + num2 + num3)

if suma > 10:
    print('La raiz cuadrada de la suma es:', math.sqrt(suma))
else:
    num4 = int(input('Ingrese el cuarto número: '))
    num5 = int(input('Ingrese el quinto número: '))
    suma = suma + (num4 + num5)
    print(f'La suma de los 5 números es: {suma}')