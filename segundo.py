import random
def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False       
    return True
def primos():
    number = int(input('Escribe un Numero: '))
    res = is_prime(number)
    if res is True:
        print('Tu numero es Primo')
    else:
        print('Tu numero no es Primo')
def factorial(number):
    if number== 0:
        return 1
    return number * factorial(number - 1)
def factorial_recursion():
    number = int(input('Escribe un numero: '))
    res = factorial(number)
    print(res)
def adivinarNumero():
    number_founf = False
    random_number = random.randint(0,20)

    while not number_founf:
        number = int (input('Intenta un numero: '))
        if number == random_number:
            print('Encontraste el numero!!')
            number_founf = True
        elif number > random_number:
            print ('El numero es mas pequeno')
        else:
            print('El numero es mas grande')
def palindrome(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_word = ''.join(reversed_letters)
    if reversed_word == word:
        return True
    return False
def palindrome2(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    return False
def palindromo():
    words = str(input('Escribe una palabra: '))
    word = words.upper()
    result = palindrome2(word)
    if result is True:
        print('{} Si es un palindromo'.format(word))
    else:
        print('{} No es un palindromo'.format(word))
def average_temps(temps):
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps = sum_of_temps + temps

    return sum_of_temps / len(temps)
    

def average():
    temperatura = [21,22,24,23,21,25,20,22,21]
    prom = average_temps(temperatura)
    print('La tempera promedio es $}'.format(prom))

def elije(eleccion):
    if eleccion == 1:
        primos()
    elif eleccion == 2:
        factorial_recursion()
    elif eleccion == 3:
        adivinarNumero()
    elif eleccion == 4:
        palindromo()
    elif eleccion == 5:
        average()

if __name__ == "__main__":
    print('Saber que numeros son primos = 1')
    print('La funcion factorial = 2')
    print('Adivinar un numero = 3')
    print('Verificar si palindromo = 4')
    eleccion = int(input('Elige aca: '))
    elije(eleccion)