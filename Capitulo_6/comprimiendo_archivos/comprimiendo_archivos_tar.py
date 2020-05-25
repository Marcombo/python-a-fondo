import tarfile

if __name__ == '__main__':
    ficheros_planetas = ['Mercurio.xml', 'Venus.xml', 'Tierra.xml', 'Marte.xml', 'Jupiter.xml', 'Saturno.xml',
                         'Urano.xml', 'Neptuno.xml']
    for sufijo, flags in [('.tar', 'w'), ('.tar.gz', 'w:gz'), ('.tar.bz', 'w:bz2'), ('.tar.xz', 'w:xz')]:
        tar = tarfile.open("planetas" + sufijo, flags)
        for nombre_fichero in ficheros_planetas:
            tar.add('archivos_xml/' + nombre_fichero)
        tar.close()
