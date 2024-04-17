import numpy as np
import nashpy as nash

# Definir las matrices de pagos para los dos jugadores
pago_jugador1 = np.array([[3, 0], [5, 1]])
pago_jugador2 = np.array([[3, 5], [0, 1]])

# Crear los juegos para cada jugador
juego_jugador1 = nash.Game(pago_jugador1)
juego_jugador2 = nash.Game(pago_jugador2)

# Calcular el equilibrio de Nash
equilibrio = juego_jugador1.lemke_howson_enumeration()

# Mostrar el equilibrio de Nash
print("Equilibrio de Nash:")
print(equilibrio)
