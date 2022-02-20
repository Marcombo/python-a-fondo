from enum import Enum


def day_type_dict(num):
    info = {1: 'Semana', 2: 'Semana', 3: 'Semana',
            4: 'Semana', 5: 'Semana',
            6: 'Fin de Semana', 7: 'Fin de Semana'}
    return info.get(num, 'No definido')


def day_type_switch_simple(num):
    match num:
        case 1:
            return 'Semana'
        case 2:
            return 'Semana'
        case 3:
            return 'Semana'
        case 4:
            return 'Semana'
        case 5:
            return 'Semana'
        case 6:
            return 'Fin de Semana'
        case 7:
            return 'Fin de Semana'
        case _:
            return 'No definido'


def day_type_switch_pattern(num):
    match num:
        case 1:
            return 'Semana'
        case 2:
            return 'Semana'
        case 3:
            return 'Semana'
        case 4:
            return 'Semana'
        case 5:
            return 'Semana'
        case 6:
            return 'Fin de Semana'
        case 7:
            return 'Fin de Semana'
        case x:
            return f'{x} No definido'


def day_type_pro(num):
    match num:
        case _ if 1 <= num < 6:
            return 'Semana'
        case _ if num in (6, 7):
            return 'Fin de Semana'
        case x:
            return f'{x} No definido'


if __name__ == '__main__':
    print(day_type_dict(4))
    print(day_type_dict(7))
    print(day_type_dict(9))

    print(day_type_switch_simple(4))
    print(day_type_switch_simple(7))
    print(day_type_switch_simple(9))

    print(day_type_switch_pattern(4))
    print(day_type_switch_pattern(7))
    print(day_type_switch_pattern(9))

    print(day_type_pro(4))
    print(day_type_pro(7))
    print(day_type_pro(9))
