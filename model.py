import view
import random

id_list = []

def init(user_list):
    global id_list
    id_list = user_list

def show_all_contacts():
    print('*СПИСОК КОНТАКОВ*')
    path = 'contacts.txt'
    with open(path, 'r', encoding = 'utf_8') as file:
        for line in file.readlines():
            print(line)

def create_new_contact():
    new_id = random.randint(1, 999)
    while new_id in id_list:
        new_id = random.randint(1, 999)
    id_list.append(new_id)
    contact_list = [new_id]
    contact_surname = view.enter_surname()
    contact_name = view.enter_name()
    contact_number = view.enter_number()
    contact_comment = view.enter_comment()

    contact_list.append(contact_surname)
    contact_list.append(contact_name)
    contact_list.append(contact_number)
    contact_list.append(contact_comment)

    print(contact_list)