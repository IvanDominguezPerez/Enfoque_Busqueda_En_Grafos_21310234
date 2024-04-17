class ProcesoDecisionMarkov:
    def __init__(self, estados, acciones, transiciones, recompensas, factor_descuento):
        self.estados = estados  # Lista de estados en el MDP
        self.acciones = acciones  # Lista de acciones posibles
        self.transiciones = transiciones  # Diccionario de transiciones, donde transiciones[(s, a)] = [(s', probabilidad)]
        self.recompensas = recompensas  # Diccionario de recompensas, donde recompensas[(s, a, s')] = recompensa
        self.factor_descuento = factor_descuento  # Factor de descuento para futuras recompensas

    def obtener_transiciones_estado_accion(self, estado, accion):
        """
        Método para obtener las transiciones posibles desde un estado dado una acción.
        :param estado: Estado actual.
        :param accion: Acción a tomar.
        :return: Lista de tuplas (estado_siguiente, probabilidad).
        """
        return self.transiciones.get((estado, accion), [])

    def obtener_recompensa_estado_accion(self, estado, accion, estado_siguiente):
        """
        Método para obtener la recompensa de una transición estado-acción-estado_siguiente.
        :param estado: Estado actual.
        :param accion: Acción a tomar.
        :param estado_siguiente: Estado siguiente.
        :return: Recompensa de la transición.
        """
        return self.recompensas.get((estado, accion, estado_siguiente), 0)

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

mdp = ProcesoDecisionMarkov(estados, acciones, transiciones, recompensas, factor_descuento)

# Ejemplo de cómo usar los métodos de la clase MDP
estado = 'B'
accion = 'ir_B'
transiciones_posibles = mdp.obtener_transiciones_estado_accion(estado, accion)
recompensa = mdp.obtener_recompensa_estado_accion(estado, accion, 'B')

print("Transiciones posibles desde el estado B con la acción ir_B:", transiciones_posibles)
print("Recompensa de la transición desde el estado B con la acción ir_B al estado B:", recompensa)
