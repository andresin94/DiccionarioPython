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

def selectLanguage():
    language = option.get()
    dic.selectLanguage(language)
    return

#MainWindow
root=Tk()
root.title("Dictionary")

#ToolBar
menubar = Menu(root)
root.config(menu=menubar)
fileMenu=Menu(menubar, tearoff=0)
fileMenu.add_command(label="Salir",command=root.quit)
menubar.add_cascade(label="Archivo",menu=fileMenu)

#We divide the screen into 2 parts
frame=Frame(root)
frame.pack(side="left")
frame.config(bd=20)
frame1=Frame(root)
frame1.pack(side="right")
frame1.config(bd=20)

#Variables
n1 = StringVar()
option = StringVar(value=" ")

#LeftPart
Label(frame, text="Enter a new word: ").pack()
entry = Entry(frame, textvariable=n1).pack()
#Select language
Label(frame, text="Select Language: ").pack()
Radiobutton(frame, text="Inglés", variable=option, value = 'en', command=selectLanguage).pack()
Radiobutton(frame, text="Español", variable=option, value = 'es', command=selectLanguage).pack()
Radiobutton(frame, text="Italiano", variable=option, value = 'it', command=selectLanguage).pack()
Radiobutton(frame, text="Francés", variable=option, value = 'fr', command=selectLanguage).pack()
#LookFor Button
Button(frame, text="Buscar", command=lookFor).pack()

#Right Part
Label(frame1, text = "Definition: ").pack()
lista = Listbox(frame1, width = 50)
lista.pack()

#Aplication Loop
root.mainloop()
