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

    def __init__(self, esta_encendido):
        self.esta_encendido = esta_encendido
        

    def encender(self):
        self.esta_encendido = True
        self._mostar_imagen()

    def apagar(self):
        self.esta_encendido = False
        self._mostar_imagen()
    
    def _mostar_imagen(self):
        if self.esta_encendido:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

def run():
    lampara = Lamp(esta_encendido = True)

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        '''))
        if command == 'p':
            lampara.encender()
        elif command == 'a':
            lampara.apagar()
        else:
            break

if __name__ == "__main__":
    run()