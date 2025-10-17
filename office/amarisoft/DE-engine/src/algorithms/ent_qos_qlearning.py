import numpy as np
import random

class QAgent:
    def __init__(self, n_actions, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.n_actions = n_actions

    def _get_state_key(self, state):
        return tuple(np.round(state, 1))  # simple discretization

    def choose_action(self, state):
        key = self._get_state_key(state)
        if random.random() < self.epsilon or key not in self.q_table:
            return random.randint(0, self.n_actions - 1)
        return np.argmax(self.q_table[key])

    def update(self, state, action, reward, next_state):
        key = self._get_state_key(state)
        next_key = self._get_state_key(next_state)
        self.q_table.setdefault(key, np.zeros(self.n_actions))
        self.q_table.setdefault(next_key, np.zeros(self.n_actions))
        best_next = np.max(self.q_table[next_key])
        self.q_table[key][action] += self.alpha * (reward + self.gamma * best_next - self.q_table[key][action])
1~import numpy as np
import random

class QAgent:
    def __init__(self, n_actions, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.n_actions = n_actions

    def _get_state_key(self, state):
        return tuple(np.round(state, 1))  # simple discretization

    def choose_action(self, state):
        key = self._get_state_key(state)
        if random.random() < self.epsilon or key not in self.q_table:
            return random.randint(0, self.n_actions - 1)
        return np.argmax(self.q_table[key])

    def update(self, state, action, reward, next_state):
        key = self._get_state_key(state)
        next_key = self._get_state_key(next_state)
        self.q_table.setdefault(key, np.zeros(self.n_actions))
        self.q_table.setdefault(next_key, np.zeros(self.n_actions))
        best_next = np.max(self.q_table[next_key])
        self.q_table[key][action] += self.alpha * (reward + self.gamma * best_next - self.q_table[key][action])
