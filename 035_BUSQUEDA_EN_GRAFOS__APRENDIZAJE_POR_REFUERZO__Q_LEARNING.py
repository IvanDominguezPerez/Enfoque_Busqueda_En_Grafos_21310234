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

# Función para realizar el aprendizaje por refuerzo con Q-Learning
def q_learning(env, num_episodes, alpha, gamma, epsilon):
    Q = np.zeros((env.grid_size, env.grid_size, len(env.action_space)))  # Inicializamos los valores Q a 0
    for _ in range(num_episodes):
        state = env.reset()  # Reiniciamos el entorno para cada episodio
        done = False
        while not done:
            if np.random.rand() < epsilon:
                action = np.random.choice(range(len(env.action_space)))  # Exploración: elegir una acción aleatoria con probabilidad epsilon
            else:
                action = np.argmax(Q[state[0], state[1]])  # Explotación: elegir la mejor acción según los valores Q
            next_state, reward, done = env.step(env.action_space[action])  # Tomar la acción y obtener el próximo estado y la recompensa
            # Actualizar el valor Q del estado-acción actual
            Q[state[0], state[1], action] += alpha * (reward + gamma * np.max(Q[next_state[0], next_state[1]]) - Q[state[0], state[1], action])
            state = next_state  # Actualizar el estado actual al próximo estado
    return Q

# Crear el entorno del juego de cuadrícula
grid_size = 5
env = GridWorld(grid_size)

# Parámetros de Q-Learning
num_episodes = 1000  # Número de episodios de entrenamiento
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
epsilon = 0.1  # Probabilidad de exploración

# Realizar el aprendizaje por refuerzo con Q-Learning
Q = q_learning(env, num_episodes, alpha, gamma, epsilon)

# Imprimir los valores Q aprendidos
print("Valores Q aprendidos:")
for i in range(grid_size):
    print(Q[i])
