# https://exercism.org/tracks/python/exercises/darts
import math


def funcion_distancia(x, y):
    return math.sqrt((x ** 2) + (y ** 2))


c = funcion_distancia(3, 4)
print(c)


def funcion_calcular(c):
    if c > 10: return 0
    if c <= 10 and c > 5: return 1
    if c > 1 and c <= 5: return 5
    if c == 1: return 10


print(funcion_calcular(c))


class Dardo:
    x: int=0
    y: int=0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass

    def funcion_distancia(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))


dardo = Dardo(2, 3)
print(dardo.funcion_distancia())
