import view

id_list = []

def init(user_list):
    global id_list
    id_list = user_list

def count_contacts():
    count = 0
    path = 'contacts.txt'
    with open(path, 'r', encoding = 'utf-8') as file:
        for line in file.readlines():
            count += 1
    return count
            
        

def show_all_contacts():
    print('*СПИСОК КОНТАКОВ*')
    path = 'contacts.txt'
    with open(path, 'r', encoding = 'utf_8') as file:
        for line in file.readlines():
            print(line)

def create_new_contact():
    id_list.append(count_contacts()+1)
    contact_list = [str(count_contacts()+1)]
    contact_list.append(view.enter_surname())
    contact_list.append(view.enter_name())
    contact_list.append(view.enter_number())
    contact_list.append(view.enter_comment())
    # contact_list.append('\n')

    return contact_list

def save_new_contact_to_file(new_contact):
    new_contact_str = '; '.join(new_contact)
    path = 'contacts.txt'
    with open(path, 'a', encoding = 'utf-8') as file:
        file.write(new_contact_str)