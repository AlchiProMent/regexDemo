import const as cst
from datas import Data
import re

def save_datas():
    # сохранение данных
    out_file_name = input('Введите имя файла для сохранения данных: ')
    # сохранить данный в указанный файл
    text_data.save_to_file(f'{cst.PATH_NAME}{out_file_name}')
    # получить код результата операции
    code = text_data.code()
    # проверить этот код
    match code:
        case cst.CODE_OK:
            cst.msg('Данные успешно сохранены')
        case cst.ERR_EMPTY_TEXT:
            cst.error_msg('Нет данных для сохранения')
        case cst.ERR_FILE_OPERATION:
            cst.error_msg('Ошибка при попытке сохранения данных')
        case _:
            cst.error_msg('Неопределенная ошибка...')

def load_and_check():
    # загрузить данные из файла
    text_data.load_text (f'{cst.PATH_NAME}{cst.IN_FILE_NAME}')
    # если данные загружены успешно
    if text_data.load_ok():
        # получить массив данных для дальнейших манипуляций
        txt = text_data.text()
        print()

        # цикл ввода регулярных выражений; на каждой итерации размер данных уменьшается
        while (regex := input(f'\nВведите регулярное выражение ({cst.EXIT_CODE} - для выхода)>>> ')) != cst.EXIT_CODE and \
                len(txt) > 0:
            # если введен не код выхода
            if regex != cst.EXIT_CODE:
                # выполнить поиск по введенному регулярному выражению
                rez = re.findall(regex, txt, re.I)
                # вывести полученные результат на экран (в виде последовательности строк)
                print(*rez, sep='\n')
                # сформировать новый текст на основе предыдущей выборки (связав все элементы списка в строку с добавлением \n)
                txt = ''.join(list(map( lambda s: s+'\n', rez )))
        # сохранить сформированное выражение в контейнере (для возможного сохранения в файл)
        text_data.set_text(txt)

    else:
        cst.msg('Не удалось загрузить текст из файла')

# создать объект для манипулирования над данными
text_data = Data()