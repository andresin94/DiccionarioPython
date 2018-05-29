from tkinter import *
#from function import *
from difflib import get_close_matches

import json

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    monitor.config(text="word")
    if word in data:
	    monitor.config(text="word")
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) > 0:
        similarWords = get_close_matches(word, data.keys())
        print("Did you mean %s instead? " % similarWords)
        pos = int(input("If it isn't one of the words, press any key: "))
        if pos <= len(similarWords):
            result = data[similarWords[pos-1]]
        else:
            result = "Please"
        print(result)
    else:
        return "The word doesn´t exit. Please, double check it"

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

Label(root, text="Introduce la palabra: ").pack()
n1 = StringVar()
entry = Entry(root, textvariable=n1).pack()

#Seleccionar idioma
opcion = StringVar()

Label(root, text="Selecciona el idioma: ").pack()
Radiobutton(root, text="Inglés", variable=opcion, value = 'en', command=seleccionar).pack()
Radiobutton(root, text="Español", variable=opcion, value = 'es', command=seleccionar).pack()
Radiobutton(root, text="Italiano", variable=opcion, value = 'it', command=seleccionar).pack()
Radiobutton(root, text="Francés", variable=opcion, value = 'fr', command=seleccionar).pack()

Button(root, text="Buscar", command=translate(n1.get())).pack()

monitor=Label(root, text="HOLA")
monitor.pack()
#Bucle de la aplicación
root.mainloop()
