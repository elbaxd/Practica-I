# -*- coding: utf-8 -*-
"""Algoritmo2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JMDOaaTkbizWNLdIs6l4lC9Ua2BqJBec
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
!pip install igraph

import igraph as ig
import matplotlib.pyplot as plt

vertices = 13
edges = [(0,1),(2,1),(1,3),(3,4),(3,5),(5,6),(3,7),(7,8),(8,9),(8,10),(8,11),(11,12)]
G13 = ig.Graph(vertices, edges)


G13.vs["name"] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]



# Plot in matplotlib
# Note that attributes can be set globally (e.g. vertex_size), or set individually using arrays (e.g. vertex_color)
fig, ax = plt.subplots(figsize=(5,5))
ig.plot(
    G13,
    target=ax,
    #layout="", # print nodes in a circular layout
    vertex_size=0.1,
    vertex_color=["steelblue"],
    vertex_frame_width=4.0,
    vertex_frame_color="white",
    vertex_label=G13.vs["name"],
    vertex_label_size=20.0,
    edge_width=[2],
    edge_color=["#7142cf"]
)

layout = G13.layout(layout='auto')

Vc = layout.centroid()

print(Vc)

G13.delete_vertices(3)

# Plot in matplotlib
# Note that attributes can be set globally (e.g. vertex_size), or set individually using arrays (e.g. vertex_color)
fig, ax = plt.subplots(figsize=(5,5))
ig.plot(
    G13,
    target=ax,
    #layout="", # print nodes in a circular layout
    vertex_size=0.1,
    vertex_color=["steelblue"],
    vertex_frame_width=4.0,
    vertex_frame_color="white",
    vertex_label=G13.vs["name"],
    vertex_label_size=20.0,
    edge_width=[2],
    edge_color=["#7142cf"]
)

currentLV = 0

# Se define la funcion para el descomponer segun los centroids de un arbol, con T el arbol, currentLV el nivel del vertices en el que se hace 
# y Vc el vertice centroid
def centroidDescomposition(T,currentLV,Vc):
    currentLV +=1
    vclv = currentLV
    T.delete(Vc) # Se remueve el vertice Vc del arbol T, para crear subarboles
    
    verticesTC = verticesTC.append(Vc) # Con verticesTC los vertices del arbol que se genero gracias al centroid
    if vclv != 1:
        aristasTC = aristasTC.append((Vc,))

# ESQUELETO

# Se comienza con currentLV = 0

currentLV = 0

def centroidDecomposition(T,currentLV,Vpc):
    # Se le suma 1 a currentLV
    currentLV +=1
    # Se debe sacar el centroid de T
    Vc = T.centroid()
    # Se actualiza el LV del centroid
    Vc.lv = currentLV
    # Luego se debe descomponer el grafo o arbol T, eliminando Vc de T
    T.delete_vertices(Vc)


    # Después, se agrega el Vc a los vertices del nuevo arbol centroid
    Tc.add_vertice(Vc)

    # Se revisa que el lv del Vc no sea 1, si no lo es , se agrega una arista
    if Vc.lv != 1:
        Tc.add_edge((Vpc,Vc))
    
    # Se comienza la iteración y recursividad
    for Tree in components(T):
        if k > 1:
            centroidDecomposition(Tree, currentLV,Vc)
        else:
            V.lv = currentLV+1 # Con V los vertices del Tree actual
            Tc.add_vertice(v)
            Tc.add_edge((v,Vpc))

# ESQUELETO

def constructVP(Tc,k,Vp={}):
    # Se crean sub arboles de Tc, según cada vertice
    for vertice in vertices(Tc):
      Tc.subTree()
    # Luego se ordenan los sub arboles
    for i = 1...k:
        Vp = Vp.add_vertices(Sortv(i))