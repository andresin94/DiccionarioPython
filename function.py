import json
from difflib import get_close_matches
import goslate
from tkinter import messagebox as MessageBox


gs = goslate.Goslate()

data = json.load(open("data.json"))

def seleccionar():
    return

def test():
    MessageBox.showinfo("Hola","Hola Mundo")
    return

def selectLanguage():
    #Hay que elegir español (es), italiano (it) o ingles (en)
    language = input("Select your language ('es', 'it', 'fr', 'en'): ")
    if language != 'es' and language != 'it' and language != 'fr' and language != 'en':
        print("The available language are Spanish (es), Italian (it), French (fr) and English (en)")
        selectLanguage()
    return language

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
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
        return result
    else:
        return "The word doesn´t exit. Please, double check it"
"""
while (True):
    language = selectLanguage()
    word = input("Enter a new word: ")
    if word == "0":
        break
    definition = translate(word)
    i = 1
    for d in definition:
        d = gs.translate(d,language)
        print(str(i) + ". " +d)
        i+=1
"""
