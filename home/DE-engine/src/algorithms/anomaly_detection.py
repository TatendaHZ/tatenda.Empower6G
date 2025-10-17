from .base import AlgorithmInterface
import json
from pathlib import Path


class AnomalyDetection(AlgorithmInterface):
    def launch(self):
        """
        Simple threshold-based anomaly detection.
        Flags any node with CPU > 80% or Memory > 80% as anomalous.
        """
        metrics = self.get_input_parameters()
        node_metrics = metrics.get("node_metrics", [])
        anomalies = []

        for node in node_metrics:
            # Each node is a dict with one key (node name)
            for node_name, values in node.items():
                cpu = float(values.get("cpu", 0))
                memory = float(values.get("memory", 0))

                node_anomalies = {}
                if cpu > 80:
                    node_anomalies["cpu"] = cpu
                if memory > 80:
                    node_anomalies["memory"] = memory

                if node_anomalies:
                    anomalies.append({
                        "node": node_name,
                        "anomalies": node_anomalies
                    })

        return {"anomalies": anomalies}


# Path for metrics file
METRICS_FILE = Path("/app/src/metrics.svc")


def read_metrics():
    """Read metrics.svc and return JSON data"""
    if not METRICS_FILE.exists():
        return None
    try:
        with open(METRICS_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading metrics: {e}")
        return None
