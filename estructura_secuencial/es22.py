'''
    Leer desde el teclado un valor que corresponda
    a la distancia entre dos puntos expresada en
    mts. y transformarla en Cms., Imprimirla.
'''

distancia_dmts = float(input('La distancia entre 2 puntos en mts.: '))

distancia_cm = distancia_dmts * 100

print(f'La distancia entre esos 2 puntos es {distancia_cm} cm')