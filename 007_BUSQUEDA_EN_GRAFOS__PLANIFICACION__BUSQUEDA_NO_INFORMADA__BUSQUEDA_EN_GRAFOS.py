from collections import deque

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, u, v):
        if u not in self.grafo:
            self.grafo[u] = []  # Crea una lista vacía para los vecinos del nodo u si no existe
        self.grafo[u].append(v)  # Agrega una arista al grafo desde el nodo u al nodo v

    def bfs(self, inicio, objetivo):
        cola = deque([inicio])  # Cola para realizar BFS desde el nodo inicial
        visitado = set([inicio])  # Conjunto para almacenar los nodos visitados durante la búsqueda
        padres = {inicio: None}  # Diccionario para almacenar los padres de cada nodo en el camino óptimo

        while cola:
            nodo_actual = cola.popleft()  # Obtiene el nodo actual de la cola
            if nodo_actual == objetivo:  # Si se alcanza el nodo objetivo, termina la búsqueda
                break

            for vecino in self.grafo.get(nodo_actual, []):  # Recorre los vecinos del nodo actual
                if vecino not in visitado:  # Si el vecino no ha sido visitado
                    visitado.add(vecino)  # Marca el vecino como visitado
                    padres[vecino] = nodo_actual  # Almacena el nodo actual como el padre del vecino
                    cola.append(vecino)  # Agrega el vecino a la cola

        if objetivo not in padres:  # Si no se encontró un camino al objetivo
            return None

        # Reconstruye el camino óptimo retrocediendo desde el nodo objetivo hasta el inicio
        camino_optimo = []
        nodo = objetivo
        while nodo is not None:
            camino_optimo.append(nodo)
            nodo = padres[nodo]
        camino_optimo.reverse()  # Invierte el camino para que esté en orden desde el inicio
        return camino_optimo

# Ejemplo de uso
g = Grafo()
g.agregar_arista(0, 1)
g.agregar_arista(0, 2)
g.agregar_arista(1, 3)
g.agregar_arista(2, 4)
g.agregar_arista(2, 5)
g.agregar_arista(3, 6)
g.agregar_arista(3, 7)

inicio = 0
objetivo = 7

camino_optimo = g.bfs(inicio, objetivo)

if camino_optimo:
    print("Camino óptimo encontrado:", camino_optimo)
else:
    print("No se encontró un camino desde el nodo inicial al objetivo")
