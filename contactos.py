import csv

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self._contacts = []
    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)
    
    def _print_contact(self,contact):
        print('---#---#---#---#---#---#---#---#')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('---#---#---#---#---#---#---#---#')

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for conta in self._contacts:
            if conta.name.lower() == name.lower():
                self._print_contact(conta)
                break
        else:
            self._not_found()
    
    def _not_found(self):
        print('#############')
        print('No encontrado!')
        print('#############')

    def actualizar(self, name):
        for conta in self._contacts:
            if conta.name.lower() == name.lower():
                conta.name = str(input('Ingresa el nuevo nombre del contacto: '))
                conta.phone = str(input('Ingresa el nuevo telefono del contacto: '))
                conta.email = str(input('Ingresa el nuevo email del contacto: '))
                self._save()
                break
        else:
            self._not_found()

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone', 'email') )
            for conta in self._contacts:
                writer.writerow((conta.name, conta.phone, conta.email))


def run():

    contacto = ContactBook()
    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            contacto.add(row[0],row[1],row[2])

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
            contacto.add(name, phone, email)

        elif command == 'ac':
            name = str(input('Escribe el nombre del contacto: '))
            contacto.actualizar(name)

        elif command == 'b':
            name = str(input('Escribe el nombre del contacto: '))
            contacto.search(name)

        elif command == 'e':
            name = str(input('Escribe el nombre del contacto: '))
            contacto.delete(name)

        elif command == 'l':
            contacto.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('B I E N V E N I D O   A   L A   A G E N D A')
    run()