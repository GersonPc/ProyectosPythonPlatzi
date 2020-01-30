# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'COMPUTADORA',
    'TELEVISION',
    'ROUTER',
    'SOFA',
    'TECLADO',
    'GUATEMALA'
]

def randomword():
    idx = random.randint(0, len(WORDS) -1)
    return WORDS[idx]

def show_board(hidden_word, tries):
    print (IMAGES[tries])
    print('')
    print(hidden_word)
    print('-------------*-------------*-------------*-------------*')

def run():
    word = randomword()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        show_board(hidden_word, tries)
        current_letter = str(input('Escoje una Letra: '))
        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries += 1
            if tries == 7:
                show_board(hidden_word, tries)
                print('')
                print('¡PERDISTE! La palabra correcta es {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter
            letter_indexes = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('FELICIDADES! GANASTE! La palabra secreta es: {}'.format(word))
            break

if __name__ == '__main__':
    print('B I E N V E N I D O S   A   A H O R C A D O ')
    run()