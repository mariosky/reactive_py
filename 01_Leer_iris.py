# Procedural
datos = []
with open('iris.data') as archivo:
    linea = archivo.readline()
    while linea:
        columnas = linea.split(",")
        print(columnas)
        if len(columnas) > 3:
            flor = []
            for cadena in columnas[:-1]:
                flor.append(float(cadena))
            datos.append(flor)

        linea = archivo.readline()
print(datos)






