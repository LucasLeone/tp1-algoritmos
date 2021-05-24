'''
    Leer tres números, calcular e imprimir los seis posibles cocientes.
'''

num1 = float(input('Ingresa el primer valor: '))
num2 = float(input('Ingresa el segundo valor: '))
num3 = float(input('Ingresa el tercer valor: '))

print(f'Los seis posibles cocientes entre {num1}, {num2}, {num3} son:')
print(num1/num2, num1/num3, num2/num1, num2/num3, num3/num1, num3/num2)