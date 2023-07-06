import numpy as np
def llenar(arreglo_crea):
    x=0
    for f in range (10):
        for c in range (10):
            x=x+1
            arreglo_crea[f][c] = str(x)
def mostrar(arreglo_crea):
    for f in range (10):
        fila=''
        for c in range (10):
            fila=fila+' | '+str(arreglo_crea[f][c])
        print(fila)
def comprar_entrada(arreglo_crea,num_asiento):
    x = 0
    for f in range(10):
        for c in range (10):
            x = x + 1
            if str(x) == str(num_asiento):
                arreglo_crea[f][c] == 'X'
def comprobarasiento(arreglo_crea,num_asiento):
    x=0
    for f in range (10):
        for c in range (10):
            x=x+1
            if str(x) == str(num_asiento):
                if arreglo_crea[f][c] == 'X':
                    return False
    return True