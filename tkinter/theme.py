import tkinter as tk
from tkinter import ttk 

ventana = tk.Tk()
ventana.title("Themes en Tkinter")
ventana.geometry("800x600")
ventana.resizable(False,False)

style=ttk.Style()
style.theme_use('clam')
style.configure(
    'MiBoton.TButton',
    font=('Arial',14),
    background='blue',
    foreground='white',
    padding=10
)
# cambiar el comportamiento
style.map(
    'MiBoton.TButton',
    background=[
        ('pressed','red'),
        ('active', 'green')
    ]
)
entrada= ttk.Entry(ventana)
entrada.pack()

boton = ttk.Button(
    ventana,
    text='Aceptar',
    style='MiBoton.TButton'
)
boton.pack(pady=10)


ventana.mainloop()
