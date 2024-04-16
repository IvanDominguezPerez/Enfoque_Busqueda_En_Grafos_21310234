class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, u, v):
        if u not in self.grafo:
            self.grafo[u] = []  # Crea una lista vacía para los vecinos del nodo u si no existe
        self.grafo[u].append(v)  # Agrega una arista al grafo desde el nodo u al nodo v

    def dfs_limitado(self, inicio, objetivo, profundidad_max):
        visitado = set()  # Conjunto para almacenar los nodos visitados
        pila = [(inicio, 0)]  # Pila para realizar DFS con una profundidad máxima
        while pila:
            nodo, profundidad = pila.pop()  # Obtiene el nodo y la profundidad actual de la pila
            visitado.add(nodo)  # Marca el nodo como visitado
            if nodo == objetivo:  # Verifica si se alcanzó el objetivo
                return True
            if profundidad < profundidad_max:  # Verifica si la profundidad es menor que la máxima permitida
                for vecino in self.grafo.get(nodo, []):  # Recorre los vecinos del nodo actual
                    if vecino not in visitado:  # Si el vecino no ha sido visitado
                        pila.append((vecino, profundidad + 1))  # Agrega el vecino a la pila con una profundidad incrementada
        return False  # Retorna False si no se encontró el objetivo dentro de la profundidad máxima

    def iddfs(self, inicio, objetivo):
        profundidad_max = 0  # Inicializa la profundidad máxima en 0
        while True:
            if self.dfs_limitado(inicio, objetivo, profundidad_max):  # Realiza DFS limitado con la profundidad máxima actual
                return profundidad_max  # Retorna la profundidad máxima si se encuentra el objetivo
            profundidad_max += 1  # Incrementa la profundidad máxima para la siguiente iteración

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

profundidad_max_encontrada = g.iddfs(inicio, objetivo)
print("La profundidad máxima encontrada para llegar al objetivo es:", profundidad_max_encontrada)
