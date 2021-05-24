'''
    Si un lote de terreno tiene X metros de frente
    por Y metros de fondo: calcular e imprimir la
    cantidad da metros de alambre para cercarlo. 
    (X e Y serán leídos al comenzar el programa).
'''

x = float(input('Cuantos metros de frente tiene el terreno? '))
y = float(input('Cuantos metros de fondo tiene el terreno? '))
total = (x*2 + y*2)

print('La cantidad de metros de alambre que se va a necesitar es: ', total)