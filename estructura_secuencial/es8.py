'''
    Leer un número e informar si es entero
'''

num = input('Ingrese un número: ')

if '.' in num:
    print(f'{num} no es número entero')
else:
    print(f'{num} es un número entero')
