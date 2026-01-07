from flask import Flask, request, render_template_string
import json
import time
from threading import Lock

app = Flask(__name__)

# Store metrics in memory
metrics_data = []
data_lock = Lock()
MAX_RECORDS = 50  # Keep only last 50 entries

# HTML template for live view
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Latency & Jitter Metrics</title>
    <meta http-equiv="refresh" content="1">
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 60%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: center; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h2>Live Latency & Jitter Metrics</h2>
    <table>
        <tr>
            <th>Timestamp</th>
            <th>Interface</th>
            <th>Latency (ms)</th>
            <th>Jitter (ms)</th>
        </tr>
        {% for record in metrics %}
        <tr>
            <td>{{ record['timestamp'] }}</td>
            <td>{{ record['interface'] }}</td>
            <td>{{ "%.2f"|format(record['latency_ms']) }}</td>
            <td>{{ "%.2f"|format(record['jitter_ms']) }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route("/post_metrics", methods=["POST"])
def post_metrics():
    try:
        data = request.get_json()
        data['timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S")
        print("Received:", data)

        # Store in memory
        with data_lock:
            metrics_data.append(data)
            if len(metrics_data) > MAX_RECORDS:
                metrics_data.pop(0)  # Keep last 50 records

        # Optionally save to file
        with open("metrics_log.json", "a") as f:
            f.write(json.dumps(data) + "\n")

        return "OK", 200
    except Exception as e:
        print("Error:", e)
        return "Error", 500

@app.route("/", methods=["GET"])
def index():
    with data_lock:
        return render_template_string(HTML_TEMPLATE, metrics=list(reversed(metrics_data)))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
