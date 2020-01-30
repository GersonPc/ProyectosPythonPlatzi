def average_temps(temps):
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps = sum_of_temps + temp

    return sum_of_temps / len(temps)
    

def average():
    temperatura = [21,22,24,23,21,25,20,22,21]
    prom = average_temps(temperatura)
    print('La tempera promedio es {}'.format(prom)

def eleccion(elc):
    if elc == 1:
        average()
    elif elc == 2:
        pass

if __name__ == "__main__":
    print('asdfasdfasdfasdfsdf')
    elc = int(input('Escribe aca: '))
    eleccion(elc)