
# Reactive Simulation

from rx import Observable
import time
import random

def sim(valor):
    print(valor)
    if valor[0] == 6.9:
        #while True:
        #    pass
        time.sleep(3)
    time.sleep(.03)
    return valor


def read_iris(ruta='iris.data'):
    archivo = open(ruta)
    return Observable.from_(archivo) \
            .map(lambda linea : linea.split(',')[:-1] ) \
            .filter(lambda linea : len(linea) > 3 ) \
            .map(lambda linea : list(map(float,linea))) \
            .map(lambda linea : sim(linea))


read_iris().subscribe(lambda linea : print(list(linea)))





