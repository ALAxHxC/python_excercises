#https://exercism.org/tracks/python/exercises/armstrong-numbers
def test():
    try:
        data ={}
        data['b']
    except KeyError as e:
        print('OCURRIO UN ERROR DE LLAVES')
    except Exception as e:
        print('OURRIO UN ERROR',e)

test()