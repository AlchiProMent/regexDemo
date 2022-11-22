from const import *
from os import path

class Data:
    __text_array = ''
    __load_ok = False
    __code = 0
    def __init__(self, txt='', file_name=''):
        self.__text_array = txt
        if file_name != '':
            self.load_text(file_name)

    def text(self):
        # вернуть текст
        return self.__text_array

    def text_prn(self):
        # вывести текст на экран
        print(self.__text_array)

    def load_text(self,file_name):
        # загрузить текст из файла

        if path.exists(file_name):
            # если файл найден на диске
            self.__load_ok = False
            self.__text_array = ''

            try:
                # прочитать его
                with open(file_name, encoding='utf-8') as f:
                    self.__text_array = f.read()
            except FileNotFoundError:
                self.__code = -1
            except OSError:
                self.__code = -2
            except UnicodeDecodeError:
                self.__code = -3
            else:
                self.__load_ok = True
                self.__code = 0

        else:
            self.__load_ok = False
            self.__code = -9

    def save_to_file(self,file_name):
        if len(self.__text_array) > 0:
            try:
                with open(file_name,'w') as f:
                    f.write(self.__text_array)
            except:
                self.__code = -12
            else:
                self.__code = 0
        else:
            self.__code = -11

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

