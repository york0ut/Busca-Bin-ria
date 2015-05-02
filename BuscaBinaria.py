# -*- coding: utf-8 -*-
"""
Created on Fri May  1 10:39:22 2015

@author: davson
"""

def bsearch (List, Search):
    start = 0
    end = len(List)-1
    while start <= end:
        center = (start+end)/2
        if Search == List[center]:
            return True
        else:
            if List[center] < Search:
                start = center+1
            else:
                end = center-1
    return False                
    
while True:
    start_vec = raw_input("Digite o número inicial do vetor: ")
    final_vec = raw_input("Digite o número final do vetor: ")
    if int(final_vec) < int(start_vec):
        print("Digite um número final maior que o inicial")
    else:
        vetor = range(int(start_vec), int (final_vec)+1) #Não é incluso
        valor_procurado = raw_input("Digite o valor que deseja buscar: ")
        if bsearch(vetor, int(valor_procurado)):
            print "Achou"
        else:
            print "Não achou"