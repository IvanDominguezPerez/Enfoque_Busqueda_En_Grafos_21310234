class PropagacionRestricciones:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables  # Lista de variables del problema
        self.dominios = dominios  # Diccionario que mapea cada variable a su dominio
        self.restricciones = restricciones  # Lista de restricciones que deben satisfacerse

    def propagar_restricciones(self):
        # Inicializa los dominios restantes como una copia de los dominios originales
        dominios_restantes = {variable: list(dominio) for variable, dominio in self.dominios.items()}
        # Crea un diccionario para almacenar las restricciones por variable
        restricciones_por_variable = {variable: [] for variable in self.variables}
        # Asigna las restricciones a las variables correspondientes en el diccionario
        for restriccion in self.restricciones:
            for variable in restriccion.variables:
                restricciones_por_variable[variable].append(restriccion)
        # Itera sobre cada variable y sus restricciones asociadas para reducir los dominios
        for variable in self.variables:
            for restriccion in restricciones_por_variable[variable]:
                dominios_restantes = self.reducir_dominios(restriccion, variable, dominios_restantes)
                # Si se alcanza un dominio vacío, no hay solución
                if not dominios_restantes:
                    return None
        return dominios_restantes

    def reducir_dominios(self, restriccion, variable, dominios_restantes):
        dominios_reducidos = {}
        # Itera sobre los valores del dominio de la variable
        for valor in dominios_restantes[variable]:
            # Verifica si el valor es consistente con la restricción
            if not restriccion.comprobar(variable, valor):
                # Si no es consistente, elimina el valor del dominio
                dominios_restantes[variable].remove(valor)
                dominios_reducidos[variable] = list(dominios_restantes[variable])
        return dominios_restantes

# Ejemplo de uso
class Restriccion:
    def __init__(self, variables, funcion_comprobacion):
        self.variables = variables
        self.funcion_comprobacion = funcion_comprobacion

    def comprobar(self, variable, valor):
        # Aplica la función de comprobación de la restricción
        return self.funcion_comprobacion(variable, valor)

# Función de comprobación para una restricción específica
def restriccion_suma_igual_10(variable, valor):
    return (variable == 'X' and valor + 5 <= 10) or (variable == 'Y' and valor + 5 <= 10)

# Definición de variables, dominios y restricciones
variables = ['X', 'Y']
dominios = {'X': [1, 2, 3, 4, 5], 'Y': [1, 2, 3, 4, 5]}
restricciones = [Restriccion({'X', 'Y'}, restriccion_suma_igual_10)]

# Instancia de PropagacionRestricciones y propagación de restricciones
propagacion_restricciones = PropagacionRestricciones(variables, dominios, restricciones)
dominios_reducidos = propagacion_restricciones.propagar_restricciones()

print("Dominios reducidos:", dominios_reducidos)
