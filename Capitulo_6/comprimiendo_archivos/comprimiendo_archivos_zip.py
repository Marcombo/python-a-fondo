import zipfile

if __name__ == '__main__':
    ficheros_planetas = ['Mercurio.xml', 'Venus.xml', 'Tierra.xml', 'Marte.xml', 'Jupiter.xml', 'Saturno.xml',
                         'Urano.xml', 'Neptuno.xml']
    nombre_zip = 'zip_planetas_separados.zip'
    fichero_zip = zipfile.ZipFile(nombre_zip, mode='w')
    for nombre_fichero_xml in ficheros_planetas:
        fichero_zip.write('archivos_xml/' + nombre_fichero_xml, arcname=nombre_fichero_xml)
    fichero_zip.close()

    zip_leido = zipfile.ZipFile(nombre_zip, mode='r')
    print(zip_leido.namelist())
    print(zip_leido.infolist())

    neptuno = zip_leido.getinfo('Neptuno.xml')
    print(neptuno)
    print(zip_leido.extract('Neptuno.xml', 'Neptuno_extraido'))

    nombre_zip = 'zip_planetas_unico_fichero.zip'
    fichero_zip = zipfile.ZipFile(nombre_zip, mode='w')
    fichero_zip.write('archivos_xml/' + 'planetas.xml', 'planetas.xml')
    fichero_zip.close()
