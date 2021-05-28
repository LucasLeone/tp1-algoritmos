'''
    Leer dos números e imprimir el mayor, suponer que son distintos.
'''

num1 = int(input('Ingrese el primer número: '))
mayor = num1
num2 = int(input('Ingrese el segundo número: '))

if num1 == num2:
    print('Son los mismos números')
    quit()

if num2 > mayor:
    mayor = num2

print(f'El número {mayor} es el mayor')