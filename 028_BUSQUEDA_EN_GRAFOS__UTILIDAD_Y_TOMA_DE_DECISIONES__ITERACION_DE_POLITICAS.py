class IteracionPoliticas:
    def __init__(self, estados, acciones, transiciones, recompensas, factor_descuento, epsilon):
        self.estados = estados  # Lista de estados en el MDP
        self.acciones = acciones  # Lista de acciones posibles
        self.transiciones = transiciones  # Diccionario de transiciones, donde transiciones[(s, a)] = [(s', probabilidad)]
        self.recompensas = recompensas  # Diccionario de recompensas, donde recompensas[(s, a, s')] = recompensa
        self.factor_descuento = factor_descuento  # Factor de descuento para futuras recompensas
        self.epsilon = epsilon  # Umbral de convergencia

    def iterar_politicas(self):
        politica = {estado: self.acciones[0] for estado in self.estados}  # Inicializa todas las acciones a la primera de la lista
        while True:
            valores = self.evaluar_politica(politica)  # Evalúa la utilidad de la política actual
            politica_mejorada = self.mejorar_politica(valores)  # Mejora la política en función de los valores
            if politica == politica_mejorada:
                break  # Si la política no cambia, se detiene la iteración
            politica = politica_mejorada
        return politica

    def evaluar_politica(self, politica):
        valores = {estado: 0 for estado in self.estados}  # Inicializa los valores de todos los estados a 0
        while True:
            delta = 0
            for estado in self.estados:
                valor_actual = valores[estado]
                valores[estado] = self.calcular_valor_estado(estado, politica[estado], valores)
                delta = max(delta, abs(valor_actual - valores[estado]))  # Calcula el cambio máximo en los valores
            if delta < self.epsilon:
                break  # Si el cambio en los valores es menor que el umbral de convergencia, se detiene la iteración
        return valores

    def mejorar_politica(self, valores):
        politica_mejorada = {}
        for estado in self.estados:
            mejores_acciones = [accion for accion in self.acciones if self.calcular_valor_estado(estado, accion, valores) == max([self.calcular_valor_estado(estado, a, valores) for a in self.acciones])]
            politica_mejorada[estado] = mejores_acciones[0]  # Selecciona la primera acción óptima encontrada
        return politica_mejorada

    def calcular_valor_estado(self, estado, accion, valores):
        valor_estado = 0
        for prox_estado, probabilidad in self.transiciones[(estado, accion)]:
            recompensa = self.recompensas.get((estado, accion, prox_estado), 0)
            valor_estado += probabilidad * (recompensa + self.factor_descuento * valores[prox_estado])
        return valor_estado

# Ejemplo de uso
estados = ['A', 'B', 'C']
acciones = ['ir_A', 'ir_B', 'ir_C']
transiciones = {('A', 'ir_A'): [('A', 0.8), ('B', 0.2)],
                ('A', 'ir_B'): [('A', 0.5), ('B', 0.5)],
                ('B', 'ir_B'): [('A', 0.1), ('B', 0.6), ('C', 0.3)],
                ('B', 'ir_C'): [('B', 0.7), ('C', 0.3)],
                ('C', 'ir_A'): [('C', 0.1), ('B', 0.9)],
                ('C', 'ir_C'): [('C', 0.5), ('B', 0.5)]}
recompensas = {('A', 'ir_A', 'A'): 10, ('A', 'ir_A', 'B'): -1, ('A', 'ir_B', 'A'): 0, ('A', 'ir_B', 'B'): 0,
               ('B', 'ir_B', 'A'): -1, ('B', 'ir_B', 'B'): 1, ('B', 'ir_B', 'C'): -1, ('B', 'ir_C', 'B'): 0,
               ('B', 'ir_C', 'C'): 2, ('C', 'ir_A', 'C'): -1, ('C', 'ir_A', 'B'): -1, ('C', 'ir_C', 'C'): 0,
               ('C', 'ir_C', 'B'): 1}
factor_descuento = 0.9
epsilon = 0.01

iteracion_politicas = IteracionPoliticas(estados, acciones, transiciones, recompensas, factor_descuento, epsilon)
politica_optima = iteracion_politicas.iterar_politicas()

for estado, accion in politica_optima.items():
    print(f"Política óptima en {estado}: {accion}")
