estado_semaforo=input('ingrese estado del semaforo: ')
if estado_semaforo=="verde":
    print('cruzar')
elif estado_semaforo=="rojo" or estado_semaforo=='amarillo':
    print('no cruzar')
else:
    print('escribir bien')
