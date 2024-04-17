class CSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables  # Lista de variables del problema
        self.dominios = dominios  # Diccionario que mapea cada variable a su dominio
        self.restricciones = restricciones  # Lista de restricciones que deben satisfacerse

    def resolver(self):
        return self.backtracking({})

    def backtracking(self, asignacion_actual):
        if len(asignacion_actual) == len(self.variables):
            return asignacion_actual  # Si todas las variables están asignadas, se ha encontrado una solución

        variable_no_asignada = self.obtener_variable_no_asignada(asignacion_actual)
        for valor in self.dominios[variable_no_asignada]:
            asignacion_actual[variable_no_asignada] = valor
            if self.es_consistente(asignacion_actual):
                resultado = self.backtracking(asignacion_actual)
                if resultado:
                    return resultado
            asignacion_actual.pop(variable_no_asignada)
        return None

    def obtener_variable_no_asignada(self, asignacion_actual):
        for variable in self.variables:
            if variable not in asignacion_actual:
                return variable

    def es_consistente(self, asignacion_actual):
        for restriccion in self.restricciones:
            if not restriccion(asignacion_actual):
                return False
        return True

# Ejemplo de uso
def restriccion_dif_distinto(asignacion_actual):
    return asignacion_actual['X'] != asignacion_actual['Y']

def restriccion_suma_igual_10(asignacion_actual):
    return asignacion_actual['X'] + asignacion_actual['Y'] == 10

variables = ['X', 'Y']
dominios = {'X': [1, 2, 3, 4, 5], 'Y': [1, 2, 3, 4, 5]}
restricciones = [restriccion_dif_distinto, restriccion_suma_igual_10]

problema_csp = CSP(variables, dominios, restricciones)
solucion = problema_csp.resolver()

print("Solución encontrada:", solucion)
