
# Pythonic

with open('iris.data') as archivo:
    datos = [ list(map(float, linea.split(',')[:-1]))
              for linea in archivo
                if len(linea)>3]
print(datos)






