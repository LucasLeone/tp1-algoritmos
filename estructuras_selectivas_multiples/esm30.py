'''
    En un comercio se venden tres modelos de frascos codificados uno, dos y tres.
    Ingresando un código, se quiere imprimir la descripción según detalle:
        1 -chico.
        2- mediano.
        3- grande
'''

print('''
    Los codigos de los frascos son: 
    [1] chico
    [2] mediano
    [3] grande
''')

frasco_chico = 1
frasco_mediano = 2
frasco_grande = 3

codigo = int(input('Ingrese el codigo: '))

if codigo == 1:
    print('Frasco chico')
elif codigo == 2:
    print('Frasco mediano')
elif codigo == 3:
    print('Frasco grande')
else:
    print('Codigo incorrecto')