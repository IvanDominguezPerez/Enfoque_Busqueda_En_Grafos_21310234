class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, u, v):
        if u not in self.grafo:
            self.grafo[u] = []  # Crea una lista vacía para los vecinos del nodo u si no existe
        self.grafo[u].append(v)  # Agrega una arista al grafo desde el nodo u al nodo v

    def bfs(self, inicio, objetivo):
        cola = [inicio]  # Cola para realizar BFS desde el nodo inicial
        visitado = set([inicio])  # Conjunto para almacenar los nodos visitados desde el nodo inicial
        while cola:
            nodo_actual = cola.pop(0)  # Obtiene el nodo actual de la cola
            if nodo_actual == objetivo:  # Verifica si se alcanzó el objetivo
                return True
            for vecino in self.grafo.get(nodo_actual, []):  # Recorre los vecinos del nodo actual
                if vecino not in visitado:  # Si el vecino no ha sido visitado
                    cola.append(vecino)  # Agrega el vecino a la cola
                    visitado.add(vecino)  # Marca el vecino como visitado
        return False  # Retorna False si no se encontró el objetivo

    def bidireccional(self, inicio, objetivo):
        cola_inicio = [inicio]  # Cola para realizar BFS desde el nodo inicial
        cola_objetivo = [objetivo]  # Cola para realizar BFS desde el nodo objetivo
        visitado_inicio = set([inicio])  # Conjunto para almacenar los nodos visitados desde el nodo inicial
        visitado_objetivo = set([objetivo])  # Conjunto para almacenar los nodos visitados desde el nodo objetivo
        while cola_inicio and cola_objetivo:
            # Realiza BFS desde el nodo inicial
            if self.bfs_extendido(cola_inicio, visitado_inicio, visitado_objetivo):
                return True
            # Realiza BFS desde el nodo objetivo
            if self.bfs_extendido(cola_objetivo, visitado_objetivo, visitado_inicio):
                return True
        return False  # Retorna False si no se encontró un camino entre el nodo inicial y el objetivo

    def bfs_extendido(self, cola, visitado, otro_visitado):
        nodo_actual = cola.pop(0)  # Obtiene el nodo actual de la cola
        if nodo_actual in otro_visitado:  # Verifica si el nodo actual fue visitado desde el otro extremo
            return True
        for vecino in self.grafo.get(nodo_actual, []):  # Recorre los vecinos del nodo actual
            if vecino not in visitado:  # Si el vecino no ha sido visitado
                cola.append(vecino)  # Agrega el vecino a la cola
                visitado.add(vecino)  # Marca el vecino como visitado
        return False  # Retorna False si no se alcanzó el objetivo desde el nodo actual

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

if g.bidireccional(inicio, objetivo):
    print("Se encontró un camino entre el nodo inicial y el objetivo")
else:
    print("No se encontró un camino entre el nodo inicial y el objetivo")
