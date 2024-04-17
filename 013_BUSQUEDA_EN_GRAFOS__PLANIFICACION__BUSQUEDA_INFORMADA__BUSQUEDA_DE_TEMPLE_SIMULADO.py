import math
import random

class TempleSimulado:
    def __init__(self, estado_inicial, funcion_evaluacion, generar_vecino, temperatura_inicial, factor_enfriamiento, max_iter=100):
        self.estado_actual = estado_inicial  # Estado inicial de la búsqueda
        self.funcion_evaluacion = funcion_evaluacion  # Función de evaluación para determinar la calidad de un estado
        self.generar_vecino = generar_vecino  # Función para generar un vecino del estado actual
        self.temperatura = temperatura_inicial  # Temperatura inicial del algoritmo
        self.factor_enfriamiento = factor_enfriamiento  # Factor de enfriamiento para reducir la temperatura
        self.max_iter = max_iter  # Número máximo de iteraciones permitidas

    def buscar(self):
        mejor_estado = self.estado_actual  # Mejor estado encontrado hasta el momento
        mejor_valor = self.funcion_evaluacion(self.estado_actual)  # Valor de la función de evaluación del mejor estado
        for iteracion in range(self.max_iter):
            vecino = self.generar_vecino(self.estado_actual)  # Genera un vecino del estado actual
            valor_vecino = self.funcion_evaluacion(vecino)  # Evalúa el vecino generado
            diferencia = valor_vecino - mejor_valor
            if diferencia > 0 or random.random() < math.exp(diferencia / self.temperatura):
                # Acepta el vecino si es mejor o con una probabilidad determinada
                self.estado_actual = vecino
                mejor_estado = vecino
                mejor_valor = valor_vecino
            self.temperatura *= self.factor_enfriamiento  # Reduce la temperatura
        return mejor_estado

# Función de evaluación de ejemplo
def funcion_evaluacion_ejemplo(estado):
    # Esta función de evaluación devuelve la suma de los elementos del estado
    return sum(estado)

# Función para generar un vecino de ejemplo
def generar_vecino_ejemplo(estado):
    # Esta función genera un vecino cambiando aleatoriamente un elemento del estado
    vecino = list(estado)
    indice = random.randint(0, len(vecino) - 1)
    vecino[indice] = random.randint(0, 100)
    return tuple(vecino)

# Ejemplo de uso
estado_inicial = (0, 0, 0)  # Estado inicial arbitrario
temperatura_inicial = 1000  # Temperatura inicial del algoritmo
factor_enfriamiento = 0.95  # Factor de enfriamiento
max_iter = 1000  # Número máximo de iteraciones
temple_simulado = TempleSimulado(estado_inicial, funcion_evaluacion_ejemplo, generar_vecino_ejemplo, temperatura_inicial, factor_enfriamiento, max_iter)
estado_optimo = temple_simulado.buscar()

print("Estado óptimo encontrado:", estado_optimo)
