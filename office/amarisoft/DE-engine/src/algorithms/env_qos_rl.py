# env_qos_rl.py
import json, time, subprocess
import numpy as np
from pathlib import Path

class QoSEnvironment:
    def __init__(self, metrics_path, camara_dir):
        self.metrics_path = Path("/home/generic/tatenda.Empower6G/office/DE-engine/src/metrics.svc")
        self.camara_dir = Path("/home/generic/tatenda.Empower6G/office/DE-engine/src/camara")
        self.qos_profiles = ["QOS_S", "QOS_M", "QOS_L", "QOS_XL", "QOS_XXL", "QOS_XXXL"]
        self.prev_throughput = 0.0
        self.state = None

    def _read_metrics(self):
        """Reads DL/UL throughput from metrics.svc"""
        try:
            data = json.loads(self.metrics_path.read_text())
            ue = data["ran_metrics"]["ue_list"][0]["cells"][0]
            dl, ul = ue["dl_bitrate"], ue["ul_bitrate"]
            return dl, ul
        except Exception as e:
            print(f"[WARN] Failed to read metrics: {e}")
            return 0.0, 0.0

    def _apply_qos(self, qos_profile):
        """Delete current session → create new one with selected QoS"""
        print(f"[ACTION] Applying QoS profile: {qos_profile}")
        try:
            subprocess.run(["python3", f"{self.camara_dir}/delete_session.py"], check=False)
            # Patch payload dynamically
            create_path = self.camara_dir / "create_session.py"
            content = create_path.read_text().replace('"qos": "QOS_M"', f'"qos": "{qos_profile}"')
            tmp_path = self.camara_dir / "tmp_create.py"
            tmp_path.write_text(content)
            subprocess.run(["python3", str(tmp_path)], check=False)
            tmp_path.unlink(missing_ok=True)
        except Exception as e:
            print(f"[ERROR] Failed to apply QoS: {e}")

    def reset(self):
        dl, ul = self._read_metrics()
        self.prev_throughput = dl + ul
        self.state = np.array([dl, ul])
        return self.state

    def step(self, action):
        qos = self.qos_profiles[action]
        self._apply_qos(qos)
        time.sleep(35)  # Wait for new metrics (metrics.svc updates every 30s)
        dl, ul = self._read_metrics()
        new_thr = dl + ul
        reward = new_thr - self.prev_throughput
        self.prev_throughput = new_thr
        self.state = np.array([dl, ul])
        return self.state, reward
