from tkinter import *
from tkinter import messagebox as MessageBox

def seleccionar():
    return

def salir():
	root.destroy()

def test():
    MessageBox.showinfo("Hola","Hola Mundo")
    return


root=Tk()

root.title("Diccionario")

menubar = Menu(root)
root.config(menu=menubar)

fileMenu=Menu(menubar, tearoff=0)
fileMenu.add_command(label="Salir", command=salir)

menubar.add_cascade(label="Archivo",menu=fileMenu)

Label(root, text="Introduce la palabra: ").pack()
entry = Entry(root).pack()

#Seleccionar idioma
opcion = IntVar()
Label(root, text="Selecciona el idioma: ").pack()
Radiobutton(root, text="Inglés", variable=opcion, value = 'en', command=seleccionar).pack()
Radiobutton(root, text="Español", variable=opcion, value = 'es', command=seleccionar).pack()
Radiobutton(root, text="Italiano", variable=opcion, value = 'it', command=seleccionar).pack()
Radiobutton(root, text="Francés", variable=opcion, value = 'fr', command=seleccionar).pack()

Button(root, text="Buscar", command=test).pack()

#Bucle de la aplicación
root.mainloop()
