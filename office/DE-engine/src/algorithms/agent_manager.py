#!/usr/bin/env python3
# agent_manager.py
import time
import os
import logging
from rl_agent import TabularAgent
from network_env import NetworkEnv

TRIGGER_FILE = "/home/generic/tatenda.Empower6G/office/DE-engine/src/agent_trigger.txt"
SESSION_FILE = "/home/generic/tatenda.Empower6G/office/DE-engine/src/camara/session_info.txt"
METRICS_FILE = "/home/generic/tatenda.Empower6G/office/DE-engine/src/metrics.svc"

POLL_INTERVAL = 3         # seconds to check trigger file
COOLDOWN_AFTER_ACTION = 10  # seconds to wait after each action (safety)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

def read_trigger():
    """Return status (str) and list of detail lines."""
    if not os.path.exists(TRIGGER_FILE):
        return None, []
    try:
        with open(TRIGGER_FILE, "r") as f:
            lines = [l.rstrip() for l in f.readlines() if l.strip()]
        if not lines:
            return None, []
        status = lines[0].strip().lower()
        details = lines[1:]
        return status, details
    except Exception as e:
        logging.error("Failed to read trigger file: %s", e)
        return None, []

def extract_ue_ips_from_details(details):
    """Given lines like 'UE 1 (10.45.0.2): DL near saturation ...', extract UE IPs."""
    ue_ips = set()
    for d in details:
        # naive parse: look for '(' and ')'
        if '(' in d and ')' in d:
            inside = d.split('(', 1)[1].split(')', 1)[0]
            # if inside contains an IP-looking token
            if '.' in inside:
                ue_ips.add(inside)
    return list(ue_ips)

def main():
    logging.info("Agent manager starting. Watching %s", TRIGGER_FILE)
    env = NetworkEnv(metrics_file=METRICS_FILE, session_file=SESSION_FILE)
    agent = TabularAgent(actions_list=env.available_actions())  # uses env to know actions

    anomaly_active = False
    while True:
        status, details = read_trigger()
        if status == "run" and not anomaly_active:
            logging.info("Trigger RUN detected with %d detail lines", len(details))
            ue_ips = extract_ue_ips_from_details(details)
            if not ue_ips:
                logging.info("No UE IPs found in trigger details — acting globally.")
                ue_ips = env.list_current_ues()

            # For each UE, let agent choose one action and apply it
            for ue_ip in ue_ips:
                state = env.get_state_for_ue(ue_ip)
                action_index = agent.select_action(state)
                action = agent.action_by_index(action_index)
                logging.info("Selected action %s for UE %s", action, ue_ip)

                obs_before = env.read_metrics_snapshot()
                success = env.step(action, ue_ip)
                if not success:
                    logging.warning("Action execution failed for %s", action)
                # wait for system to settle (reward observation delay)
                logging.info("Waiting %s s before computing reward", COOLDOWN_AFTER_ACTION)
                time.sleep(COOLDOWN_AFTER_ACTION)

                obs_after = env.read_metrics_snapshot()
                reward = env.compute_reward_for_transition(ue_ip, obs_before, obs_after)
                logging.info("Reward for action %s on %s = %.3f", action, ue_ip, reward)

                # update agent
                next_state = env.get_state_for_ue(ue_ip)
                agent.learn(state, action_index, reward, next_state)

            anomaly_active = True

        elif status == "stop" and anomaly_active:
            logging.info("Trigger STOP detected — system recovered.")
            anomaly_active = False

        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main()
