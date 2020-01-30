def iterar(number_find):
    for num in numeros:
        if num == number_find:
            return True
    return False

if __name__ == "__main__":
    numeros = [1,2,4,8,9,11,12,15,16,18,20]
    number_find = int(input('Escribe un numero a encontrar: '))
    res = iterar(number_find)
    if res:
        print('El numero si esta en la lista')
    else:
        print('El numero no esta en la lista')