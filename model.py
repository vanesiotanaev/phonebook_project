import view

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
            count += 1
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
                    if line[0] in item:
                        print(item)
                        contacts.remove(item)
                print(contacts)
    with open_file_to_rewrite() as file:
        for item in contacts:
            file.writelines(item)


# def edit_contact():
#     id = view.contact_choice()
#     with open_file_to_read() as file:
#         for line in file.readlines():
#             if line[0] == id:
#                 print(f'Вы выбрали данный контакт: {line}')
#                 contact_list = line.split('; ')
#                 contact_list.pop(len(contact_list)-1)
#                 contact_list.pop(0)
#                 fields_list = ['1', '2', '3', '4']
#                 zipper = zip(fields_list, contact_list)
#                 contact_list = dict(zipper)
#                 print(contact_list)
#                 temp = view.which_field_to_change()
#                 if temp in fields_list:
#                     contact_list[temp] = view.new_value()
#                     print(contact_list)
#                     with open_file_to_write() as file:
#                         for line in file:
#                             if line[0] == id:
#                                 file.write(contact_list)
#                 else:
#                     view.input_error()
#             else:
#                 view.input_error()
    

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