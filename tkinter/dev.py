import tkinter as tk
from tkinter import ttk

def mostrar_resultado():
    nombre = entrada_nombre.get()
    lenguaje = lenguaje_var.get()
    gusto = 'si' if check_var.get() else 'no'
    salida.config(text=f'Hola {nombre}, elegiste {lenguaje} y te gusta programar {gusto}.!!')
#creamos la ventana
ventana = tk.Tk()
ventana.title('formulario avanzado')
ventana.geometry('400x300')

#etiqueta y entrada
tk.Label(ventana, text='Ingrese su nombre: ').pack(pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

#menu desplegable
tk.Label(ventana, text='Seleccione su lenguaje de programación favorito: ').pack(pady=5)
lenguaje_var = tk.StringVar() #variable que guarda el valor seleccionado
combo = ttk.Combobox(ventana, textvariable=lenguaje_var)
combo ['values'] = ('Python', 'Java', 'C++', 'JavaScript') #opciones del menu desplegable
combo.current(0) #seleccionamos la primera opcion por defecto
combo.pack() # => hace que se integre, llama la funcion.

#radio buttons
tk.Label(ventana, text='Nivel de experiencia: ').pack()
experiencia_var = tk.StringVar(value='Principiante') #variable que guarda el valor seleccionado
tk.Radiobutton(ventana, text='Principiante', variable=experiencia_var, value='Principiante').pack()
tk.Radiobutton(ventana, text='Intermedio', variable=experiencia_var, value='Intermedio').pack()
tk.Radiobutton(ventana, text='Avanzado', variable=experiencia_var, value='Avanzado').pack()

#checkbox
check_var = tk.BooleanVar() #variable que guarda el valor seleccionado
tk.Checkbutton(ventana, text='¿Te gusta programar?', variable=check_var).pack()
#boton para mostrar el resultado    
tk.Button(ventana, text='Mostrar resultado', command=mostrar_resultado).pack(pady=10)
#salida
salida = tk.Label(ventana, text='')
salida.pack(pady=10)
#ejecuta ventana
ventana.mainloop()