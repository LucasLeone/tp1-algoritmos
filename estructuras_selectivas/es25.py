'''
    Dado un número entero positivo menor que cien, leerlo desde teclado, indicar si es primo.
    (Los números primos son aquellos que sólo son divisibles por si mismos y por uno.- En el
    caso del ejemplo, por ser el número leído menor que cien, sólo hay que comprobar que el
    número no sea 2 - 3 - 5 - 7 o múltiple de alguno de estos. Si se cumple esta condición, se trata
    entonces de un número primo.
'''

num_positive = int(input('Un número positivo menor que 100: '))
primo = False

if num_positive > 100:
    print('Ingresaste un número mayor que 100')
    quit()

for n in range(2, num_positive):
    if num_positive % n == 0:
        print(f'El número {num_positive} no es primo, {n} es el divisor')
        primo = True

if primo == False:
    print(f'El numero {num_positive} es primo')