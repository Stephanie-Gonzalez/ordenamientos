# -*- coding: utf-8 -*-
"""

@author: sttep
"""

from random import sample 
from ordenamiento import bubble_sort, selection_sort, insertion_sort, shell_sort, merge_sort, quick_sort, heap_sort, comb_sort, cocktail_sort

lista = range(100) # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria de largo 8 para cada Ordenamiento

vector_bubble = sample(lista, 8) 
vector_selection = sample(lista, 8)
vector_insertion = sample(lista, 8) 
vector_shell = sample(lista, 8)
vector_merge = sample(lista, 8)
vector_quick = sample(lista, 8)
vector_heap = sample(lista, 8)
vector_comb = sample(lista, 8)
vector_cocktail = sample(lista, 8)


# Llamamos a las funciones de ordenamiento con las listas aleatorias creadas
bubble_sort(vector_bubble)
selection_sort(vector_selection)
insertion_sort(vector_insertion)
shell_sort(vector_shell)
merge_sort(vector_merge)
quick_sort(vector_quick)
heap_sort(vector_heap)
comb_sort(vector_comb)
cocktail_sort(vector_cocktail)