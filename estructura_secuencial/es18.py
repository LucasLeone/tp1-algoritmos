'''
    Calcular la velocidad de un móvil que se desplaza
    con velocidad constante conociendo el espacio recorrido
    y el tiempo empleado en recorrerle (los datos serán leídos
    al comenzar el programa)
'''

distancia = float(input('Cual es la distancia recorrida en kilometros? '))
tiempo = float(input('Cual es el tiempo empleado en horas? '))

velocidad = distancia / tiempo

print(f'La velocidad fue {velocidad} km/h')