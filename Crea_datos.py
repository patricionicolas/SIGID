#!/usr/bin/env python
# -*- coding: utf-8 -*-
# obtener el dígito verificador de un rut
import random

def digito_verificador(rut):
    producto = [2,3,4,5,6,7] # producto de con el cual se debe multiplicar
    list_rut = list(map(int, str(rut))) # convertir en lista el rut
    list_rut.reverse() # revertir los valores
    contador = 0
    pivote = 0
    for i in list_rut:
        if pivote >= len(producto): # si el pivote pasa la cantidad del largo de producto, se debe reiniciar
            pivote = 0
        contador = contador+(i*producto[pivote])
        pivote += 1
    suma_dig = 11-(contador%11) # obtener el resto menos 11 de la suma
    # definir digito verificador
    if suma_dig == 11:
        verificador = 0
    elif suma_dig == 10:
        verificador = 'K'
    else:
        verificador = suma_dig

    return verificador

def genera_rut(**kwargs):
    # rut autoincremental a partir del numero indicado
    keys = []
    exportar = False
    for key in kwargs.keys():
        keys.append(key)
    # cantidad de rut a generar
    if not 'cantidad' in keys: # si no se especifica la cantidad, se generarán 10
        cant_rut = 10
    else:
        cant_rut = int(kwargs['cantidad'])
    # inicio del rut (es autoincremental)
    if not 'inicio' in keys:
        inicio = 1
    else:
        inicio = int(kwargs['inicio'])
    # si se exporta o no
    if not 'csv' in keys:
        exportar = False
    else:
        exportar = kwargs['csv'] # true or false
    
    pivot = 0
    lista_rut = []
    while pivot < cant_rut:
        rut = str(inicio) + '-' + str(digito_verificador(inicio))
        lista_rut.append(rut)
        # autoincrementales
        inicio += 1
        pivot += 1

    return lista_rut


##### CREA RUT
def crea_rut():
    cantidad         = random.randint(1,10000)
    rut_inicio       = random.randint(1000000,40000000)
    rut_seleccionado = random.randint(0, cantidad)
    ruts             = genera_rut(cantidad=cantidad, inicio=rut_inicio, csv=False)
    return ruts[rut_seleccionado]

def crea_nombre(sexo):
    if sexo == "femenino":
        return "Nombre femenino"
    
    if sexo == "masculino":
        return "Patricio Riffo Figueroa"
    
def crea_zona():
    return random.randint(0,1)
   

def crea_etnia():
    return random.randint(0,9)

def crea_nacionalidad():
    return random.randint(0,237)

def crea_region():
    return str(random.randint(1,15))

def crea_poblacion():
    #Crear algoritmo
    return "Poblacion"

def crea_calle():
    #Crear algoritmo
    return "calle"

def crea_telefono():
    #Crear algoritmo
    return "+56999086178"

def crea_nacimiento():
    #Crear algoritmo
    fecha = str(random.randint(0,28))+"/"+str(random.randint(1,12))+"/"+str(random.randint(1990,2005))
    return fecha
    

def crea_sexo():
    sexos = ["femenino", "masculino"]
    return sexos[random.randint(0,1)]

    
