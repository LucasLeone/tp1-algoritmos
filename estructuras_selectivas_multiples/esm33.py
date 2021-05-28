'''
    Leer un número comprendido entre uno y siete,
    ambos inclusive e imprimir el nombre del
    día de la semana correspondiente.
'''

num = int(input('Número entre 1 y 7: '))

if num == 1:
    print('Es lunes')
elif num == 2:
    print('Es martes')
elif num == 3:
    print('Es miercoles')
elif num == 4:
    print('Es jueves')
elif num == 5:
    print('Es viernes')
elif num == 6:
    print('Es sabado')
elif num == 7:
    print('Es domingo')
else:
    print('El número no esta entre 1 y 7')