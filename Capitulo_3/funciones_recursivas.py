def contar_recursivamente(elem, acumulador=0):
    if elem == 0:
        return acumulador  # caso base
    else:
        acumulador += elem
        return contar_recursivamente(elem - 1, acumulador)  # llamada recursiva


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
        centro = len(lst) // 2  # Indice de la posicion central
        mitad_izq = lst[:centro]  # Lista temporal izquierda
        mitad_der = lst[centro:]  # Lista temporal derecha

        merge_sort(mitad_izq)  # Ordena recursivamente parte izquierda
        merge_sort(mitad_der)  # Ordena recursivamente parte derecha

        i = 0  # Indice de la lista izquierda
        d = 0  # Indice de la lista derecha
        x = 0  # Indice de la lista original

        # Actualizando la lista original usando los menores
        # valores de cada lista temporal
        while i < len(mitad_izq) and d < len(mitad_der):
            if mitad_izq[i] < mitad_der[d]:
                lst[x] = mitad_izq[i]
                i += 1
            else:
                lst[x] = mitad_der[d]
                d += 1
            x += 1

        # Si quedan elementos en izq o der se añaden a la
        # lista original
        while i < len(mitad_izq):
            lst[x] = mitad_izq[i]
            i += 1
            x += 1

        while d < len(mitad_der):
            lst[x] = mitad_der[d]
            d += 1
            x += 1


if __name__ == '__main__':
    lista_listas = [1, [2, 3, 4, 5], [1, [23, [34]], [62]]]
    lista_plana = aplanador(lista_listas)
    print(lista_plana)

    lista = [3, 6, 3, 1, 2, 4, 3]
    print(f'Lista inicial: {lista}')
    merge_sort(lista)
    print(f'Lista ordenada: {lista}')
