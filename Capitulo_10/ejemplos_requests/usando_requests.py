import requests

if __name__ == '__main__':
    response = requests.get('http://www.google.es')
    print(f'Código de estado: {response.status_code}')
    print(f'Url pedida: {response.url}')
    print(f'Texto de respuesta: {response.text[:100]}')

    response = requests.get('http://www.google.es/search', params=dict(q='Python a fondo'))
    print(f'Código de estado: {response.status_code}')
    print(f'Url pedida: {response.url}')
    print(f'Texto de respuesta: {response.text[:100]}')


