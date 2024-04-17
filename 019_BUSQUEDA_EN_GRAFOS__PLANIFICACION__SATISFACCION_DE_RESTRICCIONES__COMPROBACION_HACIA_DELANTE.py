class ComprobacionHaciaAdelante:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables  # Lista de variables del problema
        self.dominios = dominios  # Diccionario que mapea cada variable a su dominio
        self.restricciones = restricciones  # Lista de restricciones que deben satisfacerse
        self.dominios_restantes = {variable: list(dominio) for variable, dominio in dominios.items()}  # Copia de los dominios originales

    def resolver(self):
        return self.backtracking({})

    def backtracking(self, asignacion_actual):
        if len(asignacion_actual) == len(self.variables):
            return asignacion_actual  # Si todas las variables están asignadas, se ha encontrado una solución

        variable_no_asignada = self.obtener_variable_no_asignada(asignacion_actual)
        for valor in self.dominios[variable_no_asignada]:
            asignacion_actual[variable_no_asignada] = valor
            dominios_reducidos = self.comprobar_hacia_adelante(variable_no_asignada, valor)
            if dominios_reducidos is not None:
                resultado = self.backtracking(asignacion_actual)
                if resultado:
                    return resultado
            asignacion_actual.pop(variable_no_asignada)
            self.restaurar_dominios(variable_no_asignada, dominios_reducidos)
        return None

    def comprobar_hacia_adelante(self, variable, valor):
        dominios_reducidos = {}
        for restriccion in self.restricciones:
            if variable in restriccion.variables and not restriccion.comprobar(variable, valor):
                variables_afectadas = restriccion.variables - {variable}
                for variable_afectada in variables_afectadas:
                    if valor in self.dominios_restantes[variable_afectada]:
                        self.dominios_restantes[variable_afectada].remove(valor)
                        dominios_reducidos[variable_afectada] = list(self.dominios_restantes[variable_afectada])
                if not self.dominios_restantes[variable_afectada]:
                    return None  # No hay valores posibles para la variable afectada
        return dominios_reducidos

    def obtener_variable_no_asignada(self, asignacion_actual):
        for variable in self.variables:
            if variable not in asignacion_actual:
                return variable

    def restaurar_dominios(self, variable, dominios_reducidos):
        for variable_afectada, dominio_reducido in dominios_reducidos.items():
            self.dominios_restantes[variable_afectada] = dominio_reducido + [valor for valor in self.dominios[variable_afectada] if valor not in dominio_reducido]

# Ejemplo de uso
class Restriccion:
    def __init__(self, variables, funcion_comprobacion):
        self.variables = variables
        self.funcion_comprobacion = funcion_comprobacion

    def comprobar(self, variable, valor):
        return self.funcion_comprobacion(variable, valor)

def restriccion_dif_distinto(variable, valor):
    return variable != 'X' or valor != 1

def restriccion_suma_igual_10(variable, valor):
    return (variable == 'X' and valor + 5 <= 10) or (variable == 'Y' and valor + 5 <= 10)

variables = ['X', 'Y']
dominios = {'X': [1, 2, 3, 4, 5], 'Y': [1, 2, 3, 4, 5]}
restricciones = [
    Restriccion({'X'}, restriccion_dif_distinto),
    Restriccion({'X', 'Y'}, restriccion_suma_igual_10)
]

comprobacion_hacia_adelante = ComprobacionHaciaAdelante(variables, dominios, restricciones)
solucion = comprobacion_hacia_adelante.resolver()

print("Solución encontrada:", solucion)
