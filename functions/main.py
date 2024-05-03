import requests

TOKEN = 'y0_AgAAAAA7fFOGAADLWwAAAAD5X6TaAACOGGOTXqdN3KPXriSq0CGD1QqJNw'
BASE_URL = 'https://cloud-api.yandex.net/v1/disk/resources?path='


def perimeter(a, b):
    if a <= 0 or b <= 0:
        raise ValueError('Такая фигура не существует')
    result = 2*a+2*b
    return result


def area(a, b):
    if a <= 0 or b <= 0:
        raise ValueError('Такая фигура не существует')
    result = a*b
    return result


def quadratics(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (discriminant ** 0.5 - b) / (2 * a)
        x2 = (-(discriminant ** 0.5) - b) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = (-b - discriminant ** 0.5) / (2 * a)
        return x
    else:
        return "Kорней нет"



