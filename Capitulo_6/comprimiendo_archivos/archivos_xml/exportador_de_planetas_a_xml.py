from Capitulo_6.formato_con_delimitadores.ficheros_delimitados_csv_tsv import lectura_de_planetas
import xml.etree.ElementTree as ET


def planeta_en_xml(planeta):
    planeta_xml = ET.Element('planeta')
    for campo in ['nombre', 'masa', 'radio', 'gravedad']:
        campo_xml = ET.Element(campo)
        campo_xml.text = str(getattr(planeta, campo))
        planeta_xml.append(campo_xml)
    return planeta_xml


def escribir_xml(planeta):
    planeta_xml = planeta_en_xml(planeta)
    arbol = ET.ElementTree(planeta_xml)
    arbol.write(f'{planeta.nombre}.xml')


def escribir_planetas_xml(planetas):
    planetas_xml = ET.Element('planetas')
    for planeta in planetas:
        planeta_xml = planeta_en_xml(planeta)
        planetas_xml.append(planeta_xml)
    arbol = ET.ElementTree(planetas_xml)
    arbol.write('planetas.xml')


if __name__ == '__main__':
    planetas = list(lectura_de_planetas('planetas.csv'))
    for planeta in planetas:
        escribir_xml(planeta)

    escribir_planetas_xml(planetas)
