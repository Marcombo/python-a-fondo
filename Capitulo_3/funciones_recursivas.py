def contar_recursivamente(elem, accumulador=0):
    if elem == 0:
        return accumulador  # caso base
    else:
        accumulador += elem
        return contar_recursivamente(elem - 1, accumulador)  # llamada recursiva


def simple_func(elem1, elem2=None):
    if elem2 is None:
        return simple_func(elem1, elem2=3)
    return elem1 * elem2


def aplanador(llst):
    lista_plana = []
    for elem in llst:
        if isinstance(elem, list):
            lista_plana.extend(aplanador(elem))
        else:
            lista_plana.append(elem)
    return lista_plana


def fibo_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibo_recursivo(n - 1) + fibo_recursivo(n - 2)


def merge_sort(lst):
    if len(lst) > 1:
        centro = len(lst) // 2  # índice de la posicion central
        izq = lst[:centro]  # lista temporal izquierda
        der = lst[centro:]  # lista temporal derecha

        merge_sort(izq)  # ordena recursivamente parte izquierda
        merge_sort(der)  # ordena recursivamente parte derecha

        i = 0  # índice de la lista izquierda
        d = 0  # índice de la lista derecha
        x = 0  # índice de la lista original

        # actualizando la lista original usando los menores
        # valores de cada lista temporal
        while i < len(izq) and d < len(der):
            if izq[i] < der[d]:
                lst[x] = izq[i]
                i += 1
            else:
                lst[x] = der[d]
                d += 1
            x += 1

        # si quedan elementos en izq o der se añaden a la
        # lista original
        while i < len(izq):
            lst[x] = izq[i]
            i += 1
            x += 1

        while d < len(der):
            lst[x] = der[d]
            d += 1
            x += 1


def merge_sort(lst):
    if len(lst) > 1:
        centro = len(lst) // 2  # índice de la posicion central
        izq = lst[:centro]  # lista temporal izquierda
        der = lst[centro:]  # lista temporal derecha
        merge_sort(izq)  # ordena recursivamente parte izquierda
        merge_sort(der)  # ordena recursivamente parte derecha

        i = 0  # índice de la lista izquierda
        d = 0  # índice de la lista derecha
        x = 0  # índice de la lista original

        # actualizando la lista original usando los menores
        # valores de cada lista temporal
        while i < len(izq) and d < len(der):
            if izq[i] < der[d]:
                lst[x] = izq[i]
                i += 1
            else:
                lst[x] = der[d]
                d += 1
            x += 1

        # si quedan elementos en izq o der se añaden a la
        # lista original
        while i < len(izq):
            lst[x] = izq[i]
            i += 1
            x += 1
        while d < len(der):
            lst[x] = der[d]
            d += 1
            x += 1


if __name__ == '__main__':
    lista_listas = [1, [2, 3, 4, 5], [1, [23, [34]], [62]]]
    lista_plana = aplanador(lista_listas)
    print(lista_plana)
