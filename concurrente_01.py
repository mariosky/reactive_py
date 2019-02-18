from rx import Observable
from threading import current_thread

import time
import random

def cálculo_intenso(valor):
    time.sleep(random.choice([0.3,0.5,1]))
    return valor


Observable.from_(["A","B","C","D","E"])\
    .map(lambda s: cálculo_intenso(s))\
    .subscribe(on_next=lambda p: print("Proceso 1: {} {}".format(current_thread().name, p)),
               on_error=lambda e: print(e),
               on_completed=lambda: print("Proceso 1: Terminado"))

Observable.from_(range(10))\
    .map(lambda s: cálculo_intenso(s))\
    .subscribe(on_next=lambda p: print("Proceso 2: {} {}".format(current_thread().name, p)),
               on_error=lambda e: print(e),
               on_completed=lambda: print("Proceso 2: Terminado"))



#input("Espera")