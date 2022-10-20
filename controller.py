import view
import model

def button_click():
    menu_choice = view.menu_command()
    while menu_choice <= 0 or menu_choice > 7:
        view.input_error()
        menu_choice = view.menu_command()
    if menu_choice == 1:
        model.show_all_contacts()
    if menu_choice == 4:
        model.save_new_contact_to_file(model.create_new_contact())
    if menu_choice == 5:
        model.edit_contact()
    if menu_choice == 6:
        model.del_contact(view.contact_choice())
