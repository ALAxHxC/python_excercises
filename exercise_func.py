#Exercise 1: Define a function that accepts 2 values and return its sum, subtraction and multiplication.

def funcion_operaciones(numero_1,numero_2):
    resultado= numero_1+numero_2
    resultado_resta=numero_1-numero_2
    resultado_multiplica=numero_1*numero_2
    return resultado,resultado_resta,resultado_multiplica
def funcion_ingreso_de_datos():
    a=int(input('Ingrese valor'))
    if a <= 0 :
        print('Ingresar un nuevo numero')
        return funcion_ingreso_de_datos()
    return a
while True:
    a = funcion_ingreso_de_datos()
    print(a)
    b = funcion_ingreso_de_datos()
    print(funcion_operaciones(a,b))
