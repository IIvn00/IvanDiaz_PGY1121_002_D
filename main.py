
from funciones import *
from asistente import *
import numpy as np
def agregarasistente(lista_asistente,num_asiento):
    asis=asistente()
    asis.rut=(input("Ingrese rut:"))
    asis.nombre=input("Ingrese Nombre:")
    asis.num_asiento=num_asiento
    if num_asiento>=1 and num_asiento<=20:
        asis.precio=120000
    if num_asiento>=21 and num_asiento<=50:
        asis.precio=80000
    if num_asiento>=51 and num_asiento<=100:
        asis.precio=50000
    lista_asistente.append(asis)
def comprarasiento(arreglo_crea,lista_asistente):
    try:
        cant_asiento=int(input("Ingrese cantidad de asiento del (1-3)"))
        if cant_asiento>=1 and cant_asiento<=3:
            buy=0
            while buy < cant_asiento:
                mostrar(arreglo_crea)
                num_asiento=int(input("Seleccione numero de asiento"))
                if num_asiento>=1 and num_asiento<=100:
                    disponible=comprobarasiento(arreglo_crea,num_asiento)
                if disponible==True:
                    agregarasistente(lista_asistente,num_asiento)
                    buy(arreglo_crea,num_asiento)
                    buy=buy+1

                    print("Comprado....")
                else:
                    print("No disponible")
        else:
            print("Solo entre 1-3")
    except BaseException as error:
        print(f"ERROR: {error}")
def listadoasistente(lista_asistente):
    rut=input("Ingrese rut:")
    for asis in lista_asistente:
        if rut==asis.rut:
            print(f"Nombre:     {asis.nombre}")
            print(f"Apellido:   {asis.apellido}")
            print(f"N Asiento:  {asis.num_asiento}")
            print(f"Precio:     {asis.precio}")
def MostrarGanancias(lista_asistente):
    p=0
    g=0
    s=0
    tot_p = 0
    tot_g=0
    tot_s=0
    for asis in lista_asistente:
        if int(asis.precio)==120000:
            p = p+1
            tot_p=tot_p+120000
        if int(asis.precio)==80000:
            g = g+1
            tot_g=tot_g+80000
        if int(asis.precio)==50000:
            s = s+1
            tot_s=tot_s+50000
    print(f"Platino Cantidad: {p} TOTAL: {tot_p}")
    print(f"Gold Cantidad:    {g} TOTAL: {tot_g}")
    print(f"Silver Cantidad:  {s} TOTAL: {tot_s}")

###############Menu
arreglo_crea=np.full((10,10),'---')
lista_asistente=[]
ciclo= True
llenar(arreglo_crea)

def salir():
    print("Ivan Diaz")
    print("FECHA: 06/07/2023")


while ciclo:
    print("CREATIVOS.CL")
    print("1) Comprar entradas")
    print("2) Mostrar ubicaciones disponibles")
    print("3) Ver listado de asistentes")
    print("4) Mostrar Ganancias Totales")
    print("5) Salir")
    try:
        op=int(input("Seleccione: (1-5)"))
        match op:
            case 1:
                comprarasiento(arreglo_crea,lista_asistente)
            case 2:
                mostrar(arreglo_crea)
            case 3:
                listadoasistente(lista_asistente)
            case 4:
                MostrarGanancias(lista_asistente)
            case 5:
                ciclo=salir()
    except BaseException as error:
        print(f"ERROR {error}")

