""" import tkinter as tk

ventana = tk.Tk()
ventana.title("¡Hola mundo!")
ventana.geometry("400x300")

def saludar():
    etiqueta.config(text="¡bom noite!")

boton = tk.Button(ventana, text="Saludar", command=saludar, bg="blue", fg="white")
boton.pack()

etiqueta = tk.Label(ventana, text="Hola mundo, desde Tk!!!")
etiqueta.pack(pady=10)

ventana.mainloop()
 
         CASO 02
 
import tkinter as tk
ventana= tk.Tk()
ventana.title("hola chaval!!")
ventana.geometry("500x400")

def saludar():
    etiqueta.config(text="hola , bom noite!!")

boton=tk.Button(ventana,text="saludar",command=saludar, bg="blue",fg="white")
boton.pack()

etiqueta= tk.Label(ventana, text="hola mundo , desde TK!!")
etiqueta.pack(pady=20)

ventana.mainloop() """

import tkinter as tk
from tkinter import ttk  # Importar ttk para usar combobox

def mostrar_resultado():
    nombre = entrada_nombre.get()
    lenguaje = lenguaje_var.get()
    gusto = "sí" if check_var.get() else "no"
    experiencia = experiencia_var.get()
    salida.config(text=f"Hola {nombre}, elegiste {lenguaje}, nivel {experiencia}, ¿te gusta programar? {gusto}!")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Formulario avanzado")
ventana.geometry("950x950")

# Etiqueta y entrada de nombre
tk.Label(ventana, text="Tu nombre:").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

# Menú desplegable de lenguaje favorito
tk.Label(ventana, text="Lenguaje favorito:").pack()
lenguaje_var = tk.StringVar()
combo = ttk.Combobox(ventana, textvariable=lenguaje_var)
combo["values"] = ("Python", "JavaScript", "C++", "Java")
combo.current(0)
combo.pack()

# Radio buttons para nivel de experiencia
tk.Label(ventana, text="Nivel de experiencia:").pack()
experiencia_var = tk.StringVar(value="Principiante")
niveles = ["Principiante", "Intermedio", "Avanzado"]
for nivel in niveles:
    tk.Radiobutton(ventana, text=nivel, variable=experiencia_var, value=nivel).pack()

# Checkbox para gusto por programar
check_var = tk.BooleanVar()
tk.Checkbutton(ventana, text="¿Te gusta programar?", variable=check_var).pack()

# Botón para mostrar resultado
tk.Button(ventana, text="Mostrar resultado", command=mostrar_resultado).pack(pady=10)

# Etiqueta de salida
salida = tk.Label(ventana, text="", wraplength=300)
salida.pack()

# Ejecutar ventana
ventana.mainloop()



