import json
import time
import os

METRICS_FILE = "/home/generic/tatenda.Empower6G/office/DE-engine/src/metrics.svc"
SESSION_FILE = "/home/generic/tatenda.Empower6G/office/DE-engine/src/camara/session_info.txt"
TRIGGER_FILE = "/home/generic/tatenda.Empower6G/office/DE-engine/src/agent_trigger.txt"

# QoS mapping in Kbps
QOS_MAP = {
    "QOS_E": {"dl": 120000, "ul": 120000},   # CONTROL
    "QOS_S": {"dl": 2000, "ul": 200},        # AUDIO
    "QOS_M": {"dl": 400, "ul": 400},         # VIDEO
    "QOS_L": {"dl": 8000, "ul": 1000},       # VIDEO
    "QOS_A": {"dl": 300, "ul": 100},         # 144p
    "QOS_B": {"dl": 500, "ul": 150},         # 240p
    "QOS_C": {"dl": 800, "ul": 200},         # 360p low
    "QOS_D": {"dl": 1000, "ul": 250},        # 360p high
    "QOS_F": {"dl": 1500, "ul": 300},        # 480p
    "QOS_G": {"dl": 2000, "ul": 400},        # 480p high
    "QOS_H": {"dl": 3000, "ul": 500},        # 720p low
    "QOS_I": {"dl": 4000, "ul": 600},        # 720p standard
    "QOS_J": {"dl": 5000, "ul": 700},        # 720p high
    "QOS_K": {"dl": 6000, "ul": 800},        # 1080p low
    "QOS_N": {"dl": 8000, "ul": 1000},       # 1080p standard
    "QOS_O": {"dl": 10000, "ul": 1200},      # 1080p high
    "QOS_P": {"dl": 12000, "ul": 1500},      # 1440p low
    "QOS_Q": {"dl": 15000, "ul": 1800},      # 1440p high
    "QOS_R": {"dl": 20000, "ul": 2000},      # 4K low
    "QOS_T": {"dl": 1000000, "ul": 2500},    # 4K high
}

CPU_THRESHOLD = 85.0
MEMORY_THRESHOLD = 85.0
PATH_LOSS_THRESHOLD = 78.0
THROUGHPUT_UTIL_THRESHOLD = 0.9  # 90%


def load_json_file(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Failed to load {path}: {e}")
        return None


def write_trigger(status, details=None):
    """Write 'run' or 'stop' into the trigger file with optional details."""
    try:
        with open(TRIGGER_FILE, 'w') as f:
            if status == "run" and details:
                f.write(f"{status}:\n" + "\n".join(details))
            else:
                f.write(status)
        print(f"[INFO] Wrote '{status}' to {TRIGGER_FILE}")
        if details:
            for d in details:
                print("   ", d)
    except Exception as e:
        print(f"[ERROR] Failed to write trigger file: {e}")


def check_metrics(metrics, sessions):
    anomalies = []

    # Build mapping: UE ID in metrics.svc -> session info (IP, QoS)
    ue_session_map = {str(ix + 1): s for ix, s in enumerate(sessions)}

    # Node metrics check
    for node in metrics.get("node_metrics", []):
        for node_name, node_values in node.items():
            cpu = float(node_values["cpu"])
            mem = float(node_values["memory"])
            if cpu > CPU_THRESHOLD:
                anomalies.append(f"Node {node_name}: High CPU ({cpu}%)")
            if mem > MEMORY_THRESHOLD:
                anomalies.append(f"Node {node_name}: High Memory ({mem}%)")

    # RAN metrics check
    for ue in metrics.get("ran_metrics", {}).get("ue_list", []):
        ue_id = ue["ue_id"]  # from metrics.svc
        session = ue_session_map.get(ue_id, None)
        ue_ip = session["UE ID"] if session else "unknown"
        qos_name = session["QoS"] if session else None

        for cell in ue.get("cells", []):
            path_loss = cell["ul_path_loss"]
            dl_bitrate = cell["dl_bitrate"] * 1000  # Mbps → Kbps
            ul_bitrate = cell["ul_bitrate"] * 1000

            # Check throughput per QoS
            if qos_name and qos_name in QOS_MAP:
                qos_dl = QOS_MAP[qos_name]["dl"]
                qos_ul = QOS_MAP[qos_name]["ul"]

                if dl_bitrate >= THROUGHPUT_UTIL_THRESHOLD * qos_dl:
                    anomalies.append(
                        f"UE {ue_id} ({ue_ip}): DL near saturation {dl_bitrate:.1f}/{qos_dl} kbps ({qos_name})"
                    )
                if ul_bitrate >= THROUGHPUT_UTIL_THRESHOLD * qos_ul:
                    anomalies.append(
                        f"UE {ue_id} ({ue_ip}): UL near saturation {ul_bitrate:.1f}/{qos_ul} kbps ({qos_name})"
                    )

            # Path loss check
            if path_loss > PATH_LOSS_THRESHOLD:
                anomalies.append(
                    f"UE {ue_id} ({ue_ip}): High path loss {path_loss} dB"
                )

    return anomalies


if __name__ == "__main__":
    print("[INFO] Starting anomaly detection service...")
    anomaly_active = False  # Track state to avoid spamming file writes

    while True:
        metrics = load_json_file(METRICS_FILE)
        sessions = load_json_file(SESSION_FILE)

        if metrics and sessions:
            anomalies = check_metrics(metrics, sessions)

            if anomalies and not anomaly_active:
                print("[DETECT] Anomaly detected!")
                write_trigger("run", anomalies)
                anomaly_active = True

            elif not anomalies and anomaly_active:
                print("[RECOVER] System back to normal — stopping agent.")
                write_trigger("stop")
                anomaly_active = False

        time.sleep(5)
