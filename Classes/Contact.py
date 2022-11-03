class Contact:
# Обозначаем поля (аттрибуты), которые нужны каждому Контакту. 
# Будем считать, что эти аттрибуты обязательные.
# Аттрибуты, грубо говоря, переменные, отвечающие за объект Класса.
    id: str
    name: str
    phone: str
    comment: str
# Конструктор.
# В нем указываем, какие параметры обязательны при создании объекта данного Класса.
    def __init__(self, id: str, name: str, phone: str, comment: str, *args, **kwargs):
        # self означает, что метод __init__ будет работать не с чем-то абстрактным, а 
        # с конкретными созданными объектами. Т.е. вместо self можно поставить имя любого объекта.
        self.id = id
        self.name = name
        self.phone = phone
        self.comment = comment
# Объект Класса Contact создали.
# Чтобы видеть, какой именно объект мы создали, нужно сделать метод. 
    def show_object(self):
        return (self.id, self.name, self.phone, self.comment)

    def set_name(self, name: str):
        self.name = name


# Создали объект класса
ivan = Contact('1', 'Ivan', '+79277351233', 'Work')
# Поняли, что объект есть, на него выделена память
print(ivan)
# Напечатали в нормальном виде объект
print(ivan.show_object())
# При этом можно добавить в существующий объект класса аттрибут, которого не было 
# у данного объекта.
ivan.second_phone = '123456789' 
print(ivan.second_phone)
# Но лучше сразу обозначать. Это, скорее, исключение.
# Потому что, как минимум, если вызвать метод show_object() для объекта ivan,
# аттрибут second_phone не отобразится в нашем кортеже, ведь в методе не 
# написано, что нужно отображать и это поле тоже. 

# Здесь используем метод класса Контакт, применяем его к объекту ivan. А конкретнее к аттрибуту name
# объекта ivan.
print(ivan.show_object())
ivan.set_name('IVAN')
print(ivan.show_object())