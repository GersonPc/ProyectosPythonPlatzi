import csv

class ContactBook:
    def __init__(self):
        self._contactos = []
    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contactos.append(contact)
        self._guardar()

    def mostrar_todo(self):
        for contacto in self._contactos:
            self._imprime_contacto(contacto)
    
    def _imprime_contacto(self, contacto):
        print('#------------#------------#------------#------------#')
        print('Nombre:      {}'.format(contacto.name))
        print('Telefono:    {}'.format(contacto.phone))
        print('Email:       {}'.format(contacto.email))
        print('#------------#------------#------------#------------#')

    def eliminar(self, name):
        for idx, contact in enumerate(self._contactos):
            if contact.name.lower() == name.lower():
                del self._contactos[idx]
                self._guardar()
                break
    def buscar(self, name):
        for contact in self._contactos:
            if contact.name.lower() == name.lower():
                self._imprime_contacto(contact)
                break
        else:
            self._no_encontrado()

    def _no_encontrado():
        print('###############')
        print('Contacto No Encontrado')
        print('###############')

    def actualizar(self, name):
        for contact in self._contactos:
            if contact.name.lower() == name.lower():
                self._actualizar_hoy_si(contact)
                self._guardar()
                break
        else:
            self._no_encontrado()

    def _actualizar_hoy_si(self, contacto):
        print('Ahora se te mostrara los campos en los que puedes modificar')
        print('')

        name = str(input('Escribe el nuevo nombre del contacto: '))
        phone = str(input('Escribe el nuevo telefono del contacto: '))
        email = str(input('Escribe el nuevo email del contacto: '))
        if name:
            contacto.name = name
        if phone:
            contacto.phone = phone
        if email:
            contacto.email = email

    def _guardar(self):
        with open('conta.csv', 'w') as f:
            escritor = csv.writer(f)
            escritor.writerow( ('name', 'phone', 'email') )

            for contacto in self._contactos:
                escritor.writerow((contacto.name, contacto.phone, contacto.email))

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

def run():
    agenda = ContactBook()

    with open('conta.csv', 'r') as f:
        lector = csv.reader(f)
        for idx, row in enumerate(lector):
            if idx == 0:
                continue
            agenda.add(row[0], row[1],row[2])

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el telefono del contacto: '))
            email = str(input('Escribe el email del contacto: '))
            agenda.add(name, phone,email)

        elif command == 'ac':
            name = str(input('Escribe el nombre del contacto: '))
            agenda.actualizar(name)

        elif command == 'b':
            name = str(input('Escribe el nombre del contacto: '))
            agenda.buscar(name)

        elif command == 'e':
            name = str(input('Escribe el nombre del contacto: '))
            agenda.eliminar(name)

        elif command == 'l':
            agenda.mostrar_todo()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('B I E N V E N I D O   A   L A   A G E N D A')
    run()