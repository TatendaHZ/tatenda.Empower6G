from algorithms.env_qos_rl import QoSEnvironment
from algorithms.agent_qos_qlearning import QAgent

env = QoSEnvironment(metrics_path="metrics.svc", camara_dir="camara")
agent = QAgent(n_actions=6)

state = env.reset()

for episode in range(10):
    print(f"\n=== Episode {episode + 1} ===")
    action = agent.choose_action(state)
    next_state, reward = env.step(action)
    agent.update(state, action, reward, next_state)
    print(f"Reward: {reward:.3f}, New Throughput: {sum(next_state):.3f} Mbps")
    state = next_state
