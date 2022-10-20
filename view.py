def menu_command():
    return int(input('*ГЛАВНОЕ МЕНЮ* \
            \n1. Показать все контакты \
            \n2. Открыть файл с контактами \
            \n3. Записать файл с контактами \
            \n4. Добавить контакт \
            \n5. Изменить контакт \
            \n6. Удалить контакт \
            \n7. Поиск по контактам \
            \nВыберите действие (1-7): '))

def enter_surname():
    return str(input('Введите фамилию нового контакта: '))

def enter_name():
    return str(input('Введите имя нового контакта: '))

def enter_number():
    return str(input('Введите номер нового контакта: '))

def enter_comment():
    return str(input('Введите комментарий: '))

def contact_choice():
    return str(input('Введите ID контакта: '))

def which_field_to_change():
    return str(input('Выберите поле, которое необходимо изменить (1-4):\
                    \n1. Фамилия\
                    \n2. Имя\
                    \n3. Номер телефона\
                    \n4. Комментарий'))

def input_error():
    print('Ошибка ввода!')