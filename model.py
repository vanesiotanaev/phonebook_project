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
    return count
            
def show_all_contacts():
    print()
    print('*СПИСОК КОНТАКОВ*')
    print()
    with open_file_to_read() as file:
        for line in file.readlines():
            line = line.split('|')
            print(f'ID: {line[0]} \
                    \nSurname: {line[1]}; Name: {line[2]}; Number: {line[3]}; Comment: {line[4]}')

def create_new_contact():
    contact_list = [str(count_contacts()+1)]
    contact_list.append(view.enter_surname())
    contact_list.append(view.enter_name())
    contact_list.append(view.enter_number())
    contact_list.append(view.enter_comment())
    # contact_list.append('\n')

    return contact_list

def del_contact(id):
    contacts = file_to_list()
    with open_file_to_read() as file:
        for line in file.readlines():
            if line[0] == id:
                for item in contacts:
                    if line[0] == item[0]:
                        contacts.remove(item)
    with open_file_to_rewrite() as file:
        for item in contacts:
            file.writelines(item)

def edit_contact(id):
    contacts = file_to_list()
    print(contacts)
    for i in range(len(contacts)):
        contacts[i] = contacts[i].split('|')
    print(contacts)
    for j in range(len(contacts)):
        if contacts[j][0] == id:
            print(contacts[j])
            field = int(view.which_field_to_change())
            contacts[j][field] = view.new_value()
            print(contacts[j])
    print(contacts)

    # contacts = file_to_list()
    # for item in contacts:
    #     if id == item[0]:
    #         view.print_line(item)
    #         item = item.split('|')
    #         index = int(view.which_field_to_change())
    #         print(item[index])
    #         item[index] = view.new_value()
    #         contacts_list.append(item)
    #     else:
    #         contacts_list.append(item)
    #     print(contacts_list)


def find_contact(id):
    with open_file_to_read() as file:
        for line in file.readlines():
            if line[0] == id: 
                return line

def save_new_contact_to_file(new_contact):
    new_contact_str = '|'.join(new_contact)
    with open_file_to_add() as file:
        file.write(new_contact_str + '\n')

def file_to_list():
    with open_file_to_read() as file:
        for line in file.readlines():
            contacts_list.append(line)
    return contacts_list