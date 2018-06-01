import json
import goslate
from difflib import get_close_matches


class Diccionario:
    language="en"
    definition=""
    def __init__(self):
        self.data = json.load(open("data.json"))
        self.gs = goslate.Goslate()
    def selectLanguage(self, language):
        self.language = language
        return

    def lookFor(self, word):
        if word in self.data:
            self.definition=self.data[word]
            return self.definition
        elif word=="":
            print("Please, insert new word")
        elif word.title() in self.data:
            self.definition = self.data[word.title()]
            return            
        else:
            print("error")

    def printDefinition(self):
        i=1
        definition=[]
        for d in self.definition:
            #d = self.gs.translate(d,self.language)
            definition.append(str(i) + ". " +d+"\n")
            i+=1
        return definition
