import xml.etree.ElementTree as ET

from Capitulo_6.formato_con_delimitadores.ficheros_delimitados_csv_tsv import Planeta


def extraer_planetas_de_xml(fichero_planetas):
    planetas = []
    xml = ET.parse(fichero_planetas)
    planetas_xml = xml.findall('planeta')
    for planeta_xml in planetas_xml:
        planetas.append(extraer_planeta_de_xml(planeta_xml))
    return planetas


def extraer_planeta_de_xml(planeta_xml):
    nombre = planeta_xml.attrib['nombre']
    masa = planeta_xml.find('masa').text
    radio = planeta_xml.find('radio').text
    return Planeta(nombre, masa, radio)


def escribir_planetas(planetas, fichero_salida):
    raiz = ET.Element('sistemasolar-completo')  # raiz del arbol final
    for planeta in planetas:
        planeta_xml = ET.Element('planeta', attrib=dict(nombre=planeta.nombre))
        masa_xml = ET.Element('masa')  # agregando cada elemento de cada planeta
        masa_xml.text = str(planeta.masa)
        radio_xml = ET.Element('radio', attrib=dict(unidad='km'))
        radio_xml.text = str(planeta.radio)
        gravedad_xml = ET.Element('gravedad')
        gravedad_xml.text = str(planeta.gravedad)
        planeta_xml.extend([masa_xml, radio_xml, gravedad_xml])
        raiz.append(planeta_xml)
    arbol = ET.ElementTree(raiz)  # creando un objeto arbol para poder guardar
    arbol.write(fichero_salida)  # guardando el arbol completo en un fichero


if __name__ == "__main__":
    fichero_xml = 'planetas.xml'
    planetas = extraer_planetas_de_xml(fichero_xml)

    fichero_xml_salida = 'planetas_completos.xml'
    escribir_planetas(planetas, fichero_xml_salida)
