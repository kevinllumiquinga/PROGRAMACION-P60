# -*- coding: utf-8 -*-
"""
Created on Tue Jul  27 00:38:24 2022

@author: Kevin llumiquinga
"""

from random import randint #xolocamos las funciones que vamos importar

N=int(input("# FILAS: ")) # Identificamos nuestra variable

while N<4 or N>31: # Abrimos el bucle para poder colocar las respectivos rangos  que hagan valer al programa.
    
    print("ERROR") # Se remitira un mensaje si no cumple el rango que puse.
    N=int(input("#FILAS: ")) # N es una variable , donde vuelve a pedir el valor de filas
    
M=int(input("#COLUMNAS ")) # Identificamos nuestra variable 
while M<4 or M>31: # Abrimos el bucle para poder colocar las respectivos rangos  que hagan valer al programa.
    
    print("ERROR") # Se remitira un mensaje si no cumple el rango que puse.
    M=int(input("#COLUMNAS ")) # N es una variable , donde vuelve a pedir el valor de columnas
   
 
       
m=[0]*N # creamos la variable de la operacion


for i in range(N): # agragamos un nuevo rango donde vamos a poner inciar con la matriz.
    m[i]=[0]*M #agragamos las variables al prblema

for i in range (N): # colocamos rango en N
    for j in range(M): # colocamos rango en M
        h=randint(4,100) # ponemos funcion
        m[i][j]=h # datos de operacion

for i in range (N): # nuevo rango para matriz
    print("| ", end="")  # impresion de detalles
    for j in range(M): # nuevo rango 
        print(m[i][j]," | ", end="") # imprimimos el detalle y los espacios que iran entre la matriz

    print("\n") # esto nos ayuda a llevar un orden en la matriz
print("") # imoresion

if N==M: # iguales N con M
    print("La diagonal principal es:") # imprimimos mensaje


for i in range (N):# for  rango [i]
    print("    ", end="") # imprimimos detalle y espacio 
    for j in range(M): # for  rango [j]
        if i==j: # igualamos las variables de rango con if
            print(m[i][j],"     ", end="") # imprsion pra espacios y diseño
    print("\n") # imprimimos espacio para abajo
else:
   
    print("")
if N==M: # igalamos N con M

    print("La diagonal secundaria es:") # imprimimos mensaje


for i in range (N): # for para rango  en N 
    print("     ", end="") # imprimos espacios
    for j in range(M): # for para [j] en M
        if i+j==N-1: # operaciom
           print(m[i][j],"    ", end="") # imprimimmos espacios
    print("\n") # espacio para abajo
else:
    print("")

