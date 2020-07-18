import tkinter as tk
from decimal import Decimal

from calculos import validacion_decimal, calc_porcentaje


class CalculadoraPorcentajes(tk.Frame):
    et_por_defecto = 'Añada números'
    et_cantidad = 'Cantidad'
    et_porcentaje = '%\n[1-100]'
    et_boton = 'Calcular'

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(padx=20, pady=10)
        self.crear_componentes()

    def crear_componentes(self):
        # registrando un validador
        reg_decimal = self.master.register(validacion_decimal)

        # bloque de etiqueta y entrada de números para Cantidad
        tk.Label(self, text=self.et_cantidad).grid(column=0, row=0)
        self.cantidad_entry = tk.Entry(self, justify='center', fg='blue', width=15)
        self.cantidad_entry.config(validate='key', validatecommand=(reg_decimal, '%P'))
        self.cantidad_entry.grid(column=0, row=1)

        # bloque de etiqueta y entrada de números para Porcentaje
        tk.Label(self, text=self.et_porcentaje).grid(column=1, row=0)
        self.porcentaje_entry = tk.Entry(self, justify='center', fg='green', width=15)
        self.porcentaje_entry.config(validate='key', validatecommand=(reg_decimal, '%P'))
        self.porcentaje_entry.grid(column=1, row=1)

        # etiqueta de resultados
        self.et_resultado = tk.Label(self, text=self.et_por_defecto, justify='center', pady=10)
        self.et_resultado.grid(column=0, row=3, columnspan=2)

        # botón de calcular
        self.calc_btn = tk.Button(self, text=self.et_boton, justify='center', command=self.comando_calcular)
        self.calc_btn.grid(column=0, row=2, columnspan=2)

    def comando_calcular(self):
        """calcula el valor del porcentaje sobre la cantidad siempre que ambos valores estén presentes"""
        cantidad = self.cantidad_entry.get()
        porcentaje = self.porcentaje_entry.get()
        if cantidad == '' or porcentaje == '':
            text = self.et_por_defecto
        else:
            calculo = calc_porcentaje(Decimal(cantidad), Decimal(porcentaje))
            text = str(calculo)
        self.et_resultado.config(text=text)


class CalculadoraBN(CalculadoraPorcentajes):
    def crear_componentes(self):
        super().crear_componentes()
        self.porcentaje_entry.config(fg='black')
        self.cantidad_entry.config(fg='black')
        self.calc_btn.config(bg='cyan')
        self.calc_btn.grid(column=0, row=5)


class EnglishCalc(CalculadoraPorcentajes):
    et_por_defecto = 'Add numbers'
    et_cantidad = 'Amount'
    et_boton = 'Calculate'


if __name__ == '__main__':
    raiz = tk.Tk()
    raiz.title('Calculadora de porcentajes')
    # raiz.title('Percent calculator')
    # app = CalculadoraBN(master=raiz)
    # app = EnglishCalc(master=raiz)
    app = CalculadoraPorcentajes(master=raiz)
    raiz.mainloop()
