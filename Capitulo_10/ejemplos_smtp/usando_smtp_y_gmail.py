import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

if __name__ == '__main__':
    email_emisor = "email_emisor@gmail.com"
    email_receptor = "email_receptor@gmail.com"
    password = "password"

    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = "Probando el envio de emails en formato html"
    mensaje["From"] = email_emisor
    mensaje["To"] = email_receptor

    texto = """Queri@ Pythonista {nombre},
    Encuentra la mejor información sobre Python en www.elpythonista.com
    Ejemplo basado en los ejemplos del libro Python a Fondo.
    """

    html = """\
    <html>
      <body>
        <p>Querid@ Pythonista {nombre},<br><br>
           Encuentra la mejor información sobre Python en <a href="www.elpythonista.com">El Pythonista</a><br><br>
           Ejemplo basado en los ejemplos del libro <b>Python a Fondo</b>
        </p>
      </body>
    </html>
    """

    for nombre in ['Juan', 'Maria', 'Pedro']:
        # Creando las partes de texto y html para el email
        mensaje_texto = MIMEText(texto.format(nombre=nombre), "plain")
        mensaje_html = MIMEText(html.format(nombre=nombre), "html")

        # Agregando el contenido al mensaje multipart
        mensaje.attach(mensaje_texto)
        mensaje.attach(mensaje_html)

        # Crea una conexión segura para el envío de emails
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as servidor:
            servidor.login(email_emisor, password)
            servidor.sendmail(email_emisor, email_receptor, mensaje.as_string())
