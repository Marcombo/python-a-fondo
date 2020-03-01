import timeit


def memoize(f):
    mem = {}
    def mem_func(n):
        if n not in mem:
            mem[n] = f(n)
        return mem[n]
    return mem_func


def fibo_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibo_recursivo(n - 1) + fibo_recursivo(n - 2)


if __name__ == '__main__':
    print(f"Normal 1 vez: {timeit.timeit('fibo_recursivo(32)', globals=globals(), number=1)}")
    print(f"Normal 10 veces: {timeit.timeit('fibo_recursivo(32)', globals=globals(), number=10)}")

    mem_fibo = memoize(fibo_recursivo)
    print(f"Memoized 1 vez: {timeit.timeit('mem_fibo(32)',globals=globals(), number=1)}")
    print(f"Memoized 10 veces: {timeit.timeit('mem_fibo(32)',globals=globals(), number=10)}")
    print(f"Memoized 1000 veces: {timeit.timeit('mem_fibo(32)',globals=globals(), number=1000)}")
