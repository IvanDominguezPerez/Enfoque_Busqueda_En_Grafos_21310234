class IteracionValores:
    def __init__(self, estados, acciones, transiciones, recompensas, factor_descuento, epsilon):
        self.estados = estados  # Lista de estados en el MDP
        self.acciones = acciones  # Lista de acciones posibles
        self.transiciones = transiciones  # Diccionario de transiciones, donde transiciones[(s, a)] = [(s', probabilidad)]
        self.recompensas = recompensas  # Diccionario de recompensas, donde recompensas[(s, a, s')] = recompensa
        self.factor_descuento = factor_descuento  # Factor de descuento para futuras recompensas
        self.epsilon = epsilon  # Umbral de convergencia

    def iterar_valores(self):
        valores = {estado: 0 for estado in self.estados}  # Inicializa los valores de todos los estados a 0
        while True:
            delta = 0
            for estado in self.estados:
                valor_actual = valores[estado]
                valores[estado] = self.calcular_nuevo_valor(estado, valores)
                delta = max(delta, abs(valor_actual - valores[estado]))  # Calcula el cambio máximo en los valores
            if delta < self.epsilon:
                break  # Si el cambio en los valores es menor que el umbral de convergencia, se detiene la iteración
        return valores

    def calcular_nuevo_valor(self, estado, valores):
        nuevos_valores = []
        for accion in self.acciones:
            nuevo_valor_accion = 0
            for prox_estado, probabilidad in self.transiciones[(estado, accion)]:
                recompensa = self.recompensas.get((estado, accion, prox_estado), 0)
                nuevo_valor_accion += probabilidad * (recompensa + self.factor_descuento * valores[prox_estado])
            nuevos_valores.append(nuevo_valor_accion)
        return max(nuevos_valores) if nuevos_valores else 0

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

iteracion_valores = IteracionValores(estados, acciones, transiciones, recompensas, factor_descuento, epsilon)
valores_optimos = iteracion_valores.iterar_valores()

for estado, valor in valores_optimos.items():
    print(f"Valor óptimo de {estado}: {valor}")
