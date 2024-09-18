#Practica: 007_BUSQUEDA_EN_GRAFOS__PLANIFICACION__BUSQUEDA_NO_INFORMADA__BUSQUEDA_EN_GRAFOS
#Alumno: IVAN_DOMINGUEZ
#Registro: 21310234
#Grupo: 7F1

from collections import deque  # Importamos deque para manejar la cola de la búsqueda en anchura

# Definimos un grafo simple que representa una ciudad
# Cada nodo representa una ubicación y las conexiones (aristas) representan las rutas entre las ubicaciones
grafo_ciudad = {
    'Casa': ['Supermercado', 'Parque', 'Cafetería'],
    'Supermercado': ['Casa', 'Gimnasio'],
    'Parque': ['Casa', 'Cafetería', 'Museo'],
    'Cafetería': ['Casa', 'Parque', 'Teatro'],
    'Gimnasio': ['Supermercado', 'Hospital'],
    'Museo': ['Parque', 'Hospital'],
    'Teatro': ['Cafetería'],
    'Hospital': ['Gimnasio', 'Museo']
}

# Función que implementa la búsqueda en anchura (BFS)
def busqueda_en_anchura(grafo, inicio, objetivo):
    # Cola para almacenar los nodos a explorar. Usamos deque para optimizar las operaciones de cola.
    cola = deque([inicio])  # Iniciamos con el nodo de inicio
    # Diccionario para llevar registro de los nodos visitados y sus predecesores (para reconstruir el camino)
    visitados = {inicio: None}
    
    # Mientras la cola no esté vacía, seguimos explorando
    while cola:
        nodo_actual = cola.popleft()  # Extraemos el primer nodo de la cola (FIFO)
        
        # Si encontramos el nodo objetivo, detenemos la búsqueda
        if nodo_actual == objetivo:
            return reconstruir_camino(visitados, inicio, objetivo)  # Llamamos a una función para reconstruir el camino
        
        # Exploramos los nodos vecinos (conectados) al nodo actual
        for vecino in grafo[nodo_actual]:
            if vecino not in visitados:  # Solo visitamos nodos no visitados
                visitados[vecino] = nodo_actual  # Guardamos de dónde venimos (predecesor)
                cola.append(vecino)  # Añadimos el vecino a la cola para explorarlo más adelante

    return None  # Si no encontramos el objetivo, devolvemos None

# Función para reconstruir el camino desde el inicio hasta el objetivo
def reconstruir_camino(visitados, inicio, objetivo):
    camino = []  # Lista para almacenar el camino
    nodo_actual = objetivo  # Empezamos desde el objetivo
    
    # Retrocedemos a través del diccionario de predecesores hasta llegar al inicio
    while nodo_actual is not None:
        camino.append(nodo_actual)
        nodo_actual = visitados[nodo_actual]  # Nos movemos al nodo predecesor
    
    # Invertimos el camino, ya que lo reconstruimos desde el objetivo al inicio
    camino.reverse()
    return camino

# Función principal
if __name__ == "__main__":
    inicio = 'Casa'  # Definimos el nodo de inicio
    objetivo = 'Hospital'  # Definimos el nodo objetivo
    
    # Llamamos a la función de búsqueda en anchura
    camino = busqueda_en_anchura(grafo_ciudad, inicio, objetivo)
    
    # Imprimimos el resultado
    if camino:
        print(f'Camino desde {inicio} hasta {objetivo}: {camino}')
    else:
        print(f'No se encontró un camino desde {inicio} hasta {objetivo}.')

#El algoritmo de Búsqueda en Anchura es un algoritmo de búsqueda no informada que explora
#todos los nodos vecinos a una profundidad fija antes de moverse a la siguiente. Es útil cuando
#buscamos el camino más corto en términos de número de pasos, pero sin tener información sobre
#las distancias o costos. En este ejemplo, aplicamos BFS para encontrar el camino más corto entre dos
#ubicaciones en una ciudad representada por un grafo.

#Este enfoque es aplicable a la vida cotidiana en situaciones como la búsqueda de rutas en mapas,
#planificación de rutas de transporte, o cualquier otro problema que pueda modelarse como un
#grafo.
