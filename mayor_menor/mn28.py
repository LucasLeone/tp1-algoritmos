'''
    Leer tres números distintos e imprimir el mayor.
'''

num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
num3 = int(input('Ingrese el tercer número: '))
mayor = num1

while True:
    if num1 > num2 and num1 > num3:
        mayor = num1
        break
    elif num2 > num1 and num2 > num3:
        mayor = num2
        break
    elif num3 > num1 and num3 > num2:
        mayor = num3
        break
    else:
        print('Los tres números son iguales')
        quit()


print(f'El número mayor es {mayor}')