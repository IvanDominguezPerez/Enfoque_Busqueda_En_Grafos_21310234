import heapq  # Importa la implementación de colas de prioridad de la biblioteca heapq

class Grafo:
    def __init__(self):
        self.grafo = {}  # Inicializa el grafo como un diccionario vacío

    def agregar_arista(self, u, v, peso):
        if u not in self.grafo:
            self.grafo[u] = []  # Crea una lista vacía para los vecinos del nodo u si no existe
        self.grafo[u].append((v, peso))  # Agrega una tupla (vecino, peso) a la lista de vecinos del nodo u

    def busqueda_coste_uniforme(self, inicio, objetivo):
        cola_prioridad = [(0, inicio)]  # Inicializa la cola de prioridad con una tupla (costo_acumulado, nodo_inicial)
        visitado = set()  # Conjunto para almacenar los nodos visitados
        padres = {}  # Diccionario para almacenar los nodos padres en el camino óptimo
        costos = {inicio: 0}  # Diccionario para almacenar los costos acumulados desde el nodo inicial

        while cola_prioridad:
            costo, nodo_actual = heapq.heappop(cola_prioridad)  # Extrae el nodo con el menor costo acumulado de la cola de prioridad
            visitado.add(nodo_actual)  # Marca el nodo actual como visitado

            if nodo_actual == objetivo:  # Si se alcanza el nodo objetivo, termina la búsqueda
                camino_optimo = []
                while nodo_actual != inicio:  # Reconstruye el camino óptimo retrocediendo desde el nodo objetivo
                    camino_optimo.append(nodo_actual)
                    nodo_actual = padres[nodo_actual]
                camino_optimo.append(inicio)
                camino_optimo.reverse()  # Invierte el camino para que esté en orden desde el inicio
                return camino_optimo

            for vecino, peso in self.grafo.get(nodo_actual, []):  # Recorre los vecinos del nodo actual y sus pesos
                costo_total = costo + peso  # Calcula el costo total para llegar al vecino desde el nodo actual
                if vecino not in visitado and (vecino not in costos or costo_total < costos[vecino]):
                    costos[vecino] = costo_total  # Actualiza el costo acumulado para llegar al vecino
                    padres[vecino] = nodo_actual  # Actualiza el nodo padre del vecino en el camino óptimo
                    heapq.heappush(cola_prioridad, (costo_total, vecino))  # Agrega el vecino a la cola de prioridad

        return None  # Si no se encuentra un camino, devuelve None

# Ejemplo de uso
g = Grafo()
g.agregar_arista('A', 'B', 1)
g.agregar_arista('A', 'C', 4)
g.agregar_arista('B', 'C', 2)
g.agregar_arista('B', 'D', 5)
g.agregar_arista('C', 'D', 1)
g.agregar_arista('C', 'E', 3)
g.agregar_arista('D', 'E', 1)

inicio = 'A'
objetivo = 'E'
camino_optimo = g.busqueda_coste_uniforme(inicio, objetivo)

if camino_optimo:
    print(f"Camino óptimo desde {inicio} a {objetivo}: {' -> '.join(camino_optimo)}")
else:
    print(f"No hay camino desde {inicio} a {objetivo}")
