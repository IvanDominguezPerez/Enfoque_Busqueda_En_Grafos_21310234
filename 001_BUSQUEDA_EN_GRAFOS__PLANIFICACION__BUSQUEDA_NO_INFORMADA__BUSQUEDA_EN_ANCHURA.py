from collections import defaultdict, deque  # Importa las clases defaultdict y deque de la biblioteca collections

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)  # Inicializa un diccionario que almacenará las listas de adyacencia de cada nodo

    def agregar_arista(self, u, v):
        self.grafo[u].append(v)  # Añade una arista (u, v) al grafo

    def bfs(self, inicio):
        visitado = [False] * (max(self.grafo) + 1)  # Crea una lista de booleanos para marcar los nodos visitados
        cola = deque()  # Inicializa una cola vacía para BFS

        cola.append(inicio)  # Agrega el nodo de inicio a la cola
        visitado[inicio] = True  # Marca el nodo de inicio como visitado

        while cola:  # Mientras haya nodos en la cola
            nodo = cola.popleft()  # Obtiene el primer nodo de la cola
            print(nodo, end=" ")  # Imprime el nodo visitado

            for vecino in self.grafo[nodo]:  # Recorre los nodos vecinos del nodo actual
                if not visitado[vecino]:  # Si el vecino no ha sido visitado
                    cola.append(vecino)  # Agrega el vecino a la cola
                    visitado[vecino] = True  # Marca el vecino como visitado

# Ejemplo de uso
g = Grafo()  # Crea un objeto de la clase Grafo
g.agregar_arista(0, 1)  # Agrega una arista (0, 1)
g.agregar_arista(0, 2)  # Agrega una arista (0, 2)
g.agregar_arista(1, 2)  # Agrega una arista (1, 2)
g.agregar_arista(2, 0)  # Agrega una arista (2, 0)
g.agregar_arista(2, 3)  # Agrega una arista (2, 3)
g.agregar_arista(3, 3)  # Agrega una arista (3, 3)

print("Recorrido BFS comenzando desde el nodo 2:")
g.bfs(2)  # Realiza un recorrido BFS comenzando desde el nodo 2

