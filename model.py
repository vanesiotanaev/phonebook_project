def show_all_contacts():
    path = 'contacts.txt'
    with open(path, 'r', encoding = 'utf_8') as file:
        for line in file.readlines():
            print(line)


