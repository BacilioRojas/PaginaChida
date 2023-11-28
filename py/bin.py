from math import exp
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#---------------------------------------------------------

T = 6/12
r = .12
n = 2
s0 = 50
k = 52
u = 1.1
d = .9
op = 1#0 para put, 1 para call
americana = True #False para europea, True para amer



#---------------------------------------------------------
arbol= [[s0]]
for i in range(n):
    rama = []

    for j in range(len(arbol[i])):
        rama.append(arbol[i][j]*u)
    rama.append(arbol[i][len(arbol[i])-1]*d)
    arbol.append(rama)

#---------------------------------------------------------

present =exp(-1*(T/n)*r)
p = ((present**(-1))-d)/(u-d)

#---------------------------------------------------------

arbolPut=[]
ramaFinal = len(arbol[n])
rama =[]
for i in range(ramaFinal):
    rama.append(max(0,((-1)**op)*(k-arbol[n][i])))
arbolPut.append(rama)

#---------------------------------------------------------

for i in range(n):
    rama =[]
    for j in range(len(arbolPut[i])-1):
        aux =(p*arbolPut[i][j]+(1-p)*arbolPut[i][j+1])*present
        if americana:
            aux =max(aux,((-1)**op)*(k-arbol[n-i-1][j]))
        rama.append(aux)
    arbolPut.append(rama)
arbolPut.reverse()

#---------------------------------------------------------
def graficoArbol():
    # Crea un grafo dirigido
    G = nx.DiGraph()

    # Agrega nodos
    for i in range(n+1):
        for j in range(len(arbol[i])):
            G.add_node(f"{round(arbol[i][j],2)}")


    # Agrega arcos (conexiones entre nodos)
    for i in range(n):
        for j in range(len(arbol[i])):
            G.add_edge(f"{round(arbol[i][j],2)}", f"{round(arbol[i+1][j],2)}")
            G.add_edge(f"{round(arbol[i][j],2)}", f"{round(arbol[i+1][j+1],2)}")

    # Dibuja el grafo
    pos = {}
    for i in range(n+1):
        paso = (2*i)/len(arbol[i])
        for j in range(len(arbol[i])):
            pos[f"{round(arbol[i][j],2)}"]=(i,i-paso*j)


    # Define la disposición de los nodos

    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=10, font_weight="bold")
    plt.savefig("Arbol.png")
    plt.show()
#---------------------------------------------------------
def graficoArbolOpcion():
    # Crea un grafo dirigido
    G = nx.DiGraph()

    # Diccionario para rastrear nodos duplicados
    nodo_counter = {}
    label =[]
    # Agrega nodos
    for i in range(n+1):
        label.append([])
        for j in range(len(arbolPut[i])):
            valor_nodo = round(arbolPut[i][j], 2)

            # Agrega un sufijo único para evitar duplicados
            if valor_nodo in nodo_counter:
                nodo_counter[valor_nodo] += 1
                aux =nodo_counter[valor_nodo]*" "
                nombre_nodo = f"{aux}{valor_nodo}{aux}"
            else:
                nodo_counter[valor_nodo] = 0
                aux =nodo_counter[valor_nodo]*" "
                nombre_nodo = f"{aux}{valor_nodo}{aux}"

            G.add_node(nombre_nodo)
            label[i].append(nombre_nodo)

    # Agrega arcos (conexiones entre nodos)
    for i in range(n):
        for j in range(len(arbolPut[i])):
            nodo_actual = label[i][j]
            nodo_siguiente_izquierda = label[i+1][j]
            nodo_siguiente_derecha = label[i+1][j+1]

            G.add_edge(nodo_actual, nodo_siguiente_izquierda)
            G.add_edge(nodo_actual, nodo_siguiente_derecha)

    # Dibuja el grafo
    pos = {}
    for i in range(n+1):
        paso = (2*i)/len(arbolPut[i])
        for j in range(len(arbolPut[i])):
            nombre_nodo = label[i][j]
            pos[nombre_nodo] = (i, i - paso*j)

    # Define la disposición de los nodos

    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=10, font_weight="bold")

    plt.savefig("ArbolOpcion.png")
    plt.show()
#---------------------------------------------------------


