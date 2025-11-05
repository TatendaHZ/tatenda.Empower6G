import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("seven_days_metrics.csv", parse_dates=["timestamp"])

# Basic info
print(df.info())
print(df.describe())

# Check missing values
missing = df.isnull().sum()
print("Missing values:\n", missing[missing > 0])

# Plot correlation heatmap
plt.figure(figsize=(15,10))
sns.heatmap(df.corr(), cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

# Plot some key trends
cols_to_plot = ["core_node_cpu", "mec_node_cpu", "kube_app_server_cpu", "ue1_dl_bitrate"]
df.set_index("timestamp")[cols_to_plot].plot(subplots=True, figsize=(12,8))
plt.show()
