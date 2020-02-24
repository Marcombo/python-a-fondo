from typing import List, Tuple


def concat_propio(cad1: str, cad2: str) -> str:
    return cad1 + cad2


def suma_2(elem: int) -> int:
    return elem + 2


def dict_propio(elems: List[Tuple[str, int]]) -> dict:
    d = dict()
    for k, v in elems:
        d[k] = v
    return d


if __name__ == '__main__':
    print(concat_propio('Hola', ' Mundo'))
    print(concat_propio(2, 3))
    print(suma_2(5))
    print(suma_2(5.43))
    print(dict_propio([('clave1', 4), ('Clave2', 5)]))
