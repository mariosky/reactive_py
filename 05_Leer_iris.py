
# Reactive
from rx import from_iterable , operators as op


def read_iris(ruta='iris.data'):
    archivo = open(ruta)
    return from_iterable(archivo).pipe(
           op.map(lambda linea : linea.split(',')[:-1] ), 
           op.filter(lambda linea : len(linea) > 3 ), 
           op.map(lambda linea : map(float,linea)))


read_iris().subscribe(lambda linea : print(list(linea)))








