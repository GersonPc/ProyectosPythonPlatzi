from clase_lampara import Lamp

def run():
    lamp = Lamp(_is_turned_on = False)
    print(lamp)

    while True:
        command = str(input(
            '''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        '''
        ))
        if command == 'p':
            lamp.trun_on()
        elif command == 'a':
            lamp.trun_off()
        else:
            break

if __name__ == "__main__":
    run()