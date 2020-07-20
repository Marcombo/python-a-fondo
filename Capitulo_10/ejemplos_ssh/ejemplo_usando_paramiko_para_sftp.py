import os

import paramiko

if __name__ == '__main__':
    cliente = paramiko.client.SSHClient()
    cliente.load_system_host_keys()
    cliente.connect('192.168.1.148', username='ubuntu', password='pass')
    sftp = cliente.open_sftp()
    sftp.chdir('/tmp')
    print(sftp.listdir())
    with sftp.open('fichero_de_prueba.txt', 'w') as fw:
        fw.write('Escribiendo en el fichero ubicado en el servidor')

    path_local = os.path.join(os.getcwd(), 'fichero_importado.txt')
    sftp.get('/tmp/fichero_de_prueba.txt', path_local)

    with open(path_local, 'r') as fr:
        print(f'Contenido del fichero importado: {fr.read()}')

    with open('fichero_de_prueba_local.txt', 'w') as fw:
        fw.write('Fichero creado en local')

    sftp.put('fichero_de_prueba_local.txt', '/tmp/fichero_enviado.txt')
    ret = cliente.exec_command('cat /tmp/fichero_enviado.txt')
    print(f'Contenido en el servidor del fichero enviado: {ret[1].read().decode()}')
    sftp.close()
    cliente.close()