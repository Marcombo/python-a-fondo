import sys


class TupleIndexError(IndexError):
    pass


class ListIndexError(IndexError):
    pass


def get_index_value(obj, index):
    try:
        return obj[index]
    except IndexError as e:
        args, description, tb = sys.exc_info()
        if isinstance(obj, tuple):
            raise TupleIndexError(description)
        elif isinstance(obj, list):
            raise ListIndexError(description).with_traceback(tb)
        else:
            raise e


if __name__ == '__main__':
    get_index_value((1, 2, 3), 4)
    get_index_value([1, 2, 3], 4)
    get_index_value("hola", 6)
