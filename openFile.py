from const import *
from datas import Data
import re

PATH_NAME = 'data/'
IN_FILE_NAME = 'netdoctora.txt'



def save_datas():
    out_file_name = input('Введите имя файла для сохранения данных: ')
    text_data.save_to_file(f'{PATH_NAME}{out_file_name}')
    code = text_data.code()
    match code:
        case 0:
            msg('Данные успешно сохранены')
        case -11:
            error_msg('Нет данных для сохранения')
        case -12:
            error_msg('Ошибка при попытке сохранения данных')
        case _:
            error_msg()

def load_and_check():
    text_data.load_text (f'{PATH_NAME}{IN_FILE_NAME}')
    if text_data.load_ok():
        txt = text_data.text()
        print()

        while (regex := input('Введите регулярное выражение:')) != '' and len(txt) > 0:
            if regex != '':
                rez = re.findall(regex, txt, re.I)
                print(rez)
                txt = ''
                for s in rez:
                    txt += f'{s}\n'
        # сохранить сформированное выражение
        text_data.set_text(txt)

    else:
        msg('Не удалось загрузить текст из файла')

# создать объект для манипулирования над данными
text_data = Data()