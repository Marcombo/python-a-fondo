def calculo_general(**kwargs):
    ret_s = suma(**kwargs)
    ret_d = division(**kwargs)
    return ret_s * ret_d


def suma(op1, op2, **kwargs):
    return op1 + op2


def division(num, deno, **kwargs):
    return num / deno


if __name__ == '__main__':
    res = calculo_general(op1=5, op2=9, num=8, deno=2)
    print(res)
