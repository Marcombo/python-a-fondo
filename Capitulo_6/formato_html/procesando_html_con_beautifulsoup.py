from bs4 import BeautifulSoup, Tag


def calc_gravedad(masa, radio):
    g_constante = 6.673e-11
    return g_constante * float(masa) / (float(radio) ** 2)


if __name__ == '__main__':
    with open('planetas.html', 'r') as fs:
        cadena_html = fs.read()

    html = BeautifulSoup(cadena_html, 'html.parser')
    print(html.title.text)
    print(html.body.find_all('h2'))

    # Agregando la gravedad de cada planeta a su nodo
    planetas = html.find_all('div', class_='planeta')
    for planeta in planetas:
        masa = planeta.select_one('.masa').text  # forma simple de encontrar nodos hijos usando selectores CSS

        # forma compleja de encontrar el radio radio iterando por los hijos
        radios = [x for x in planeta.children if isinstance(x, Tag) and ['radio'] == x.attrs.get('class')]
        radio = radios[0].text

        gravedad = calc_gravedad(masa, radio)  # calculo de la gravedad
        gravedad_tag = html.new_tag(name='div', attrs={'class': 'gravedad'})  # creacion de nueva etiqueta
        gravedad_tag.string = str(gravedad)

        planeta.append(gravedad_tag)  # agregando la gravedad al planeta

    # Guardando el nuevo documento
    nombre_salida = 'planetas_con_gravedad.html'
    with open(nombre_salida, 'w') as fw:
        fw.write(html.prettify())
