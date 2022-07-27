# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 20:18:59 2022

@author: Adrian Flores
"""

import random
while True:
    filas=int(input("INGRESE NUMERO DE FILAS{4-10}: "))
    if filas<4 or filas>10:
        print("ERROR, FUERA DEL RANGO ESTABLECIDO")
    else:
        break
while True:
    columnas=int(input("INGRESE NUMERO DE COLUMNAS{4-10}: "))
    if columnas<4 or columnas>10:
        print("ERROR, FUERA DEL RANGO ESTABLECIDO")
    else:
        break
    
matriz = [[int() for i in range(columnas)] for j in range(filas)]

def numrandom():
    for f in range(filas):
        for c in range(columnas):
            valor=random.randint(0,5)
            matriz[f][c]=valor
        
numrandom()

for i in range(filas):
    print("|", end=" ")
    for j in range(columnas):
        print(matriz[i][j],"|",end=" ")
    print("\n")

def sumaf(fila):
    sumaf=0
    for s in range(columnas):
        valorf=matriz[fila-1][s]
        sumaf+=valorf
    print("LA SUMA DE LA FILA:",fila,"EN TOTAL ES:",sumaf)
    
def sumac(columna):
    sumac=0
    for b in range(filas):
        valorc=matriz[b][columna-1]
        sumac+=valorc
    print("LA SUMA DE LA COLUMNA:",columna,"EN TOTAL ES:",sumac)
    print("\n")

for k in range(filas):   
    sumaf(k+1)
    sumac(k+1)

def promedio():
    sumat=0
    for p in range(filas):
        for q in range(columnas):
            suma=matriz[p][q]
            sumat+=suma
    print("EL PROMEDIO TOTAL ES:",sumat/(filas*columnas))
promedio()