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

    html = """\
    <html>
      <body>
        <p>Querid@ Pythonista {nombre},<br>
           ¿Que tal?<br><br>
           Encuentra la mejor información sobre Python en <a href="www.elpythonista.com">El Pythonista</a><br><br>
           
           Ejemplo basado en los ejemplos del libro <b>Python a Fondo</b>
        </p>
      </body>
    </html>
    """

    for nombre in ['Juan', 'Maria', 'Pedro']:
        mensaje_html = MIMEText(html.format(nombre=nombre), "html")
        mensaje.attach(mensaje_html)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as servidor:
            servidor.login(email_emisor, password)
            servidor.sendmail(
                email_emisor, email_receptor, mensaje.as_string()
            )
