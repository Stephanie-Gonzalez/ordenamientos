# -*- coding: utf-8 -*-
"""

@author: sttep
"""

from random import sample 



def bubble_sort(vector):
    """Esta función ordenará el vector que le pases como argumento
    con el método de Bubble Sort"""
    
    print("----------------------------------------------------------------------")
    print("El vector a ordenar con bubble es:", vector)
    
    n = 0 # Establecemos un contador del largo del vector
    
    for _ in vector:
        n += 1 #Contamos la cantidad de caracteres dentro del vector
    
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            # Revisa la matriz de 0 hasta n-i-1
            if vector[j] > vector[j+1] :
                vector[j], vector[j+1] = vector[j+1], vector[j]
            # Se intercambian si el elemento encontrado es mayor 
            # Luego pasa al siguiente
            
    print ("El vector ordenado con bubble es: ", vector)


def selection_sort(vector):
    """Esta función ordenará el vector que le pases como argumento 
    con el método Selection Sort"""
    
    print("----------------------------------------------------------------------")
    print ("El vector a ordenar con selección es:", vector)
    
    largo = 0 # Establecemos un contador del largo
    
    for _ in vector:
        largo += 1 # Obtenemos el largo del vector
        
    for i in range(largo): 
      
       
        minimo = i 
        for j in range(i+1, largo): 
            if vector[minimo] > vector[j]: 
                minimo = j 
                
        
        vector[i], vector[minimo] = vector[minimo], vector[i]
        # Repetimos el proceso hasta terminar
    print("El vector ordenado con selección es: ", vector)

def insertion_sort(vector): 
    """Esta función ordenará el vector que le pases como argumento 
    con el método Insertion Sort"""
    
    print("----------------------------------------------------------------------")
    print("El vector a ordenar con inserción es:", vector)
    
    largo = len(vector) # Obtenemos el largo del vector
     
    # Recorremos la lista de 1 hasta el largo del vector
    for i in range(1, largo): 
    
        elemento = vector[i] 
  
        # Movemos los elementos de vector[0...i-1], que son mayores que el elemento a una posición adelante de su posición actual
        j = i-1
        while j >= 0 and elemento < vector[j] : 
            vector[j+1] = vector[j] 
            j -= 1
        vector[j+1] = elemento 
        
    print("El vector ordenado con inserción es: ", vector)
    
def shell_sort(vector_shell):
    # Aquí comienza el bloque de la función, indentado con cuatro espacios.
    n = len(vector_shell)
    espacio = n // 2
    while espacio > 0:
        for i in range(espacio, n):
            temp = vector_shell[i]
            j = i
            while j >= espacio and vector_shell[j - espacio] > temp:
                vector_shell[j] = vector_shell[j - espacio]
                j -= espacio
            vector_shell[j] = temp
        espacio //= 2
    return vector_shell
    # Aquí termina el bloque de la función, también indentado con cuatro espacios.

def merge_sort(vector_merge): 
    """Esta función ordenara el vector que le pases como argumento 
    con el metodo Merge Sort"""
    
    print("----------------------------------------------------------------------")
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con merge es:", vector_merge)
    
    def merge(vectormerge):
    
        def largo(vec):
                largovec = 0 # Establecemos un contador del largovec
                for _ in vec:
                    largovec += 1 # Obtenemos el largo del vector
                return largovec
        
        
        if largo(vectormerge) >1: 
            medio = largo(vectormerge)//2 # Buscamos el medio del vector
            
            # Lo dividimos en 2 partes 
            izq = vectormerge[:medio]  
            der = vectormerge[medio:]
            
            merge(izq) # Mismo procedimiento a la primer mitad
            merge(der) # Mismo procedimiento a la segunda mitad
            
            i = j = k = 0
            
            # Copiamos los datos a los vectores temporales izq[] y der[] 
            while i < largo(izq) and j < largo(der): 
                if izq[i] < der[j]: 
                    vectormerge[k] = izq[i] 
                    i+= 1
                else: 
                    vectormerge[k] = der[j] 
                    j+= 1
                k += 1
            
            # Nos fijamos si quedaron elementos en la lista
            # tanto derecha como izquierda 
            while i < largo(izq): 
                vectormerge[k] = izq[i] 
                i+= 1
                k+= 1
            
            while j < largo(der): 
                vectormerge[k] = der[j] 
                j+= 1
                k+= 1
    merge(vector_merge)
    print("El vector ordenado con merge es: ", vector_merge)
    
