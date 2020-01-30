def proteccion(func):

    def envuelto(password):
        if password == 'hola':
            return func()
        else:
            print('Tu contraseña es incorrecta')

    return envuelto

@proteccion
def funcion_protegida():
    print('Tu contraseña es Correcta')

if __name__ == "__main__":
    password = str(input('Ingresa tu contraseña: '))

    funcion_protegida(password)