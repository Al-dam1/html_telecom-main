#importa la librería tkinter
import tkinter as tk
print('hola tkinter')

#función que se ejecuta al presionar el botón
#obtiene el contenido de las cajas de texto y lo muestra en una etiqueta
def saludar():
    nombre = caja1.get().title()       #obtiene el texto de la primera caja
    apellido = caja2.get().title()     #obtiene el texto de la segunda caja
    #actualiza la etiqueta con el saludo
    etiqueta_saludo.config(text=f'hola {apellido} {nombre}')
    final.config(text='')      #limpia la etiqueta final (aunque no se usa mucho)

#creamos la ventana principal
ventana = tk.Tk()

#establecer un título para la ventana
ventana.title('Expreso Del Oeste')

#establecer un tamaño fijo de la ventana
ventana.geometry('400x300')

#entrada de datos (cajas de texto)
caja1 = tk.Entry(ventana)   #caja para el nombre
caja1.place(x=120, y=50, width=150, height=25)

caja2 = tk.Entry(ventana)   #caja para el apellido
caja2.place(x=120, y=90, width=100, height=25)

#crear un botón que ejecuta la función saludar
boton1 = tk.Button(ventana, text='que onda wachina', command=saludar)
#tamaño y una posición
boton1.place(x=40, y=130, width=140, height=25)

#etiquetas => textos que se muestran en la pantalla
etiqueta1 = tk.Label(ventana, text='nombre:', bg='#ff0000')
etiqueta1.place(x=40, y=50)

etiqueta2 = tk.Label(ventana, text='apellido:', bg='#00ff00')
etiqueta2.place(x=40, y=90)

#etiqueta donde se mostrará el saludo
etiqueta_saludo = tk.Label(ventana)
etiqueta_saludo.place(x=40, y=200)

#etiqueta final (no se usa mucho en este ejemplo)
final = tk.Label(ventana)

#mostramos la ventana y mantenemos el programa en ejecución
ventana.mainloop()
