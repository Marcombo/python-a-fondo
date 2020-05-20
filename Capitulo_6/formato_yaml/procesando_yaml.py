import yaml

from Capitulo_6.formato_con_delimitadores.ficheros_delimitados_csv_tsv import Planeta


class PlanetaYaml(Planeta, yaml.YAMLObject):
    yaml_tag = '!Planeta'

    def __init__(self, nombre, masa, radio):
        super(PlanetaYaml, self).__init__(nombre, masa, radio)
        self.__dict__['gravedad'] = self.gravedad


if __name__ == '__main__':
    planetas = []
    planetas.append(PlanetaYaml(nombre='Mercurio', masa=3.303e+23, radio=2439700.0))
    planetas.append(PlanetaYaml(nombre='Venus', masa=4.869e+24, radio=6051000.0))
    planetas.append(PlanetaYaml(nombre='Tierra', masa=5.976e+24, radio=6378140.0))
    with open('planetas_con_gravedad.yaml', 'w') as fw:
        yaml.dump(planetas, fw)
