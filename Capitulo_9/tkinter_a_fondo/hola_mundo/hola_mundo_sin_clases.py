import tkinter as tk

import random


def cambia_texto(label_wt, textos):
    texto = random.choice(textos)
    label_wt.config(text=texto)


if __name__ == '__main__':
    textos = ['Hola amigos', 'Primera app en tkinter',
              'Python a fondo', 'Los gatos maúllan',
              'Los perros ladran', 'Los niños juegan']

    raiz = tk.Tk()
    raiz.title('Hola Mundo')

    app = tk.Frame(raiz)
    app.pack(padx=20, pady=10)

    etiqueta = tk.Label(app, text='Hola Mundo')
    etiqueta.pack()

    btn = tk.Button(app, command=lambda: cambia_texto(etiqueta, textos))
    btn.config(text='Haga click aquí')
    btn.pack()

    raiz.mainloop()
