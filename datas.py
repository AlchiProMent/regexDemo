from const import *
from os import path

class Data:
    # класс для работы с данными из файла
    __text_array = ''       # текстовый массив
    __load_ok = False       # загрузка данных прошла успешно?
    __code = CODE_OK        # код операции

    def __init__(self, txt='', file_name=''):
        # инициализация
        self.__text_array = txt
        # если передано имя файла, сразу загрузить данные
        if file_name != '':
            self.load_text(file_name)

    def text(self):
        # вернуть текстовый массив
        return self.__text_array

    def text_prn(self):
        # вывести текст на экран
        print(self.__text_array)

    def load_text(self,file_name):
        # загрузить текст из файла

        # если файл найден на диске
        if path.exists(file_name):

            self.__load_ok = False
            self.__text_array = ''

            try:
                with open(file_name, encoding='utf-8') as f:
                    # прочитать файла
                    self.__text_array = f.read()
            except FileNotFoundError:       # файл не найден (излишняя проверка после path.exists)
                self.__code = ERR_FILE_NOT_FOUNT
            except OSError:                 # общая ошибка работы с файлом
                self.__code = ERR_OS
            except UnicodeDecodeError:      # ошибка декодирования
                self.__code = ERR_DECODE
            else:
                # файл прочитан успешно
                self.__load_ok = True
                self.__code = CODE_OK

        else:
            # файла нет на диске
            self.__load_ok = False
            self.__code = ERR_FILE_NOT_FOUNT

    def save_to_file(self,file_name):
        if len(self.__text_array) > 0:
            try:
                with open(file_name,'w') as f:
                    f.write(self.__text_array)
            except:
                self.__code = ERR_FILE_OPERATION
            else:
                self.__code = CODE_OK
        else:
            self.__code = ERR_EMPTY_TEXT

    def load_ok(self):
        # информация об успехе/недуаче загрузки
        return self.__load_ok

    def set_text(self, txt=''):
        # установить текст
        self.__text_array = txt

    def code(self):
        return self.__code

    def clear(self):
        # очистить текст
        self.__text_array = ''

