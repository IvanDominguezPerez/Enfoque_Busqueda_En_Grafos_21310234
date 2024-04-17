import random

class MinimosConflictos:
    def __init__(self, variables, dominios, restricciones, max_iter=1000):
        self.variables = variables  # Lista de variables del problema
        self.dominios = dominios  # Diccionario que mapea cada variable a su dominio
        self.restricciones = restricciones  # Lista de restricciones que deben satisfacerse
        self.max_iter = max_iter  # Número máximo de iteraciones permitidas

    def resolver(self):
        asignacion_actual = self.inicializar_asignacion()  # Asignación inicial aleatoria
        for _ in range(self.max_iter):
            if self.es_solucion(asignacion_actual):
                return asignacion_actual  # Si se alcanza una solución, se devuelve la asignación actual
            variable_conflicto = self.obtener_variable_conflicto(asignacion_actual)  # Variable que genera más conflictos
            valor = self.elegir_valor_conflicto(variable_conflicto, asignacion_actual)  # Valor que minimiza los conflictos
            asignacion_actual[variable_conflicto] = valor  # Se asigna el valor a la variable
        return None  # Si no se encuentra solución en el número máximo de iteraciones, se devuelve None

    def inicializar_asignacion(self):
        asignacion = {}
        for variable in self.variables:
            asignacion[variable] = random.choice(self.dominios[variable])  # Asignación aleatoria inicial
        return asignacion

    def es_solucion(self, asignacion_actual):
        for restriccion in self.restricciones:
            if not restriccion(asignacion_actual):  # Verifica si se cumplen todas las restricciones
                return False
        return True

    def obtener_variable_conflicto(self, asignacion_actual):
        variables_conflicto = []
        max_conflictos = float('-inf')
        for variable in self.variables:
            conflictos = self.contar_conflictos(variable, asignacion_actual)
            if conflictos > max_conflictos:
                variables_conflicto = [variable]
                max_conflictos = conflictos
            elif conflictos == max_conflictos:
                variables_conflicto.append(variable)
        return random.choice(variables_conflicto)  # Se elige aleatoriamente entre las variables con más conflictos

    def contar_conflictos(self, variable, asignacion_actual):
        conflictos = 0
        for restriccion in self.restricciones:
            if variable in restriccion.variables and not restriccion(asignacion_actual):
                conflictos += 1
        return conflictos

    def elegir_valor_conflicto(self, variable, asignacion_actual):
        valores_conflicto = []
        min_conflictos = float('inf')
        for valor in self.dominios[variable]:
            asignacion_actual[variable] = valor
            conflictos = self.contar_conflictos(variable, asignacion_actual)
            if conflictos < min_conflictos:
                valores_conflicto = [valor]
                min_conflictos = conflictos
            elif conflictos == min_conflictos:
                valores_conflicto.append(valor)
        return random.choice(valores_conflicto)  # Se elige aleatoriamente entre los valores con menos conflictos

# Ejemplo de uso
def restriccion_suma_igual_10(asignacion_actual):
    return 'X' in asignacion_actual and 'Y' in asignacion_actual and asignacion_actual['X'] + asignacion_actual['Y'] == 10

variables = ['X', 'Y']
dominios = {'X': [1, 2, 3, 4, 5], 'Y': [1, 2, 3, 4, 5]}
restricciones = [restriccion_suma_igual_10]

minimos_conflictos = MinimosConflictos(variables, dominios, restricciones)
solucion = minimos_conflictos.resolver()

print("Solución encontrada:", solucion)
