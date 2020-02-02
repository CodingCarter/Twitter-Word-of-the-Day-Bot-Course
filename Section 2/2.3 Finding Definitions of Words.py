from PyDictionary import PyDictionary
dictionary = PyDictionary()

word = "indentation"
definition = dictionary.meaning(word)

print(word + ": " + definition["Noun"][0])
