class SaltoAtrasDirigidoConflictos:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables  # Lista de variables del problema
        self.dominios = dominios  # Diccionario que mapea cada variable a su dominio
        self.restricciones = restricciones  # Lista de restricciones que deben satisfacerse
        self.asignacion = {}  # Diccionario para almacenar la asignación actual
        self.niveles_conflicto = {variable: 0 for variable in variables}  # Diccionario para almacenar el nivel de conflicto de cada variable

    def resolver(self):
        return self.backjumping({})

    def backjumping(self, asignacion_actual):
        # Si se han asignado todas las variables, se ha encontrado una solución
        if len(asignacion_actual) == len(self.variables):
            return asignacion_actual

        # Selecciona la próxima variable no asignada
        variable_no_asignada = self.obtener_variable_no_asignada(asignacion_actual)

        # Intenta asignar valores a la variable no asignada
        for valor in self.dominios[variable_no_asignada]:
            asignacion_actual[variable_no_asignada] = valor
            if self.es_consistente(asignacion_actual):
                # Si la asignación es consistente, realiza backtracking recursivamente
                resultado = self.backjumping(asignacion_actual)
                if resultado:
                    return resultado
            else:
                # Si se encuentra una inconsistencia, retrocede basado en el nivel de conflicto
                nivel_conflicto = self.obtener_nivel_conflicto(asignacion_actual)
                if nivel_conflicto > self.niveles_conflicto[variable_no_asignada]:
                    self.niveles_conflicto[variable_no_asignada] = nivel_conflicto
                    resultado = self.backjumping(asignacion_actual)
                    if resultado:
                        return resultado

            # Retrocede al eliminar la asignación actual
            asignacion_actual.pop(variable_no_asignada)
        return None

    def obtener_variable_no_asignada(self, asignacion_actual):
        # Encuentra la próxima variable no asignada
        for variable in self.variables:
            if variable not in asignacion_actual:
                return variable

    def es_consistente(self, asignacion_actual):
        # Verifica si la asignación actual es consistente con todas las restricciones
        for restriccion in self.restricciones:
            if not restriccion(asignacion_actual):
                return False
        return True

    def obtener_nivel_conflicto(self, asignacion_actual):
        # Calcula el nivel de conflicto basado en el número de restricciones incumplidas
        nivel_conflicto = 0
        for restriccion in self.restricciones:
            if not restriccion(asignacion_actual):
                nivel_conflicto += 1
        return nivel_conflicto

# Ejemplo de uso
def restriccion_suma_igual_10(asignacion_actual):
    return 'X' in asignacion_actual and 'Y' in asignacion_actual and asignacion_actual['X'] + asignacion_actual['Y'] == 10

variables = ['X', 'Y']
dominios = {'X': [1, 2, 3, 4, 5], 'Y': [1, 2, 3, 4, 5]}
restricciones = [restriccion_suma_igual_10]

salto_atras_dirigido_conflictos = SaltoAtrasDirigidoConflictos(variables, dominios, restricciones)
solucion = salto_atras_dirigido_conflictos.resolver()

print("Solución encontrada:", solucion)
