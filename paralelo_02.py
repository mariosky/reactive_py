from rx import Observable
from rx.concurrency import ThreadPoolScheduler

from threading import current_thread

import multiprocessing
import time
import random


def cálculo_intenso(valor):
    time.sleep(random.choice([1,3,5]))
    return valor

num_threads = multiprocessing.cpu_count()
calendarizador_pool = ThreadPoolScheduler(num_threads)

print("Número de threads: {}".format(num_threads))


Observable.from_(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"])\
    .flat_map( lambda s : Observable.just(s).subscribe_on(calendarizador_pool))\
    .map(lambda s: cálculo_intenso(s))\
    .subscribe(on_next=lambda p: print("Proceso 1: {} {}".format(current_thread().name, p)),
               on_error=lambda e: print(e),
               on_completed=lambda: print("Proceso 1: Terminado"))


Observable.from_(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"])\
    .flat_map( lambda s : Observable.just(s).subscribe_on(calendarizador_pool))\
    .map(lambda s: cálculo_intenso(s))\
    .subscribe(on_next=lambda p: print("Proceso 2: {} {}".format(current_thread().name, p)),
               on_error=lambda e: print(e),
               on_completed=lambda: print("Proceso 2: Terminado"))

