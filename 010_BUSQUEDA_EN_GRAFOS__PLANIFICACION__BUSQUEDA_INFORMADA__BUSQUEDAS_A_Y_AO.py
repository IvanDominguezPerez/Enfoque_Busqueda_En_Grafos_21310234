import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, u, v, peso):
        if u not in self.grafo:
            self.grafo[u] = []
        self.grafo[u].append((v, peso))  # Agrega una arista al grafo con su peso

    def a_estrella(self, inicio, objetivo, heuristica):
        cola_prioridad = [(0, inicio)]  # Cola de prioridad para los nodos a explorar
        visitado = set()  # Conjunto para almacenar los nodos visitados durante la búsqueda
        padres = {}  # Diccionario para almacenar los padres de cada nodo en el camino óptimo
        costos = {inicio: 0}  # Diccionario para almacenar los costos acumulados desde el nodo inicial

        while cola_prioridad:
            costo_actual, nodo_actual = heapq.heappop(cola_prioridad)  # Obtiene el nodo con menor costo acumulado
            if nodo_actual == objetivo:  # Si se alcanza el nodo objetivo, termina la búsqueda
                camino_optimo = []
                while nodo_actual is not None:  # Reconstruye el camino óptimo retrocediendo desde el objetivo
                    camino_optimo.append(nodo_actual)
                    nodo_actual = padres.get(nodo_actual)
                camino_optimo.reverse()  # Invierte el camino para que esté en orden desde el inicio
                return camino_optimo

            visitado.add(nodo_actual)  # Marca el nodo actual como visitado

            for vecino, peso in self.grafo.get(nodo_actual, []):  # Recorre los vecinos del nodo actual y sus pesos
                costo_total = costos[nodo_actual] + peso  # Calcula el costo total para llegar al vecino
                if vecino not in costos or costo_total < costos[vecino]:
                    costos[vecino] = costo_total  # Actualiza el costo acumulado para llegar al vecino
                    prioridad = costo_total + heuristica(vecino, objetivo)  # Calcula la prioridad usando la heurística
                    heapq.heappush(cola_prioridad, (prioridad, vecino))  # Agrega el vecino a la cola de prioridad
                    padres[vecino] = nodo_actual  # Almacena el nodo actual como el padre del vecino

        return None  # Si no se encuentra un camino, devuelve None

    def ao_estrella(self, inicio, objetivo, heuristica, epsilon=1):
        cola_prioridad = [(0, inicio)]  # Cola de prioridad para los nodos a explorar
        visitado = set()  # Conjunto para almacenar los nodos visitados durante la búsqueda
        padres = {}  # Diccionario para almacenar los padres de cada nodo en el camino óptimo
        costos = {inicio: 0}  # Diccionario para almacenar los costos acumulados desde el nodo inicial

        while cola_prioridad:
            costo_actual, nodo_actual = heapq.heappop(cola_prioridad)  # Obtiene el nodo con menor costo acumulado
            if nodo_actual == objetivo:  # Si se alcanza el nodo objetivo, termina la búsqueda
                camino_optimo = []
                while nodo_actual is not None:  # Reconstruye el camino óptimo retrocediendo desde el objetivo
                    camino_optimo.append(nodo_actual)
                    nodo_actual = padres.get(nodo_actual)
                camino_optimo.reverse()  # Invierte el camino para que esté en orden desde el inicio
                return camino_optimo

            visitado.add(nodo_actual)  # Marca el nodo actual como visitado

            for vecino, peso in self.grafo.get(nodo_actual, []):  # Recorre los vecinos del nodo actual y sus pesos
                costo_total = costos[nodo_actual] + peso  # Calcula el costo total para llegar al vecino
                if vecino not in costos or costo_total < costos[vecino]:
                    costos[vecino] = costo_total  # Actualiza el costo acumulado para llegar al vecino
                    prioridad = costo_total + heuristica(vecino, objetivo) * epsilon  # Calcula la prioridad ajustada por epsilon
                    heapq.heappush(cola_prioridad, (prioridad, vecino))  # Agrega el vecino a la cola de prioridad
                    padres[vecino] = nodo_actual  # Almacena el nodo actual como el padre del vecino

        return None  # Si no se encuentra un camino, devuelve None

# Ejemplo de uso
g = Grafo()
g.agregar_arista('A', 'B', 4)
g.agregar_arista('A', 'C', 2)
g.agregar_arista('B', 'C', 5)
g.agregar_arista('B', 'D', 10)
g.agregar_arista('C', 'D', 3)
g.agregar_arista('D', 'E', 7)

def heuristica_simple(nodo, objetivo):
    # Se puede utilizar una heurística simple, como la distancia Manhattan, la distancia Euclidiana, etc.
    # En este caso, se utiliza la distancia en línea recta entre los nodos como la heurística
    dist_x = abs(ord(nodo[0]) - ord(objetivo[0]))
    dist_y = abs(int(nodo[1]) - int(objetivo[1]))
    return dist_x + dist_y

inicio = 'A'
objetivo = 'E'

# Ejemplo de búsqueda A*
camino_optimo_a_estrella = g.a_estrella(inicio, objetivo, heuristica_simple)

if camino_optimo_a_estrella:
    print("Camino óptimo encontrado con A*:", camino_optimo_a_estrella)
else:
    print("No se encontró un camino desde el nodo inicial al objetivo con A*")

# Ejemplo de búsqueda AO*
epsilon = 1.5  # Valor de epsilon, puede ajustarse según se desee
camino
