# -*- coding: utf-8 -*-
#Created on Fri Jun 17 07:44:44 2022

#@author: Kevin Llumiquinga


def isPrime():
 

    numero=2
    
    yield numero
    
    while True:
        temp=numero
        while True:
            temp+=1
            contador=1
            contador_divisores = 0
            
            while contador <= temp:
                if temp % contador  == 0:
                    contador_divisores +=1
                    
                if contador_divisores > 2:
                    break
                contador+=1
            if contador_divisores == 2:
                yield temp
g= isPrime()
primos= [next(g) for _ in range (8)]
print (primos)
def isPrime(n):
     for i in range (1,20):
         if n%i==0:
            return True
     return False
print (isPrime(8))