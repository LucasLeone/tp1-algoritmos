'''
    Leer un número positivo, calcular su cuadrado y
    su cubo. Imprimir los resultados
'''

num = float(input('Ingresa un número: '))

if num < 0:
    print('El número ingresado es negativo')
    quit()
else:
    print(f'El cuadrado de {num} es: {num**2}.')
    print(f'El cubo de {num} es: {num**3}.')
