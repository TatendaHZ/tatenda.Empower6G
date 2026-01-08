import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, RepeatVector, TimeDistributed, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.regularizers import l2
import matplotlib.pyplot as plt
import sys
import os

# ===============================
# CONFIG
# ===============================
REGION = sys.argv[1] if len(sys.argv) > 1 else "core"
DATA_FILE = "seven_days_metrics_clean.csv"
TIME_STEPS = 10

# Different training settings for UE (more complex + noisier data)
if REGION == "ue":
    EPOCHS = 80
    BATCH_SIZE = 32
    LR = 0.0005
else:
    EPOCHS = 50
    BATCH_SIZE = 64
    LR = 0.001

print(f"🚀 Training LSTM Autoencoder for region: {REGION.upper()}")

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv(DATA_FILE)
cols = df.columns.drop("timestamp")

region_map = {
    "core": [c for c in cols if "core_node" in c],
    "mec": [c for c in cols if "mec_node" in c],
    "app": [c for c in cols if "kube_app_server" in c],
    "ue": [c for c in cols if "ue" in c],
}

region_cols = region_map[REGION]
X = df[region_cols]

# ===============================
# SCALE DATA
# ===============================
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
joblib.dump(scaler, f"{REGION}_scaler.pkl")

# ===============================
# CREATE SEQUENCES
# ===============================
def create_sequences(data, time_steps=TIME_STEPS):
    return np.array([data[i:i + time_steps] for i in range(len(data) - time_steps)])

X_seq = create_sequences(X_scaled, TIME_STEPS)
print(f"{REGION.upper()} sequence shape:", X_seq.shape)

# Time-based train-test split
split = int(0.9 * len(X_seq))
X_train, X_val = X_seq[:split], X_seq[split:]

# ===============================
# BUILD MODEL
# ===============================
timesteps = X_train.shape[1]
n_features = X_train.shape[2]

inp = Input(shape=(timesteps, n_features))

if REGION == "ue":
    # Deeper autoencoder for UE (noisier + higher variance)
    enc = LSTM(256, activation='relu', return_sequences=True,
               dropout=0.2, recurrent_dropout=0.2)(inp)
    enc = LSTM(128, activation='relu', return_sequences=False,
               dropout=0.2, recurrent_dropout=0.2)(enc)

    bottleneck = RepeatVector(timesteps)(enc)

    dec = LSTM(128, activation='relu', return_sequences=True,
               dropout=0.2, recurrent_dropout=0.2)(bottleneck)
    dec = LSTM(256, activation='relu', return_sequences=True)(dec)

else:
    # Simple autoencoder for CORE/MEC/APP
    enc = LSTM(128, activation='relu', return_sequences=False)(inp)
    bottleneck = RepeatVector(timesteps)(enc)
    dec = LSTM(128, activation='relu', return_sequences=True)(bottleneck)

out = TimeDistributed(Dense(n_features, kernel_regularizer=l2(1e-6)))(dec)

model = Model(inp, out)
model.compile(optimizer=Adam(learning_rate=LR), loss="mse")
model.summary()

# ===============================
# TRAIN MODEL
# ===============================
callbacks = [
    EarlyStopping(
        monitor='val_loss',
        patience=8,
        restore_best_weights=True
    )
]

history = model.fit(
    X_train, X_train,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    validation_data=(X_val, X_val),
    shuffle=False,  # DO NOT shuffle for time-series!
    callbacks=callbacks,
    verbose=1
)

# ===============================
# SAVE MODEL
# ===============================
os.makedirs("models", exist_ok=True)
model.save(f"models/{REGION}_autoencoder.h5")

# ===============================
# PLOT TRAINING LOSS
# ===============================
plt.figure(figsize=(8, 4))
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')

plt.title(f"{REGION.upper()} Autoencoder Training Loss")
plt.xlabel("Epochs")
plt.ylabel("Reconstruction Loss (MSE)")
plt.legend()

# Explanation text under the plot
plt.figtext(
    0.5, -0.1,
    "X-axis: Number of training epochs\n"
    "Y-axis: Mean squared reconstruction error (MSE)\n"
    "Lower values = better reconstruction performance",
    wrap=True, horizontalalignment='center', fontsize=9
)

plt.tight_layout()
plt.savefig(f"{REGION}_training_loss.png", bbox_inches="tight")
plt.show()
