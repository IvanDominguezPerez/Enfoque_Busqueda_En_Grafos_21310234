import numpy as np

class BlackjackEnv:
    def __init__(self):
        self.state_space = [(player_sum, dealer_showing, usable_ace) 
                            for player_sum in range(12, 22) 
                            for dealer_showing in range(1, 11) 
                            for usable_ace in [True, False]]
        self.action_space = [0, 1]  # 0: "Stick" (no pedir más cartas), 1: "Hit" (pedir otra carta)
        self.reset()

    def reset(self):
        self.player_sum = np.random.randint(12, 22)
        self.dealer_sum = np.random.randint(1, 11)
        self.usable_ace = bool(np.random.choice([0, 1]))
        return (self.player_sum, self.dealer_sum, self.usable_ace)

    def step(self, action):
        if action == 1:  # Pedir otra carta
            new_card = np.random.randint(1, 14)  # Cartas del 1 al 13
            if new_card > 10:  # Cartas de 10 a 13 tienen valor 10
                new_card = 10
            if new_card == 1:  # Si es un As
                if self.player_sum + 11 <= 21:  # Si el As no lleva a pasarse de 21
                    new_card = 11
                    self.usable_ace = True
            self.player_sum += new_card
            if self.player_sum > 21 and self.usable_ace:  # Si hay un As usable y el jugador se pasa de 21
                self.player_sum -= 10  # Convierte el As en un 1
                self.usable_ace = False
        if self.player_sum > 21:  # Si el jugador se pasa de 21, pierde
            return ((self.player_sum, self.dealer_sum, self.usable_ace), -1, True)
        if action == 0:  # Stick (no pedir más cartas)
            while self.dealer_sum < 17:  # El dealer debe pedir cartas hasta llegar a 17 o más
                new_card = np.random.randint(1, 14)
                if new_card > 10:
                    new_card = 10
                self.dealer_sum += new_card
            if self.dealer_sum > 21:  # Si el dealer se pasa de 21, el jugador gana
                return ((self.player_sum, self.dealer_sum, self.usable_ace), 1, True)
            if self.player_sum > self.dealer_sum:  # Si el jugador tiene una suma mayor que el dealer, gana
                return ((self.player_sum, self.dealer_sum, self.usable_ace), 1, True)
            if self.player_sum < self.dealer_sum:  # Si el dealer tiene una suma mayor que el jugador, pierde
                return ((self.player_sum, self.dealer_sum, self.usable_ace), -1, True)
            return ((self.player_sum, self.dealer_sum, self.usable_ace), 0, True)  # Empate
        return ((self.player_sum, self.dealer_sum, self.usable_ace), 0, False)

# Función para realizar el aprendizaje por refuerzo pasivo usando Monte Carlo
def monte_carlo(env, num_episodes):
    returns_sum = {}
    returns_count = {}
    V = {}
    for state in env.state_space:
        returns_sum[state] = 0
        returns_count[state] = 0
        V[state] = 0
    for _ in range(num_episodes):
        episode = []
        state = env.reset()
        while True:
            action = np.random.choice(env.action_space)
            next_state, reward, done = env.step(action)
            episode.append((state, action, reward))
            if done:
                break
            state = next_state
        G = 0
        for t in range(len(episode) - 1, -1, -1):
            state, action, reward = episode[t]
            G += reward
            if state not in [x[0] for x in episode[:t]]:
                returns_sum[state] += G
                returns_count[state] += 1
                V[state] = returns_sum[state] / returns_count[state]
    return V

# Crear el entorno del juego de blackjack
env = BlackjackEnv()

# Realizar el aprendizaje por refuerzo pasivo con Monte Carlo
V = monte_carlo(env, num_episodes=100000)

# Imprimir los valores de estado aprendidos
print("Valores de estado aprendidos:")
for state, value in V.items():
    print(f"Estado: {state}, Valor: {value}")
