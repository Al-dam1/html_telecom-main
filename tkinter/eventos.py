
import tkinter as tk

ventana = tk.Tk()
ventana.title("Eventos en Tkinter")
ventana.geometry("800x600")

def saludar(event=None):
    nombre = entrada_texto.get().strip().title()
    valor_str.set(f'Hola, {nombre} ¿como estas?')
    print(event.char)
   # print(event.x, event.y)
   

entrada_texto = tk.Entry(ventana, font=('Arial', 14))
entrada_texto.pack(pady=10)

# Evento al presionar Enter
# entrada_texto.bind('<Button-1>', saludar)
entrada_texto.bind('<Key>', saludar)

# boton = tk.Button(
#     ventana,
#     text='Saludar',
#     font=('Arial', 14),
#     command=saludar
# )
# boton.pack(pady=10)

valor_str = tk.StringVar(value='Esperando...')

letrero_salida = tk.Label(
    ventana,
    textvariable=valor_str,
    font=('Arial', 14)
)
letrero_salida.pack(pady=10)


ventana.mainloop()
