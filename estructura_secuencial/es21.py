'''
    Ingresar por teclado los precios correspondientes
    a cinco artículos y las cantidades vendidas de cada
    uno de ellos. Calcular e imprimir el importe total
    de ventas de cada uno y un importe total de lo vendido.
'''

precio_art1 = float(input('Cual es el precio del articulo 1? '))
cant_art1 = int(input('Y la cantidad vendida del articulo 1? '))
total_art1 = precio_art1 * cant_art1


precio_art2 = float(input('Cual es el precio del articulo 2? '))
cant_art2 = int(input('Y la cantidad vendida del articulo 2? '))
total_art2 = precio_art2 * cant_art2


precio_art3 = float(input('Cual es el precio del articulo 3? '))
cant_art3 = int(input('Y la cantidad vendida del articulo 3? '))
total_art3 = precio_art3 * cant_art3


precio_art4 = float(input('Cual es el precio del articulo 4? '))
cant_art4 = int(input('Y la cantidad vendida del articulo 4? '))
total_art4 = precio_art4 * cant_art4


precio_art5 = float(input('Cual es el precio del articulo 5? '))
cant_art5 = int(input('Y la cantidad vendida del articulo 5? '))
total_art5 = precio_art5 * cant_art5

total_ventas = total_art1 + total_art2 + total_art3 + total_art4 + total_art5

print(f'''
    Los importes totales de cada venta fueron:
        Articulo 1: ${total_art1},
        Articulo 2: ${total_art2},
        Articulo 3: ${total_art3},
        Articulo 4: ${total_art4},
        Articulo 5: ${total_art5}

    Y el total de las ventas fue: ${total_ventas}
''')