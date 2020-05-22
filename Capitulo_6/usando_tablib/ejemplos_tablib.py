import tablib

if __name__ == '__main__':
    with open('planetas.csv', 'r') as fr:
        data = tablib.Dataset().load(fr)
        print(data)

    print(data[0])
    print(data.export('json'))
    print(data.export('yaml'))
    print(data.export('df'))

