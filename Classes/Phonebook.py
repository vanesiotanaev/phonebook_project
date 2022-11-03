import Contact

class Phonebook:
    contact: list = []
    last_id: str = '0'

    def __init__(self):
        pass

    def add(self, name: str, phone: str, comment: str, id: str):
        user = Contact.Contact(self.last_id, name, phone, comment)
        self.last_id = str(int(self.last_id) + 1)
        self.contact.append(user)

book = Phonebook()
book.add('Eleonora', '123457', 'sometext', '1')
book.add('Seva', '7777', 'lalaal', '3')

print(book.contact[0].show_object())
print(book.contact[1].show_object())