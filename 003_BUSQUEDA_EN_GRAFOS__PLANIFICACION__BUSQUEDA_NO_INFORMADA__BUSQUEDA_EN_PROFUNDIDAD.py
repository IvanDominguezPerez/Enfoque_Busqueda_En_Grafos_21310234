class Grafo:
    def __init__(self):
        self.grafo = {}  # Inicializa el grafo como un diccionario vacío

    def agregar_arista(self, u, v):
        if u not in self.grafo:
            self.grafo[u] = []  # Crea una lista vacía para los vecinos del nodo u si no existe
        self.grafo[u].append(v)  # Agrega una arista al grafo desde el nodo u al nodo v

    def dfs(self, inicio, visitado=None):
        if visitado is None:
            visitado = set()  # Inicializa el conjunto de nodos visitados en la primera llamada a la función

        visitado.add(inicio)  # Marca el nodo actual como visitado
        print(inicio, end=" ")  # Imprime el nodo actual

        for vecino in self.grafo.get(inicio, []):  # Recorre los vecinos del nodo actual
            if vecino not in visitado:  # Si el vecino no ha sido visitado
                self.dfs(vecino, visitado)  # Realiza DFS desde el vecino, llamando recursivamente a la función

# Ejemplo de uso
g = Grafo()
g.agregar_arista(0, 1)
g.agregar_arista(0, 2)
g.agregar_arista(1, 2)
g.agregar_arista(2, 0)
g.agregar_arista(2, 3)
g.agregar_arista(3, 3)

print("Recorrido DFS comenzando desde el nodo 2:")
g.dfs(2)