def quick_sort(vector_quick, start = 0, end = len(vector_quick) - 1 ):
    """Esta función ordenara el vector que le pases como argumento 
    con el metodo Quick Sort"""
    print("----------------------------------------------------------------------")
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con quick es:", vector_quick)
    
    def quick(vector_quick, start = 0, end = len(vector_quick) - 1):
        
        
        if start >= end:
            return

        def particion(vector_quick, start=0, end=len(vector_quick)-1):
            pivot = vector_quick[start]
            menor = start + 1
            mayor = end

            while True:
                while menor <= mayor and vector_quick[mayor] >= pivot:
                    mayor = mayor - 1

                while menor <= mayor and vector_quick[menor] <= pivot:
                    menor = menor + 1
                
                if menor <= mayor:
                    vector_quick[menor], vector_quick[mayor] = vector_quick[mayor], vector_quick[menor]
                
                else:
                    break

            vector_quick[start], vector_quick[mayor] = vector_quick[mayor], vector_quick[start]

            return mayor
        
        p = particion(vector_quick, start, end)
        quick(vector_quick, start, p-1)
        quick(vector_quick, p+1, end)
        
    quick(vector_quick)
    print("El vector ordenado con quick es:", vector_quick)
    
def heap_sort(vectorheap):
    """Esta función ordenara el vector que le pases como argumento 
    con el metodo Heap Sort"""
    
    print("----------------------------------------------------------------------")
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con heap es:", vectorheap)

    largo = 0 # Establecemos un contador del largo
        
    for _ in vectorheap:
        largo += 1 # Obtenemos el largo del vector

    # Para amontonar la subparte a partir de i. 
    # n es el tamaño del montón.
    def amontonar(vectorheap, n, i): 
        mas_largo = i # Tomamos i como el más grande 
        izq = 2 * i + 1      
        der = 2 * i + 2    
    
        
        if izq < n and vectorheap[i] < vectorheap[izq]: 
            mas_largo = izq 
    
        # Ver si existe la subparte de i correctamente y 
        # si es mayor que i
        if der < n and vectorheap[mas_largo] < vectorheap[der]: 
            mas_largo = der 
            
    
        if mas_largo != i: 
            vectorheap[i],vectorheap[mas_largo] = vectorheap[mas_largo],vectorheap[i]
            # Cambiar el origen, si es necesario
            # amontonar el origen. 
            amontonar(vectorheap, n, mas_largo)
            
    def heap(vectorheap):
        
        n = largo
        # Crear un montón maximo 
        for i in range(n//2 - 1, -1, -1): 
            amontonar(vectorheap, n, i) 
    
        # Extraer elementos uno a uno
        for i in range(n-1, 0, -1): 
            vectorheap[i], vectorheap[0] = vectorheap[0], vectorheap[i] 
            # Intercambio 
            amontonar(vectorheap, i, 0)
        
    heap(vectorheap)
    print("El vector ordenado con heap es:", vectorheap)
    
def comb_sort(vectorcomb):
    """Esta función ordenara el vector que le pases como argumento
    con el metodo de Comb Sort"""
    
    
    print("----------------------------------------------------------------------")
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con comb es:",vectorcomb)
    
    largo = 0 # Establecemos un contador del largo del vector
    
    for _ in vectorcomb:
        largo += 1
    
    
    # Comenzamos con la diferencia o distancia igual al largo del vector
    diferencia = largo
    
    # Establecemos la variable que define si es necesario o no
    #  intercambiar los numeros que se están comparando
    cambiar = True
    
    while diferencia > 1 or cambiar:
        diferencia = max(1, int(diferencia / 1.25))  
        # La diferencia minima es 1
        # En cada iteración vamos bajando la diferencia
        cambiar = False
        for i in range(largo - diferencia):
            j = i+diferencia 
            # Ubicamos el número que está a la distancia x de i
            if vectorcomb[i] > vectorcomb[j]:
                vectorcomb[i], vectorcomb[j] = vectorcomb[j], vectorcomb[i]
                # Hacemos el intercambio de los numeros
                cambiar = True
    
    print("El vector ordenado con comb es: ",vectorcomb)

def cocktail_sort(vectorcocktail):
    """Esta función ordenara el vector que le pases como argumento
    con el metodo de Cocktail Sort"""
    
    print("----------------------------------------------------------------------")
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con cocktail es:",vectorcocktail)
    
    largo = 0 # Establecemos un contador del largo
    
    for _ in vectorcocktail:
        largo += 1 # Obtenemos el largo del vector
    
    for i in range(largo//2): # Comenzamos desde la mitad aprox
        cambiar = False 
        # Declaramos la variable que inidica si es necesario intercambiar o no 
        for j in range(1+i, largo-i):
            # Probar si los dos elementos están en el orden incorrecto
            if vectorcocktail[j] < vectorcocktail[j-1]:
                # Entonces ambos elementos cambian de lugar
                vectorcocktail[j], vectorcocktail[j-1] = vectorcocktail[j-1], vectorcocktail[j]
                cambiar = True
        # Si no ocurren cambios salimos del bucle
        if not cambiar:
            break
        cambiar = False
        for j in range(largo-i-1, i, -1):
            # Probar si los dos elementos están en el orden incorrecto
            if vectorcocktail[j] < vectorcocktail[j-1]:
                # Entonces ambos elementos cambian de lugar
                vectorcocktail[j], vectorcocktail[j-1] = vectorcocktail[j-1], vectorcocktail[j]
                cambiar = True
        if not cambiar:
            break
    print("El vector ordenado con cocktail es: ",vectorcocktail)
    print("----------------------------------------------------------------------")