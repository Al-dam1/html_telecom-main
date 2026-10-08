import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana") #set the title of the window
ventana.geometry("800x600") #set the size of the window
ventana.resizable(True, False) #hace q no se pueda estirar ni de ancho ni de alto
ventana.configure(bg='#1b49e2') #set the background color of the window


letrero = tk.Label(
    ventana,
    text='Hola ingrese su nombre',
    pady=20,
    font=('Arial', 14),
    cursor='hand2'
 ).pack(fill='x', pady=(20,20), padx=10)


entrada_texto = tk.Entry(
    ventana,
    font=('Arial', 14)
    )
entrada_texto.pack()

def saludar():
    nombre = entrada_texto.get().strip()
    letrero_salida.configure(text=f'Hola, {nombre} ¿como estas?')

boton = tk.Button(
    text='saludar',
    font=('Arial', 14),
    cursor='hand2',
    command=saludar
)
boton.pack(pady=20)
# letrero.pack( pady=(20,0), padx=10, anchor='e', side='bottom') #
letrero_salida= tk.Label(
     ventana,
        font=('Arial',14)
)
letrero_salida.pack()
ventana.mainloop() #start the main event loop of the application