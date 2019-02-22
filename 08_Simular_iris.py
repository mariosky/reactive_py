
# Reactive
from rx import Observable
from rx.concurrency import ThreadPoolScheduler
from threading import current_thread
import multiprocessing

import time
import random


io_work = True

def work(n):
    for _ in range(n):
        for _ in range(n):
            for x in range(n):
                y = x**2


def sim(valor): 
    if valor[0] == 6.9:
        #while True:
        #    time.sleep(.03)
        if io_work:
            time.sleep(4)
        else:
            work(200)
    time.sleep(.03)
    return valor

num_threads = multiprocessing.cpu_count()
_pool = ThreadPoolScheduler(num_threads)

print("Número de hilos: {}".format(num_threads))

def read_iris(ruta='iris.data'):
    archivo = open(ruta)
    return Observable.from_(archivo) \
            .flat_map( lambda s : Observable.just(s).subscribe_on(_pool))\
            .map(lambda linea : linea.split(',')[:-1] ) \
            .filter(lambda linea : len(linea) > 3 ) \
            .map(lambda linea : list(map(float,linea))) \
            .map(lambda linea : sim(linea)) 
            
read_iris().subscribe(lambda linea : print("{} -> {}".format(current_thread().name,list(linea)) ))







