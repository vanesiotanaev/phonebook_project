import view
import model

def button_click():
    menu_choice = view.menu_command()
    while menu_choice <= 0 or menu_choice > 7:
        view.input_error()
        menu_choice = view.menu_command()
    if menu_choice == '1':
        model.show_all_contacts()
