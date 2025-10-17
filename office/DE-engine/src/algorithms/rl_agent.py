#!/usr/bin/env python3
# rl_agent.py
import random
import math
import json
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

class TabularAgent:
    def __init__(self, actions_list, alpha=0.2, gamma=0.9, epsilon=0.2):
        """
        actions_list: list of action tuples from env.available_actions()
        """
        self.actions = actions_list
        self.qtable = {}  # mapping state_key -> [qvals]
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def state_to_key(self, state):
        """
        Convert state dict to discrete key. State expected keys:
          dl_kbps, ul_kbps, path_loss, qos, cpu_avg, mem_avg
        We'll discretize:
          dl_util_bucket = int(min(10, dl_kbps/100))  # coarse
          pathloss_bucket = int(min(20, path_loss // 5))
        and qos name kept as is.
        """
        dl = state.get("dl_kbps", 0)
        cpu = state.get("cpu_avg", 0)
        pl = state.get("path_loss", 0)
        qos = state.get("qos") or "QOS_M"
        dl_bucket = int(min(20, dl // 200))   # 200 kbps per bucket (coarse)
        pl_bucket = int(min(40, pl // 2))     # 2 dB per bucket
        cpu_bucket = int(min(100, cpu // 5))  # 5% per bucket
        key = f"{qos}|dl{dl_bucket}|pl{pl_bucket}|cpu{cpu_bucket}"
        return key

    def _ensure_state(self, key):
        if key not in self.qtable:
            self.qtable[key] = [0.0 for _ in range(len(self.actions))]

    def select_action(self, state):
        key = self.state_to_key(state)
        self._ensure_state(key)
        # epsilon-greedy
        if random.random() < self.epsilon:
            choice = random.randrange(len(self.actions))
            logging.debug("Random action %d for key %s", choice, key)
            return choice
        qvals = self.qtable[key]
        best = max(range(len(qvals)), key=lambda i: qvals[i])
        logging.debug("Greedy action %d for key %s", best, key)
        return best

    def action_by_index(self, idx):
        return self.actions[idx]

    def learn(self, state, action_idx, reward, next_state):
        s_key = self.state_to_key(state)
        ns_key = self.state_to_key(next_state)
        self._ensure_state(s_key)
        self._ensure_state(ns_key)
        q_sa = self.qtable[s_key][action_idx]
        max_q_next = max(self.qtable[ns_key])
        # Q-learning update
        new_q = q_sa + self.alpha * (reward + self.gamma * max_q_next - q_sa)
        self.qtable[s_key][action_idx] = new_q
        logging.info("Q[%s][%d] <- %.3f (reward %.3f)", s_key, action_idx, new_q, reward)

    # persistence helpers
    def save(self, path):
        with open(path, "w") as f:
            json.dump(self.qtable, f)

    def load(self, path):
        if os.path.exists(path):
            with open(path, "r") as f:
                self.qtable = json.load(f)
