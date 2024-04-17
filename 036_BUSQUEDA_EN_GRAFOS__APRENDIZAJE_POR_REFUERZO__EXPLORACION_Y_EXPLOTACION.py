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

# Función para realizar la exploración y explotación con la regla epsilon-greedy
def epsilon_greedy(Q, state, epsilon):
    if np.random.rand() < epsilon:
        action = np.random.choice(len(Q[state[0], state[1]]))  # Exploración: elige una acción aleatoria
    else:
        action = np.argmax(Q[state[0], state[1]])  # Explotación: elige la mejor acción según los valores Q
    return action

# Crear el entorno del juego de cuadrícula
grid_size = 5
env = GridWorld(grid_size)

# Parámetros de exploración y explotación
epsilon = 0.1  # Probabilidad de exploración

# Crear una matriz Q vacía para almacenar los valores Q de cada estado y acción
Q = np.zeros((grid_size, grid_size, len(env.action_space)))

# Realizar varias iteraciones de exploración y explotación
num_iterations = 100
for _ in range(num_iterations):
    state = env.reset()
    done = False
    while not done:
        action = epsilon_greedy(Q, state, epsilon)  # Determinar la acción usando epsilon-greedy
        next_state, reward, done = env.step(env.action_space[action])
        # Actualizar los valores Q según la recompensa obtenida
        Q[state[0], state[1], action] += reward
        state = next_state

# Imprimir los valores Q aprendidos
print("Valores Q aprendidos:")
for i in range(grid_size):
    print(Q[i])
