import tkinter as tk
from decimal import Decimal

from calculadora_porcentaje.calculos import validacion_decimal, calc_porcentaje


def calcular_wd(cantidad_wd, porcentaje_wd, resultado_wd):
    """Calcula el porcentaje del valor de porcentaje_wd sobre la cantidad en cantidad_wd y muestra el resultado
    en formato de cadena de texto en resultado_wd"""
    cantidad = cantidad_wd.get()
    porcentaje = porcentaje_wd.get()

    if cantidad == '' or porcentaje == '':
        text = 'Añada números'
    else:
        calculo = calc_porcentaje(Decimal(cantidad), Decimal(porcentaje))
        text = str(calculo)
    resultado_wd.config(text=text)


if __name__ == '__main__':
    # Creando la ventana y el único frame
    raiz = tk.Tk()
    raiz.title('Calculadora de porcentajes')
    panel = tk.Frame()
    panel.pack(padx=20, pady=10)

    # registrando un validador para que solo se añadan números en los campos
    reg_decimal = raiz.register(validacion_decimal)

    # bloque de etiqueta y entrada de números para Cantidad
    tk.Label(panel, cnf=dict(text='Cantidad')).grid(column=0, row=0)
    cantidad_entry = tk.Entry(panel, cnf=dict(justify='center', fg='blue', width=15))
    cantidad_entry.config(validate='key', validatecommand=(reg_decimal, '%P'))
    cantidad_entry.grid(column=0, row=1)

    # bloque de etiqueta y entrada de números para Porcentaje
    tk.Label(panel, cnf=dict(text='%\n[1-100]')).grid(column=1, row=0)
    porcentaje_entry = tk.Entry(panel, cnf=dict(justify='center', fg='green', width=15))
    porcentaje_entry.config(validate='key', validatecommand=(reg_decimal, '%P'))
    porcentaje_entry.grid(column=1, row=1)

    # Etiqueta de resultados
    resultado_lbl = tk.Label(panel, cnf=dict(text='Añada números', justify='center', pady=10))
    resultado_lbl.grid(column=0, row=3, columnspan=2)

    # Boton de calcular
    calc_btn = tk.Button(panel, cnf=dict(text='Calcular', justify='center'),
                         command=lambda: calcular_wd(cantidad_entry, porcentaje_entry, resultado_lbl))
    calc_btn.grid(column=0, row=2, columnspan=2)

    raiz.mainloop()
