import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana") #set the title of the window
ventana.geometry("400x300") #set the size of the window
def saludar():
    etiqueta.config(text="¡Hola, mundo!") #change the text of the label
boton = tk.Button(ventana, text='saludar', command=saludar) #create a button that calls the saludar function when clicked
boton.pack() #add the button to the window
etiqueta = tk.Label(ventana, text='Hola mundo, desde tk') #create a label with the text 'Hola mundo, desde Tkinter'
etiqueta.pack(pady=10) #add the label to the window with some padding

ventana.mainloop() #start the main event loop of the application
bg='#ffffff' #set the background color of the window
fg='#000000' #set the foreground color of the window