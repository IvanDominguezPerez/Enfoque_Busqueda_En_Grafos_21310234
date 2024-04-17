import numpy as np

class GridWorld:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.state_space = [(i, j) for i in range(grid_size) for j in range(grid_size)]
        self.action_space = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Derecha, Izquierda, Abajo, Arriba
        self.start_state = (0, 0)
        self.goal_state = (grid_size - 1, grid_size - 1)
        self.current_state = self.start_state
        self.done = False

    def reset(self):
        self.current_state = self.start_state
        self.done = False
        return self.current_state

    def step(self, action):
        if self.done:
            return self.current_state, 0, self.done
        next_state = (self.current_state[0] + action[0], self.current_state[1] + action[1])
        if next_state[0] < 0 or next_state[0] >= self.grid_size or next_state[1] < 0 or next_state[1] >= self.grid_size:
            return self.current_state, -1, self.done
        self.current_state = next_state
        if next_state == self.goal_state:
            self.done = True
            return next_state, 1, self.done
        return next_state, 0, self.done

# Función para realizar la búsqueda de política utilizando la estrategia de valor de acción
def policy_search(Q):
    policy = np.zeros((Q.shape[0], Q.shape[1]), dtype=int)  # Inicializamos la política como una matriz de ceros
    for i in range(Q.shape[0]):
        for j in range(Q.shape[1]):
            policy[i, j] = np.argmax(Q[i, j])  # Para cada estado, elegimos la acción con el mayor valor Q
    return policy

# Crear el entorno del juego de cuadrícula
grid_size = 5
env = GridWorld(grid_size)

# Crear una matriz Q vacía para almacenar los valores Q de cada estado y acción
Q = np.random.rand(grid_size, grid_size, len(env.action_space))

# Realizar la búsqueda de política utilizando la estrategia de valor de acción
policy = policy_search(Q)

# Imprimir la política aprendida
print("Política aprendida:")
for i in range(grid_size):
    print(policy[i])
