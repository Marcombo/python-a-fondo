import subprocess

if __name__ == '__main__':
    salida = subprocess.check_output(['uname', '-v'])
    print(f'La información del kernel es: {salida.decode("utf-8")}')

    stdout = subprocess.check_output('pip freeze | grep python', shell=True)
    print(f'Los paquetes instalados son: \n{stdout.decode("utf-8")}')

    texto = """Python es el mejor lenguaje de programación del mundo
    Permite crear aplicaciones fácil y rápidamente, multiplataforma,
    y con soporte para diferentes tipos de aplicaciones tanto de
    escritorio como web."""
    p = subprocess.Popen(['wc'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)

    stdout, stderr = p.communicate(texto.encode('utf-8'))
    print(f'El número de líneas, palabras y bytes encontrados en el texto es de: \n{stdout.decode("utf-8")}')
