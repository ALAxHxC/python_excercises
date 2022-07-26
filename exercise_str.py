#Given a sentence containing n words/strings. Remove all duplicates words/strings which are similar to each others.
#Examples:
def funcion_diccstring (liststring:dict):
    contador=""
    for item in liststring.keys():
        contador= contador + " "+item
    print(contador)
#Input : Geeks for Geeks
#Output : Geeks for
def funcion_duplicados (string:str):
    lista=string.split(" ")
    valor={}
    for item in lista:
        if item not in valor.keys():
            valor[item]=0
        if item in valor.keys():
            valor[item]=valor[item]+1
    funcion_diccstring (valor)

print(funcion_duplicados("levante en los levante conviertan en leones"))
#Input: Python is great and Java is also great
#Output: is also Java Python and great

