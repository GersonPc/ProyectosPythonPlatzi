def run():
    contador = 0
    with open('aleph.txt', 'r') as f:
        for line in f:
            contador += line.count('Beatriz')
    print('Beatriz se encuentra {} veces en el texto'.format(contador))

if __name__ == "__main__":
    run()