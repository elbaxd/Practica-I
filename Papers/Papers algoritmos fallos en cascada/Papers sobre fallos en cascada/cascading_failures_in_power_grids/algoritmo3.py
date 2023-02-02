# -*- coding: utf-8 -*-
"""Algoritmo3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18K2CZauxskDEgBHK_15ndSz0hoL9MRK-
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
!pip install igraph

import igraph as ig
import matplotlib.pyplot as plt

# ESQUELETO

def CFE(G,F0):
    F*= F0
    i = 0
    while Fi != None:
        # Ajustar la demanda total igual a al total supply en cada componente conectado

        #Computar los nuevos flujos 

        # Encontrar el nuevo set de aristas que fallan

    return t=i-1 , (F0,...,Ft) , fe(f*t) # Para cada e en las aristas menos las aristas que fallan

def CFEPB(G,F0):
    # Se computa A+
    F*=0
    i=0
    while Fi != None:
        for arista in Fi:
            if arista is a cut-edge: # Lemma 1
                delete_edge(arista)
                components(G)
                # Ajustar la demanda al supply en cada componente
              
            else:
                delete_edge(arista) # Lemma 4
                # Update A+ despues
    # Computar los angulos 0 = A^+ P
    # Computar los nuevos flujos de los angulos de fase
    # Encontrar el nuevo set de aristas que fallan
    return t=i-1, (F0,...,Fi), fe(f*t)

def MVESRB(G,k):
    # Computar A+
    # Computar angulos de fase Θ =A^+ P y los flujos de los angulos de fase
    # Computar la distancia de resistencia r(i,j)= r(e), para todo e=(i,j) de E
    # Ordenar las aristas (Sort edges) tal que p<=q si solo si f(ep)r(ep) = f(eq)r(eq)
    return e1,e2,...,ek