countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31,
    'guatemala': 18
}

while True:
    countri = str(input('Escribe el nombre de un pais: ')).lower()
    try:
        print('La poblacion de {} es de {} millones de habiatantes'.format(countri, countries[countri]))
    except KeyError:
        print('No tenemos el dato de la poblacion de {}'.format(countri))
