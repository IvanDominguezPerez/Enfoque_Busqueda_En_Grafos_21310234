import numpy as np

class RedBayesianaDinamica:
    def __init__(self, num_timesteps, nodos, conexiones_temporales, probabilidades_condicionales):
        self.num_timesteps = num_timesteps  # Número de pasos de tiempo en la DBN
        self.nodos = nodos  # Lista de nodos en la DBN
        self.conexiones_temporales = conexiones_temporales  # Diccionario de conexiones temporales, donde conexiones_temporales[(t, nodo)] = [nodos_siguiente_tiempo]
        self.probabilidades_condicionales = probabilidades_condicionales  # Diccionario de probabilidades condicionales, donde probabilidades_condicionales[(t, nodo)] = matriz_probabilidad

    def inferencia(self, evidencia):
        """
        Realiza inferencia en la DBN para estimar la distribución de probabilidad de las variables ocultas en el tiempo actual.
        :param evidencia: Evidencia observada en el tiempo actual, un diccionario de la forma {nodo: valor}.
        :return: Distribución de probabilidad de las variables ocultas en el tiempo actual.
        """
        distribucion_probabilidad = {}
        for nodo in self.nodos:
            distribucion_probabilidad[nodo] = np.ones(len(self.probabilidades_condicionales[(0, nodo)]))  # Inicializa la distribución de probabilidad uniformemente
        for t in range(1, self.num_timesteps):  # Comienza desde el segundo paso de tiempo
            for nodo in self.nodos:
                nodos_anteriores = self.conexiones_temporales.get((t, nodo), [])
                matriz_probabilidad = self.probabilidades_condicionales[(t, nodo)]
                for i, valor in enumerate(evidencia[nodo]):
                    if valor is not None:
                        distribucion_probabilidad[nodo][i] = 0  # Fija la probabilidad de la evidencia observada a 1
                for i, valor in enumerate(distribucion_probabilidad[nodo]):
                    if valor != 0:
                        for j, prob in enumerate(matriz_probabilidad[i]):
                            distribucion_probabilidad[nodo][i] *= prob * distribucion_probabilidad[nodos_anteriores[j]][j]
            distribucion_probabilidad = self.normalizar_distribucion(distribucion_probabilidad)
        return distribucion_probabilidad

    def normalizar_distribucion(self, distribucion):
        """
        Normaliza la distribución de probabilidad.
        :param distribucion: Distribución de probabilidad a normalizar.
        :return: Distribución de probabilidad normalizada.
        """
        for nodo in distribucion:
            distribucion[nodo] /= np.sum(distribucion[nodo])
        return distribucion

# Ejemplo de uso
num_timesteps = 3
nodos = ['A', 'B', 'C']
conexiones_temporales = {(0, 'A'): [],
                         (0, 'B'): [],
                         (0, 'C'): [],
                         (1, 'A'): ['B'],
                         (1, 'B'): ['C'],
                         (1, 'C'): [],
                         (2, 'A'): [],
                         (2, 'B'): [],
                         (2, 'C'): ['A']}
probabilidades_condicionales = {(0, 'A'): np.array([0.2, 0.8]),
                                (0, 'B'): np.array([0.6, 0.4]),
                                (0, 'C'): np.array([0.4, 0.6]),
                                (1, 'A'): np.array([[0.3, 0.7],
                                                     [0.5, 0.5]]),
                                (1, 'B'): np.array([[0.1, 0.9],
                                                     [0.7, 0.3]]),
                                (1, 'C'): np.array([[0.8, 0.2],
                                                     [0.2, 0.8]]),
                                (2, 'A'): np.array([0.2, 0.8]),
                                (2, 'B'): np.array([0.6, 0.4]),
                                (2, 'C'): np.array([0.4, 0.6])}

dbn = RedBayesianaDinamica(num_timesteps, nodos, conexiones_temporales, probabilidades_condicionales)

# Ejemplo de inferencia con evidencia observada
evidencia = {'A': [None, None, None], 'B': [1, None, None], 'C': [None, 0, None]}
distribucion_probabilidad = dbn.inferencia(evidencia)

print("Distribución de probabilidad
