#There are various situations we might encounter when a list is given and we convert it to a string. For example, conversion to string from the list of strings or the list of integers or mixed data types.
#Input: ['Geeks', 'for', 'Geeks']
#Output: Geeks for Geeks
def funcion_unir(listastring):
    contador=""
    for item in listastring:
        contador= contador+item
    return contador
print(funcion_unir(list ({"geeks","for","eks"})))
#funcion_conversion(lista)
#Onput: ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
#intput: I want 4 apples and 18 bananas
frase = 'hola mundo que se dice el mundo'
response = frase.split(' ')
print(response, type(response))
#def funcion_separa (stringlist):

#string levante una y otra vez hasta que los corderos se conviertan en leones
#delimitador
#list()
def funcion_separar (separadorfrase,separador):
    return separadorfrase.split(separador)
print(funcion_separar("levante una y otra vez hasta que los corderos se conviertan en leones"," "))

