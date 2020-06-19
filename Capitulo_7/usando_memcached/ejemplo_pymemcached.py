from pymemcache.client.base import Client

if __name__ == '__main__':
    client = Client(('localhost', 11211))
    client.set('titulo_libro', 'Python A Fondo')

    contador = client.get('contador')
    if contador is None:
        client.set('contador', 1)

    print(client.get('contador'))
    client.incr('contador', 5)
    client.incr('contador', 5)
    print(client.get('contador'))
    client.close()
