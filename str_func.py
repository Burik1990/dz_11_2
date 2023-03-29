def str_title():
    '''
    Все заглавные буквы
    '''
    str = input()
    return print(str.upper())


def all_title():
    '''
    Заглавные буквы в каждом слове строки
    '''
    str = input()
    str.lower()
    str.split(' ')
    return print(''.join(str.title()))
