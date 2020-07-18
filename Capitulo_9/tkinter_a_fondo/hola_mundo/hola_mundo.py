import tkinter as tk
import random


class HolaMundoApp(tk.Frame):
    textos = ['Hola amigos', 'Primera app usando tkinter',
              'Python a fondo', 'Los gatos maullan',
              'Los perros ladran', 'Los niños juegan']

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(padx=20, pady=10)
        self.crear_componentes()

    def crear_componentes(self):
        self.etiqueta = tk.Label(self, text='Hola Mundo')
        self.etiqueta.pack()
        self.btn = tk.Button(self, command=self.cambiar_texto)
        self.btn.config(text='Haga click aquí')
        self.btn.pack()

    def cambiar_texto(self):
        texto = random.choice(self.textos)
        self.etiqueta.config(text=texto)


class AplicacionDeColores(HolaMundoApp):
    textos = {'Azul': 'blue', 'Rojo': 'red', 'Gris': 'grey', 'Verde': 'green', 'Marrón': 'brown'}

    def cambiar_texto(self):
        color = random.choice(list(self.textos.keys()))
        self.etiqueta.config(text=color.title(), fg=self.textos[color])


if __name__ == '__main__':
    raiz = tk.Tk()
    raiz.title('Hola Mundo')
    app = HolaMundoApp(master=raiz)
    # app2 = AplicacionDeColores(master=raiz)
    raiz.mainloop()
