# network_env.py
import json
import os
import time
import subprocess
import requests

# Paths
CAMARA_PATH = "/home/generic/tatenda.Empower6G/office/DE-engine/src/camara"
GAIN_PATH = "/home/generic/tatenda.Empower6G/office/DE-engine/src/gain"
METRICS_FILE = "/home/generic/tatenda.Empower6G/office/DE-engine/src/metrics.svc"
SESSION_FILE = os.path.join(CAMARA_PATH, "session_info.txt")

# QoS options
QOS_MAP = {
    "QOS_E": {"dl": 120000, "ul": 120000},  # CONTROL
    "QOS_S": {"dl": 2000, "ul": 200},       # AUDIO
    "QOS_M": {"dl": 400, "ul": 400},        # VIDEO
    "QOS_L": {"dl": 8000, "ul": 1000},      # VIDEO
    "QOS_A": {"dl": 300, "ul": 100},        # 144p
    "QOS_B": {"dl": 500, "ul": 150},        # 240p
    "QOS_C": {"dl": 800, "ul": 200},        # 360p low
    "QOS_D": {"dl": 1000, "ul": 250},       # 360p high
    "QOS_F": {"dl": 1500, "ul": 300},       # 480p
    "QOS_G": {"dl": 2000, "ul": 400},       # 480p high
    "QOS_H": {"dl": 3000, "ul": 500},       # 720p low
    "QOS_I": {"dl": 4000, "ul": 600},       # 720p standard
    "QOS_J": {"dl": 5000, "ul": 700},       # 720p high
    "QOS_K": {"dl": 6000, "ul": 800},       # 1080p low
    "QOS_N": {"dl": 8000, "ul": 1000},      # 1080p standard
    "QOS_O": {"dl": 10000, "ul": 1200},     # 1080p high
    "QOS_P": {"dl": 12000, "ul": 1500},     # 1440p low
    "QOS_Q": {"dl": 15000, "ul": 1800},     # 1440p high
    "QOS_R": {"dl": 20000, "ul": 2000},     # 4K low
    "QOS_T": {"dl": 1000000, "ul": 2500},   # 4K high
}

# Amarisoft gain levels
GAIN_LEVELS = ["low", "medium", "high", "max"]

# API config
API_ROOT = "http://192.168.3.89:30991/"
BASE_PATH = "qod/v0"
SESSIONS_ENDPOINT = f"{API_ROOT}{BASE_PATH}/sessions"

# Thresholds for reward calculation
CPU_THRESHOLD = 85.0
MEMORY_THRESHOLD = 85.0
PATH_LOSS_THRESHOLD = 78.0
THROUGHPUT_UTIL_THRESHOLD = 0.9  # 90%

# Cooldown in seconds between actions
ACTION_COOLDOWN = 5

class NetworkEnv:
    def __init__(self):
        self.last_action_time = 0

    # --------------------
    # Helpers
    # --------------------
    def load_metrics(self):
        try:
            with open(METRICS_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"[ERROR] Failed to load metrics: {e}")
            return {}

    def load_sessions(self):
        if not os.path.exists(SESSION_FILE):
            return []
        with open(SESSION_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def save_sessions(self, sessions):
        with open(SESSION_FILE, "w") as f:
            json.dump(sessions, f, indent=2)

    # --------------------
    # Environment Actions
    # --------------------
    def delete_session_for_ue(self, ue_ip):
        sessions = self.load_sessions()
        session_entry = next((s for s in sessions if s["UE ID"] == ue_ip), None)
        if not session_entry:
            print(f"[INFO] No session found for UE {ue_ip}")
            return False

        session_id = session_entry["Session ID"]
        DELETE_ENDPOINT = f"{API_ROOT}{BASE_PATH}/sessions/{session_id}"
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.delete(DELETE_ENDPOINT, headers=headers)
            if response.status_code == 204:
                print(f"[INFO] Deleted session {session_id} for UE {ue_ip}")
                return True
            else:
                print(f"[ERROR] Failed to delete session: {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Exception while deleting session: {e}")
            return False

    def create_session_for_ue(self, ue_ip, qos="QOS_M", as_ip="192.168.3.108"):
        payload = {
            "duration": 86400,
            "ueId": {"ipv4addr": ue_ip},
            "asId": {"ipv4addr": as_ip},
            "uePorts": {"ranges": [{"from": 0, "to": 65535}]},
            "asPorts": {"ranges": [{"from": 0, "to": 65535}]},
            "qos": qos,
            "notificationUri": f"{API_ROOT}notifications",
            "notificationAuthToken": "c8974e592c2fa383d4a3960714"
        }
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(SESSIONS_ENDPOINT, json=payload, headers=headers)
            if response.status_code == 201:
                print(f"[INFO] Created session for UE {ue_ip} with QoS {qos}")
                return True
            else:
                print(f"[ERROR] Failed to create session: {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Exception while creating session: {e}")
            return False

    def change_gain(self, level):
        if level not in GAIN_LEVELS:
            print(f"[ERROR] Invalid gain level: {level}")
            return False
        try:
            subprocess.run(["python3", os.path.join(GAIN_PATH, "change_gain.py"), level], check=True)
            print(f"[INFO] Gain changed to {level}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Failed to change gain: {e}")
            return False

    # --------------------
    # Environment Interface
    # --------------------
    def get_state_for_ue(self, ue_ip):
        metrics = self.load_metrics()
        ue_list = metrics.get("ran_metrics", {}).get("ue_list", [])
        ue_data = next((ue for ue in ue_list if ue["ue_id"] == ue_ip), None)
        if not ue_data:
            return None

        # Use first cell for simplicity
        cell = ue_data["cells"][0]
        state = {
            "dl_bitrate": cell["dl_bitrate"],  # Mbps
            "ul_bitrate": cell["ul_bitrate"],
            "ul_path_loss": cell["ul_path_loss"],
            "cpu": metrics.get("node_metrics", [{}])[0].get("cpu", 0),
            "memory": metrics.get("node_metrics", [{}])[0].get("memory", 0)
        }
        return state

    def calculate_reward(self, state, qos):
        """Reward based on throughput vs QoS limits and path loss"""
        if not state or qos not in QOS_MAP:
            return -1  # negative reward if state invalid

        qos_dl = QOS_MAP[qos]["dl"]
        qos_ul = QOS_MAP[qos]["ul"]

        reward = 0
        # Penalty for high CPU/memory
        reward -= 0.01 * max(0, state["cpu"] - CPU_THRESHOLD)
        reward -= 0.01 * max(0, state["memory"] - MEMORY_THRESHOLD)

        # Reward for staying below throughput limits
        reward += min(state["dl_bitrate"]*1000/qos_dl, 1.0)
        reward += min(state["ul_bitrate"]*1000/qos_ul, 1.0)

        # Penalty for high path loss
        if state["ul_path_loss"] > PATH_LOSS_THRESHOLD:
            reward -= 0.5

        return reward

    def step(self, action, ue_ip):
        """Perform action and return (new_state, reward)"""
        # Cooldown check
        if time.time() - self.last_action_time < ACTION_COOLDOWN:
            return self.get_state_for_ue(ue_ip), 0

        self.last_action_time = time.time()

        # Actions: "qos_QOS_H", "gain_high", etc.
        if action.startswith("qos_"):
            qos = action.split("_")[1]
            self.delete_session_for_ue(ue_ip)
            self.create_session_for_ue(ue_ip, qos=qos)
        elif action.startswith("gain_"):
            gain_level = action.split("_")[1]
            self.change_gain(gain_level)
        else:
            print(f"[WARN] Unknown action {action}")

        state = self.get_state_for_ue
