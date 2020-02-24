def calculo_posicional(*args):
    ret_s = suma(*args)
    ret_d = division(*args)
    return ret_s * ret_d


def suma(op1, op2, *args):
    return op1 + op2


def division(a1, a2, num, deno):
    return num / deno


if __name__ == '__main__':
    res = calculo_posicional(5, 9, 8, 2)
    print(res)
