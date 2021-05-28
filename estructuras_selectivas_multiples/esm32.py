'''
    Se leen el sueldo básico y la categoría de un empleado. Para calcular el sueldo neto se
    efectúan los siguientes descuentos:

        Categoría 1: 30%
        Categoría 2: 25%
        Categoría 3: 25%
        Categoría 4: 10%

    Para otras Categorías no hay descuentos. Imprimir el sueldo neto básico y Categoría.-
'''

sueldo_basico = float(input('Cual es el sueldo basico? $'))
categoria = int(input('A que categoria pertenece? '))
sueldo_neto = 0

if categoria == 1:
    sueldo_neto = sueldo_basico - (30 * 100 / sueldo_basico)
elif categoria == 2:
    sueldo_neto = sueldo_basico - (25 * 100 / sueldo_basico)
elif categoria == 3:
    sueldo_neto = sueldo_basico - (25 * 100 / sueldo_basico)
elif categoria == 4:
    sueldo_neto = sueldo_basico - (10 * 100 / sueldo_basico)
else:
    sueldo_neto = sueldo_basico

print(f'El sueldo neto es ${sueldo_neto} y pertenece a la categoria {categoria}')