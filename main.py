import tkinter as tk
from tkinter import *
from Diccionario import *
from tkinter import messagebox
from difflib import get_close_matches

dic = Diccionario()
def lookFor():
    lista.delete(0, tk.END)
    word = n1.get()
    dic.lookFor(word)
    definition=dic.printDefinition()
    lista.insert(0, *definition)

def seleccionar():
    return

def test():
    MessageBox.showinfo(opcion.get(),"Hola Mundo")
    return

root=Tk()
root.title("Diccionario")

menubar = Menu(root)
root.config(menu=menubar)

fileMenu=Menu(menubar, tearoff=0)
fileMenu.add_command(label="Salir",command=root.quit)

menubar.add_cascade(label="Archivo",menu=fileMenu)
"""
imagen = PhotoImage(file="diccionario.png")
Label(root, image=imagen).pack(side="left")
"""
frame=Frame(root)
frame.pack(side="left")
frame.config(bd=20)

frame1=Frame(root)
frame1.pack(side="right")
frame1.config(bd=20)

Label(frame, text="Introduce la palabra: ").pack()
n1 = StringVar()
entry = Entry(frame, textvariable=n1).pack()

#Seleccionar idioma
opcion = StringVar(value=" ")

Label(frame, text="Selecciona el idioma: ").pack()
Radiobutton(frame, text="Inglés", variable=opcion, value = 'en', command=seleccionar).pack()
Radiobutton(frame, text="Español", variable=opcion, value = 'es', command=seleccionar).pack()
Radiobutton(frame, text="Italiano", variable=opcion, value = 'it', command=seleccionar).pack()
Radiobutton(frame, text="Francés", variable=opcion, value = 'fr', command=seleccionar).pack()

Button(frame, text="Buscar", command=lookFor).pack()


lista = Listbox(frame1, width = 50)
lista.pack()
#Bucle de la aplicación
root.mainloop()
