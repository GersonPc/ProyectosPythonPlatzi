def imprimirTabla(num,rang):
    print('La tabla del numero {} es:'.format(num))
    for i in range(rang):
        if i > 0:
            res = i * num
            print(' {}  X  {}  =  {}'.format(i,num,res))
        

if __name__ == "__main__":
    print('T A B L A   D E   M U L T I P L I C A R')
    numTabla = int(input('Escribe un numero: '))
    rangeTable = int(input('Ahora pon el rango de la tabla '))
    rangeTable = rangeTable + 1
    print('')
    imprimirTabla(numTabla,rangeTable)

# >>> string[1:5]
# 'latz'
# >>> string[1:6]
# 'latzi'
# >>> string[1:6:2]
# 'lti'
# >>> string[0:6:2]
# 'paz'
# >>> string[::2]
# 'paz'
# >>> string[::-1]
# 'iztalp'
