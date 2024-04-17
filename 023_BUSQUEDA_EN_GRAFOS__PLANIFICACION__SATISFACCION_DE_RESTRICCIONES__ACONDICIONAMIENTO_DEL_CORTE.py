class AcondicionamientoCorte:
    def __init__(self, variables, restricciones):
        self.variables = variables  # Lista de variables del problema
        self.restricciones = restricciones  # Lista de restricciones que deben satisfacerse

    def encontrar_corte_minimo(self):
        corte_minimo = self.variables[:]  # Crea una copia de todas las variables
        for variable in self.variables:
            corte = self.calcula_corte(variable)  # Calcula el corte para cada variable
            if len(corte) < len(corte_minimo):  # Actualiza el corte mínimo si es necesario
                corte_minimo = corte
        return corte_minimo

    def calcula_corte(self, variable):
        corte = set()
        visitados = set()
        pendientes = [variable]  # Inicializa la lista de variables pendientes de explorar
        while pendientes:
            actual = pendientes.pop()  # Toma la variable actual
            if actual not in visitados:
                visitados.add(actual)
                for restriccion in self.restricciones:
                    if actual in restriccion.variables:  # Verifica si la variable está en una restricción
                        corte |= restriccion.variables - {actual}  # Añade todas las variables de la restricción excepto la actual al corte
                        for vecino in restriccion.variables - {actual}:
                            if vecino not in visitados:  # Añade los vecinos no visitados a la lista de pendientes
                                pendientes.append(vecino)
        return list(corte)

# Ejemplo de uso
class Restriccion:
    def __init__(self, variables):
        self.variables = set(variables)  # Conjunto de variables involucradas en la restricción

# Definición de variables y restricciones
variables = ['A', 'B', 'C', 'D']
restricciones = [
    Restriccion(['A', 'B']),
    Restriccion(['B', 'C']),
    Restriccion(['C', 'D'])
]

acondicionamiento_corte = AcondicionamientoCorte(variables, restricciones)
corte_minimo = acondicionamiento_corte.encontrar_corte_minimo()

print("Corte mínimo encontrado:", corte_minimo)
