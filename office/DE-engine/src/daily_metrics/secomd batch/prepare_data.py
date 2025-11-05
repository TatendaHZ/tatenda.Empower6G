import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the data
df = pd.read_csv("seven_days_metrics.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df = df.drop_duplicates(subset=["timestamp"]).sort_values("timestamp")

# Group columns by subsystem
core_features = [c for c in df.columns if "core_node" in c]
mec_features = [c for c in df.columns if "mec_node" in c]
server_features = [c for c in df.columns if "kube_app_server" in c]
ue_features = [c for c in df.columns if "ue" in c]

subsystem_groups = {
    "core": core_features,
    "mec": mec_features,
    "server": server_features,
    "ran": ue_features
}

print("Subsystem grouping summary:")
for k, v in subsystem_groups.items():
    print(f"  {k}: {len(v)} features")

# Normalize numeric data
scaler = StandardScaler()
X = df.drop(columns=["timestamp"])
X_scaled = scaler.fit_transform(X)

# Save for later steps
import joblib
joblib.dump(scaler, "scaler.pkl")

print("Data ready. Shape:", X_scaled.shape)
