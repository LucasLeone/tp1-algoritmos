'''
    Un pintor sabe que con una pintura determinada puede
    pintar 3,6 metros cuadrados por cada medio litro. 
    Sabiendo la altura y el largo de la pared a pintar, 
    informar cuántos litros de pintura utilizará. 
    (Altura y Largo en metros)
'''

litro_pintura = 7.2 # Cada medio litro de pintura se pinta 3.6 metros cuadrados, por lo tanto, un litro seran 7.2 m2

altura = float(input('Altura de la pared en metros: '))
largo = float(input('Largo de la pared en metros: '))

pared = altura * largo

print('La cantidad de litros de pintura que se va a utilizar seran: ', pared / litro_pintura)