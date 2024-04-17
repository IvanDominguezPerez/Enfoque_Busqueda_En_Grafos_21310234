import random

class AlgoritmoGenetico:
    def __init__(self, tamano_poblacion, generar_estado, funcion_evaluacion, probabilidad_mutacion=0.1, max_iter=100):
        self.tamano_poblacion = tamano_poblacion  # Tamaño de la población
        self.generar_estado = generar_estado  # Función para generar un estado inicial
        self.funcion_evaluacion = funcion_evaluacion  # Función de evaluación para determinar la calidad de un estado
        self.probabilidad_mutacion = probabilidad_mutacion  # Probabilidad de mutación para cada gen
        self.max_iter = max_iter  # Número máximo de iteraciones permitidas
        self.poblacion = []  # Lista para almacenar la población de estados

    def buscar(self):
        # Genera la población inicial
        self.poblacion = [self.generar_estado() for _ in range(self.tamano_poblacion)]
        for _ in range(self.max_iter):
            # Evaluación de la población actual
            evaluaciones = [(estado, self.funcion_evaluacion(estado)) for estado in self.poblacion]
            # Selecciona los individuos más aptos para la reproducción
            seleccionados = self.seleccionar(evaluaciones)
            # Crea la próxima generación mediante cruces y mutaciones
            nueva_generacion = self.reproducir(seleccionados)
            # Actualiza la población con la nueva generación
            self.poblacion = nueva_generacion
            # Verifica si se alcanza un criterio de terminación (por ejemplo, una solución satisfactoria)
            if self.es_solucion():
                break
        return self.mejor_estado()

    def seleccionar(self, evaluaciones):
        # Esta función selecciona individuos para la reproducción basándose en sus evaluaciones.
        # En este ejemplo, se utiliza la selección de ruleta proporcional.
        total_evaluaciones = sum(evaluacion[1] for evaluacion in evaluaciones)
        probabilidades = [evaluacion[1] / total_evaluaciones for evaluacion in evaluaciones]
        seleccionados = random.choices(evaluaciones, weights=probabilidades, k=self.tamano_poblacion)
        return [individuo[0] for individuo in seleccionados]

    def reproducir(self, seleccionados):
        # Esta función crea una nueva generación mediante cruces y mutaciones.
        # En este ejemplo, se utiliza el cruce de un punto y la mutación de un gen.
        nueva_generacion = []
        for _ in range(self.tamano_poblacion):
            padre1, padre2 = random.choices(seleccionados, k=2)
            punto_cruce = random.randint(1, len(padre1) - 1)
            hijo = padre1[:punto_cruce] + padre2[punto_cruce:]
            hijo_mutado = self.mutar(hijo)
            nueva_generacion.append(hijo_mutado)
        return nueva_generacion

    def mutar(self, estado):
        # Esta función aplica una mutación a un estado con una cierta probabilidad.
        # En este ejemplo, se muta un gen seleccionado al azar con una pequeña variación.
        estado_mutado = list(estado)
        for i in range(len(estado_mutado)):
            if random.random() < self.probabilidad_mutacion:
                estado_mutado[i] += random.uniform(-0.1, 0.1)
        return tuple(estado_mutado)

    def es_solucion(self):
        # Esta función verifica si se ha alcanzado un criterio de terminación deseado.
        # Aquí se puede definir cualquier criterio, como encontrar una solución satisfactoria.
        # En este ejemplo, simplemente se ejecuta un número fijo de iteraciones.
        return False

    def mejor_estado(self):
        # Esta función devuelve el mejor estado encontrado en la última generación.
        return max(self.poblacion, key=self.funcion_evaluacion)

# Ejemplo de uso
def generar_estado_aleatorio():
    # Esta función genera un estado inicial aleatorio.
    return tuple(random.uniform(0, 1) for _ in range(5))

def funcion_evaluacion_ejemplo(estado):
    # Esta función de evaluación devuelve la suma de los elementos del estado.
    return sum(estado)

tamano_poblacion = 50  # Tamaño de la población
probabilidad_mutacion = 0.1  # Probabilidad de mutación
max_iter = 100  # Número máximo de iteraciones
algoritmo_genetico = AlgoritmoGenetico(tamano_poblacion, generar_estado_aleatorio, funcion_evaluacion_ejemplo, probabilidad_mutacion, max_iter)
estado_optimo = algoritmo_genetico.buscar()

print("Estado óptimo encontrado:", estado_optimo)
