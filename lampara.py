class Lamp:
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, _is_turned_on):
        self._is_turned_on = _is_turned_on

    def trun_on(self):
        self._is_turned_on = True
        self._display_image()

    def trun_off(self):
        self._is_turned_on = False
        self._display_image()

    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

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