# вспомогательные данные
def msg(text=''):
    # вывод простого сообщения
    print(text)

def error_msg(text=''):
    # вывод сообщения об ошибке
    print('ОШИБКА!')
    print(text)

# код выхода из меню
EXIT_CODE = '0'

# имя файла, из которого берутся данные
PATH_NAME = 'data/'
IN_FILE_NAME = 'netdoctora.txt'

# коды при работе с файлами
CODE_OK = 0
ERR_FILE_NOT_FOUNT = -1
ERR_OS = -2
ERR_DECODE = -3
ERR_EMPTY_TEXT = 1
ERR_FILE_OPERATION = -12
