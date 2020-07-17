def aplicar_funcion_str():
    n_caracteres = input('Texto: ')
    fun = input('Función a aplicar: ')
    return getattr(str, fun)(n_caracteres)

if __name__ == '__main__':
    print(aplicar_funcion_str())
