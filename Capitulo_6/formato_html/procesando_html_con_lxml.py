from lxml import etree


class HTMLParserPropio(object):
    def start(self, tag, attrib):
        print(f"Comienzo de etiqueta: {tag}")

    def end(self, tag):
        print(f"Fin de etiqueta: {tag}")

    def data(self, data):
        info = data.strip()
        if info:
            print(f"Contenido: {info}")

    def comment(self, text):
        print(f"Comentario {text}")

    def close(self):
        print("Cerrando")
        return "Cerrado!"


if __name__ == '__main__':
    with open('planetas.html', 'r') as fs:
        cadena_html = fs.read()
    html = etree.HTML(cadena_html)
    result = etree.tostring(html, pretty_print=True, method="html")
    print(result.decode())

    parser = etree.XMLPullParser(target=HTMLParserPropio())
    parser.feed(cadena_html)

    parse = etree.fromstring(cadena_html)
    nombre_planetas = parse.xpath('//div[@class="planeta"]/h2')
    for nombre in nombre_planetas:
        print(nombre.text)

    pie_pagina = parse.xpath('//footer')
    radios = parse.xpath('//div[@class="radio"]')
