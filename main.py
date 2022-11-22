# Проверка работы с регулярными выражениями
# Автор: Дмитрий Румянцев
# Москва, 2022
#

# секция импорта
from const import *
from openFile import *

def run(menu_items):
    # главная функция

    def view_menu(items_menu):
        # вывод меню на экран
        print()
        for key, item in items_menu.items():
            msg(f'[{key}] - {items_menu[key][0]}')

    menu_keys_lst = []
    # получить ключи всех пунктов меню
    for key in menu_items:
        menu_keys_lst.append(key)

    # стартовый вывод меню на экран
    view_menu(menu_items)
    # Большой цикл по пунктами меню, пока пользователь не введёт EXIT_CODE
    while (menu_key := input('Введите код меню: ')) != EXIT_CODE:

        # если пользователь ввёл верный пункт меню и не EXIT_CODE
        if menu_key in menu_keys_lst and menu_key != EXIT_CODE:
            # получить имя функции
            func_name = menu_items[menu_key][1]
            # оформить вызов функции
            func_name()
        elif (menu_key != EXIT_CODE):
            msg('Неверная команда!')

        # снова вывести меню на экран
        view_menu(menu_items)

    # сообщение в конце работы программы
    msg('\nПрограмма закончила работу.')

if __name__ == '__main__':
    # стартовая точка программы
    run({'1':('Проверка данных',load_and_check),
         '2':('Сохранить данные',save_datas),
         EXIT_CODE:('Выход',None)})
