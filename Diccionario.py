import json
import goslate

class Diccionario:
    language="es"
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
        else:
            print("error")

    def printDefinition(self):
        i=1
        definition=[]
        for d in self.definition:
            d = self.gs.translate(d,self.language)
            definition.append(str(i) + ". " +d+"\n")
            i+=1
        print(definition)
        return definition
