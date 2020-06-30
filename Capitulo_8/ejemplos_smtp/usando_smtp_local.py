import smtplib

if __name__ == '__main__':
    server = smtplib.SMTP('localhost', port=1025)
    server.set_debuglevel(1)
    msg = 'Cuerpo del email de ejemplo'
    direccion_emisora = 'ejemplo@example.com'
    direccion_destino = ['ejemplo_para_enviar@gmail.com']
    server.sendmail(direccion_emisora, direccion_destino, msg)
    server.quit()
