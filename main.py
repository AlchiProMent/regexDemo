from const import *
from fnew import new
from openFile import *

def run(menu_items):
    # главная функция

    def view_menu(items_menu):
        # вывод меню на экран
        print()
        for key, item in items_menu.items():
            msg(f'[{key}] - {items_menu[key][0]}')

    menu_keys_lst = []
    # получить ключ всех пунктов меню
    for key in menu_items:
        menu_keys_lst.append(key)

    view_menu(menu_items)
    while (menu_key := input('Введите код меню: ')) != EXIT_CODE:

        if menu_key in menu_keys_lst and menu_key != EXIT_CODE:
            # получить функцию
            func_name = menu_items[menu_key][1]
            func_name()
        elif (menu_key != EXIT_CODE):
            msg('Неверная команда!')
        view_menu(menu_items)

    msg('Программа закончила работу')

if __name__ == '__main__':
    run({'1':('Проверка данных',load_and_check),
         '2':('Сохранить данные',save_datas),
         EXIT_CODE:('Выход',None)})
