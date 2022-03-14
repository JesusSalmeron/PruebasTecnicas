

# Prueba técnica #
#Cuenta las palabras y devuelve cuantas veces se repiten.



from os import sep


def toLowerCase(text):
    lowercase = text.lower()
    return lowercase

def CleanText(textlower):
    CleanText = textlower.replace(',','').replace('.','')
    separatedText = CleanText.split(" ")
    return separatedText

def countWords(CleanText):
    dictionary = {}
    for word in CleanText:
        if word in dictionary:
            dictionary[word] +=1
        else:
            dictionary[word]=1
    return dictionary



text = "Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar"

toLowerCase = toLowerCase(text)
CleanText = CleanText(toLowerCase)
countWords = countWords(CleanText)

print(countWords)


