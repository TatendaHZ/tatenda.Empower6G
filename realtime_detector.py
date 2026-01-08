import numpy as np
import pandas as pd
import joblib
import time
import os
from tensorflow.keras.models import load_model
from datetime import datetime

TIME_STEPS = 10
DATA_FILE = "seven_days_metrics.csv"  # Make sure this file exists in the same folder!

# ========= Region Column Map =========
def region_columns(df):
    cols = df.columns.drop("timestamp", errors="ignore")
    mapping = {
        "core": [c for c in cols if "core_node" in c],
        "mec":  [c for c in cols if "mec_node" in c],
        "app":  [c for c in cols if "kube_app_server" in c],
        "ue":   [c for c in cols if "ue" in c],
    }
    # Debug print
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Column detection:")
    for r, clist in mapping.items():
        print(f"   {r.upper():4}: {len(clist)} columns → {clist[:3]}{'...' if len(clist)>3 else ''}")
    return mapping

# ========= Sliding window buffers =========
sequence_buffers = {r: [] for r in ["core", "mec", "app", "ue"]}
samples_seen = {r: 0 for r in ["core", "mec", "app", "ue"]}

def update_sequence(region, new_row, scaler, cols):
    if len(cols) == 0:
        return None

    vec = new_row[cols].values.astype(float).reshape(1, -1)
    vec_scaled = scaler.transform(vec)[0]

    sequence_buffers[region].append(vec_scaled)
    samples_seen[region] += 1

    if len(sequence_buffers[region]) > TIME_STEPS:
        sequence_buffers[region].pop(0)

    if len(sequence_buffers[region]) < TIME_STEPS:
        return None

    return np.array([sequence_buffers[region]])  # shape: (1, 10, features)

# ========= Load models & scalers safely =========
print("\nLoading models and scalers...")
models = {}
scalers = {}

for r in ["core", "mec", "app", "ue"]:
    model_path = f"models/{r}_autoencoder.h5"
    scaler_path = f"scaler/{r}_scaler.pkl"

    if not os.path.exists(model_path):
        print(f"Model NOT FOUND: {model_path}")
    else:
        # FIX: use compile=False for TensorFlow compatibility
        models[r] = load_model(model_path, compile=False)
        print(f"Loaded model: {model_path}")

    if not os.path.exists(scaler_path):
        print(f"Scaler NOT FOUND: {scaler_path}")
    else:
        scalers[r] = joblib.load(scaler_path)
        print(f"Loaded scaler: {scaler_path}")

print("\nREAL-TIME ANOMALY DETECTOR STARTED")
if not os.path.exists(DATA_FILE):
    print(f"DATA FILE NOT FOUND: {DATA_FILE}")
    print("   Place your CSV in this folder or update DATA_FILE path.")
    exit(1)
else:
    print(f"Monitoring file: {os.path.abspath(DATA_FILE)}")

# ========= MAIN LOOP =========
last_row_count = 0

while True:
    try:
        if not os.path.exists(DATA_FILE):
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Waiting for {DATA_FILE} to appear...")
            time.sleep(10)
            continue

        df = pd.read_csv(DATA_FILE)
        current_rows = len(df)

        if current_rows == 0:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] CSV is empty. Waiting for data...")
            time.sleep(10)
            continue

        if current_rows == last_row_count:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] No new data yet ({current_rows} rows). Waiting...")
            time.sleep(10)
            continue

        print(f"[{datetime.now().strftime('%H:%M:%S')}] New telemetry row #{current_rows}")
        last_row_count = current_rows

        last = df.iloc[-1]
        region_cols = region_columns(df)

        all_waiting = True
        for region in ["core", "mec", "app", "ue"]:
            cols = region_cols[region]
            if len(cols) == 0:
                print(f"   {region.upper():4}: No columns found (skipped)")
                continue

            seq = update_sequence(region, last, scalers[region], cols)

            if seq is None:
                print(f"   {region.upper():4}: Collecting... ({samples_seen[region]}/{TIME_STEPS})")
            else:
                all_waiting = False
                pred = models[region].predict(seq, verbose=0)
                err = np.mean(np.abs(pred - seq))
                threshold = 0.09

                status = "ANOMALY" if err > threshold else "OK"
                emoji = "ALERT" if err > threshold else "CHECKMARK"
                print(f"   {region.upper():4}: {emoji} {status} | Error={err:.5f} (thresh={threshold})")

        if all_waiting:
            print("   Still warming up all regions...\n")
        else:
            print("   Monitoring active!\n")

        time.sleep(10)

    except KeyboardInterrupt:
        print("\nStopping real-time detector. Bye!")
        break
    except Exception as e:
        print(f"Unexpected error: {e}")
        print("   Will retry in 5 seconds...")
        time.sleep(5)
