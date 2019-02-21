
# Reactive Simulation

# Tarea

from rx import Observable


def sim(valor):
    time.sleep(random.choice([0.3,0.5,1]))
    return valor



def read_iris(ruta='iris.data'):
    archivo = open(ruta)
    return Observable.from_(archivo) \
            .map(lambda linea : linea.split(',')[:-1] ) \
            .filter(lambda linea : len(linea) > 3 ) \
            .map(lambda linea : map(float,linea))


read_iris().subscribe(lambda linea : print(list(linea)))





