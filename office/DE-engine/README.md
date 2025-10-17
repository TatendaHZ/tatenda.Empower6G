# 📡 Empower6G Decision Engine — RL-based QoS Control (Local Mode)

This module implements a **local Reinforcement Learning (RL)** test harness that learns to **optimize throughput** by dynamically adjusting QoS sessions via the **CAMARA QoD API (NEF)**. It extends the existing Empower6G Decision Engine components.

---

## 🧠 Overview

The RL control loop uses **real-time metrics** collected from:
- **Amarisoft RAN** (`dl_bitrate`, `ul_bitrate`, `CQI`, etc.)
- **Kubernetes nodes** (CPU, memory, TX/RX, latency)

These metrics are exported by `combined_metrics.py` every 30 seconds and written into:
```
metrics.svc
```

The RL environment reads this file, decides which **QoS profile** to apply (e.g., `QOS_M`, `QOS_L`, `QOS_XXXL`), and interacts with the **Network Exposure Function (NEF)** by:
1. Deleting the existing QoS session (`delete_session.py`)
2. Creating a new one (`create_session.py`) with the chosen QoS profile

The current goal is to **maximize downlink + uplink throughput** using trial-and-error learning.

---

## 📁 Project Structure

```
home/DE-engine/src/
├── combined_metrics.py        # Collects and logs Amarisoft + Prometheus metrics → metrics.svc
├── metrics.svc                # JSON output file (updated every 30s)
│
├── camara/                    # NEF (CAMARA QoD) API control scripts
│   ├── create_session.py      # Creates a QoS session (payload includes qos: "QOS_M" etc.)
│   ├── delete_session.py      # Deletes current QoS session using session_info.txt
│   └── session_info.txt       # Stores current UE IP and session ID
│
└── algorithms/                # Local RL training components
    ├── env_qos_rl.py          # RL environment interface (reads metrics, applies QoS)
    ├── agent_qos_qlearning.py # Simple tabular Q-learning agent
    └── main_train.py          # Main training loop combining agent + environment
```

---

## ⚙️ How It Works

### 1️⃣ `combined_metrics.py`
- Connects to **Amarisoft gNB** (via WebSocket) and **Prometheus** (via REST).
- Collects UE metrics (`dl_bitrate`, `ul_bitrate`, `mcs`, `cqi`, etc.) and node metrics (CPU, memory, TX, RX).
- Writes a combined JSON snapshot every 30 seconds:
  ```json
  {
    "time": 1730743080.123456,
    "ran_metrics": {
      "ue_list": [
        {
          "ue_id": "1",
          "cells": [
            {"dl_bitrate": 50.5, "ul_bitrate": 20.3, "cqi": 12, "ul_mcs": 22}
          ]
        }
      ]
    },
    "node_metrics": [
      {"core node": {"cpu": "25.5", "memory": "60.2", "latency": "1.0"}}
    ]
  }
  ```

### 2️⃣ `env_qos_rl.py`
- Reads the latest `metrics.svc` file.
- Computes throughput: `throughput = dl_bitrate + ul_bitrate`.
- When the RL agent chooses an action (e.g., `QOS_XL`):
  - Deletes the current QoS session.
  - Creates a new one with the selected profile.
  - Waits for 35 seconds for the network to stabilize.
- Returns the **new state** (bitrate values) and **reward** (throughput gain).

### 3️⃣ `agent_qos_qlearning.py`
- Implements a simple **tabular Q-learning** agent.
- Learns which QoS level produces higher throughput under current conditions.
- Balances exploration (try new QoS) and exploitation (use best known QoS).

### 4️⃣ `main_train.py`
- Runs the training loop:
  1. Reads current metrics.
  2. Chooses QoS via Q-learning.
  3. Applies new session via NEF.
  4. Waits → reads new metrics → computes reward.
  5. Updates Q-table.
- Logs throughput improvements after each iteration.

---

## 🧪 Running Locally

### Step 1: Start Metrics Collection
```bash
cd home/DE-engine/src
python3 combined_metrics.py
```
Ensure that `metrics.svc` updates every ~30 seconds with new throughput data.

### Step 2: Run the RL Training Loop
In another terminal:
```bash
cd home/DE-engine/src
python3 algorithms/main_train.py
```

You’ll see logs like:
```
=== Episode 1 ===
[ACTION] Applying QoS profile: QOS_M
Reward: +10.2, New Throughput: 70.8 Mbps

=== Episode 2 ===
[ACTION] Applying QoS profile: QOS_XXL
Reward: -5.4, New Throughput: 65.4 Mbps
```

### Step 3: Monitor Behavior
- Confirm that sessions are being created/deleted in the NEF logs.
- Check that UE throughput responds to different QoS profiles.

---

## 🧩 Notes & Next Steps

- The **video server** will later send its *required bandwidth* to the Decision Engine so that the RL agent can adapt QoS based on **application intent**.
- For now, the RL loop only uses **measured throughput** as the optimization objective.
- Once stable:
  - Add latency/jitter metrics to the state.
  - Introduce reward penalties for excessive resource use.
  - Integrate with NEF **Traffic Influence** once the 6GSunrise feature is ready.

---

## 🧰 Dependencies

All scripts rely on:
- Python ≥ 3.8
- Libraries: `numpy`, `requests`, `asyncio`, `websockets`, `prometheus_client`, `psutil`

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 📜 License

© 2025 Empower6G Research — AI-Driven Network Automation  
Developed by **Tatenda Horiro Zhou**
