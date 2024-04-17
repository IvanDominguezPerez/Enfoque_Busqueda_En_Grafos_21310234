class POMDP:
    def __init__(self, estados, acciones, observaciones, transiciones, recompensas, observaciones_prob):
        self.estados = estados  # Lista de estados en el POMDP
        self.acciones = acciones  # Lista de acciones posibles
        self.observaciones = observaciones  # Lista de observaciones posibles
        self.transiciones = transiciones  # Diccionario de transiciones, donde transiciones[(s, a)] = [(s', probabilidad)]
        self.recompensas = recompensas  # Diccionario de recompensas, donde recompensas[(s, a, s')] = recompensa
        self.observaciones_prob = observaciones_prob  # Diccionario de probabilidades de observaciones, donde observaciones_prob[(a, s', o)] = probabilidad

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

    def obtener_probabilidad_observacion(self, accion, estado_siguiente, observacion):
        """
        Método para obtener la probabilidad de una observación dada una acción y un estado siguiente.
        :param accion: Acción tomada.
        :param estado_siguiente: Estado siguiente.
        :param observacion: Observación realizada.
        :return: Probabilidad de la observación.
        """
        return self.observaciones_prob.get((accion, estado_siguiente, observacion), 0)

# Ejemplo de uso
estados = ['A', 'B']
acciones = ['accion1', 'accion2']
observaciones = ['observacion1', 'observacion2']
transiciones = {('A', 'accion1'): [('A', 0.7), ('B', 0.3)],
                ('A', 'accion2'): [('A', 0.2), ('B', 0.8)],
                ('B', 'accion1'): [('A', 0.4), ('B', 0.6)],
                ('B', 'accion2'): [('A', 0.1), ('B', 0.9)]}
recompensas = {('A', 'accion1', 'A'): 10, ('A', 'accion1', 'B'): -1, ('A', 'accion2', 'A'): 5, ('A', 'accion2', 'B'): 0,
               ('B', 'accion1', 'A'): 2, ('B', 'accion1', 'B'): 7, ('B', 'accion2', 'A'): -3, ('B', 'accion2', 'B'): 8}
observaciones_prob = {('accion1', 'A', 'observacion1'): 0.8, ('accion1', 'A', 'observacion2'): 0.2,
                      ('accion1', 'B', 'observacion1'): 0.5, ('accion1', 'B', 'observacion2'): 0.5,
                      ('accion2', 'A', 'observacion1'): 0.3, ('accion2', 'A', 'observacion2'): 0.7,
                      ('accion2', 'B', 'observacion1'): 0.6, ('accion2', 'B', 'observacion2'): 0.4}

pomdp = POMDP(estados, acciones, observaciones, transiciones, recompensas, observaciones_prob)

# Ejemplo de cómo usar los métodos de la clase POMDP
estado = 'A'
accion = 'accion1'
transiciones_posibles = pomdp.obtener_transiciones_estado_accion(estado, accion)
recompensa = pomdp.obtener_recompensa_estado_accion(estado, accion, 'A')
probabilidad_observacion = pomdp.obtener_probabilidad_observacion(accion, 'A', 'observacion1')

print("Transiciones posibles desde el estado A con la acción accion1:", transiciones_posibles)
print("Recompensa de la transición desde el estado A con la acción accion1 al estado A:", recompensa)
print("Probabilidad de la observación observacion1 dada la acción accion1 y el estado A:", probabilidad_observacion)
