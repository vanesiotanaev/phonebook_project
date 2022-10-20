import view
import random

contacts_list = []

def init(user_list):
    global contacts_list
    contacts_list = user_list

def open_file_to_read():
    path = 'contacts.txt'
    return open(path, 'r', encoding= 'utf-8')

def open_file_to_add():
    path = 'contacts.txt'
    return open(path, 'a', encoding= 'utf-8')

def open_file_to_rewrite():
    path = 'contacts.txt'
    return open(path, 'w', encoding= 'utf-8')

def count_contacts():
    count = 0
    file = open_file_to_read()
    for line in file.readlines():
            count = int(line[0])
    print(count)
    return count
            
def show_all_contacts():
    print('*СПИСОК КОНТАКОВ*')
    with open_file_to_read() as file:
        for line in file.readlines():
            print(line)

def create_new_contact():
    contact_list = [str(count_contacts()+1)]
    contact_list.append(view.enter_surname())
    contact_list.append(view.enter_name())
    contact_list.append(view.enter_number())
    contact_list.append(view.enter_comment())
    contact_list.append('\n')

    return contact_list

def del_contact(id):
    contacts = file_to_list()
    with open_file_to_read() as file:
        for line in file.readlines():
            if line[0] == id:
                for item in contacts:
                    if line[0] == item[0]:
                        print(item)
                        contacts.remove(item)
                print(contacts)
    with open_file_to_rewrite() as file:
        for item in contacts:
            file.writelines(item)

def find_contact(id):
    with open_file_to_read() as file:
        for line in file.readlines():
            if line[0] == id: 
                return line

def save_new_contact_to_file(new_contact):
    new_contact_str = '; '.join(new_contact)
    path = 'contacts.txt'
    with open_file_to_add() as file:
        file.write(new_contact_str)

def file_to_list():
    with open_file_to_read() as file:
        for line in file.readlines():
            contacts_list.append(line)
    return contacts_list