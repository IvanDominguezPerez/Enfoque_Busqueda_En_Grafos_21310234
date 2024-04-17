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

# Función para realizar el aprendizaje por refuerzo activo usando Q-learning
def q_learning(env, num_episodes, alpha, gamma, epsilon):
    Q = np.zeros((env.grid_size, env.grid_size, len(env.action_space)))
    for _ in range(num_episodes):
        state = env.reset()
        done = False
        while not done:
            if np.random.rand() < epsilon:
                action = np.random.choice(range(len(env.action_space)))
            else:
                action = np.argmax(Q[state[0], state[1]])
            next_state, reward, done = env.step(env.action_space[action])
            Q[state[0], state[1], action] += alpha * (reward + gamma * np.max(Q[next_state[0], next_state[1]]) - Q[state[0], state[1], action])
            state = next_state
    return Q

# Crear el entorno del juego de cuadrícula
grid_size = 5
env = GridWorld(grid_size)

# Parámetros de Q-learning
num_episodes = 1000
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
epsilon = 0.1  # Probabilidad de exploración

# Realizar el aprendizaje por refuerzo activo con Q-learning
Q = q_learning(env, num_episodes, alpha, gamma, epsilon)

# Imprimir la política óptima aprendida
optimal_policy = np.argmax(Q, axis=2)
print("Política óptima aprendida:")
for i in range(grid_size):
    print(optimal_policy[i])
