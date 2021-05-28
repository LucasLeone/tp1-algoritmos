'''
    Hacer un programa que ingresando como datos:
        a. Kms. recorridos por un vehículo.
        b. Precio del combustible por litro.
        c. Kms. recorridos por cada litro
        
        Calcule:
            i. La cantidad de litros consumidos
            ii. Importe gastado en combustible.
            iii. Imprimir los resultados
            iv. Ejemplificar y realizar la prueba de escritorio
'''

km_recorrido = float(input('Cuantos km recorrio el vehiculo? '))
precio_combustible = float(input('Cual es el precio del combustible? '))
km_por_litro = float(input('Cuantos km recorrio por cada litro? '))

litros_consumidos = km_recorrido / km_por_litro
gastado_combustible = litros_consumidos * precio_combustible

print(f'Los litros consumidos fueron {litros_consumidos} y el gastado en combustible fue ${gastado_combustible}')