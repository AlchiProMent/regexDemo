from const import *

def new():
    try:
        n = 100*0

        try:
            n = 100**10
        except:
            error_msg('Многовато будет')
        else:
            msg('Обошлось')

    except ZeroDivisionError:
        error_msg('Деление на ноль!')
    except AttributeError:
        error_msg('Ошибка атрибута!')
    else:
        msg(n)
    finally:
        msg('Всё завершилось')
