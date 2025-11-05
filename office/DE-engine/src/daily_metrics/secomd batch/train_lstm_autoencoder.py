import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, RepeatVector, TimeDistributed, Dense
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

# ===== Load data and scaler =====
df = pd.read_csv("seven_days_metrics.csv")
scaler = joblib.load("scaler.pkl")

X = df.drop(columns=["timestamp"])
X_scaled = scaler.transform(X)

# ===== Create temporal sequences =====
TIME_STEPS = 10  # you can adjust (5–30 typical)
def create_sequences(data, time_steps=TIME_STEPS):
    seqs = []
    for i in range(len(data) - time_steps):
        seqs.append(data[i:i+time_steps])
    return np.array(seqs)

X_seq = create_sequences(X_scaled, TIME_STEPS)
print("Sequence shape:", X_seq.shape)  # (samples, timesteps, features)

# ===== LSTM Autoencoder architecture =====
timesteps = X_seq.shape[1]
n_features = X_seq.shape[2]

input_layer = Input(shape=(timesteps, n_features))
encoded = LSTM(128, activation='relu', return_sequences=False)(input_layer)
bottleneck = RepeatVector(timesteps)(encoded)
decoded = LSTM(128, activation='relu', return_sequences=True)(bottleneck)
decoded = TimeDistributed(Dense(n_features))(decoded)

model = Model(inputs=input_layer, outputs=decoded)
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')
model.summary()

# ===== Train =====
history = model.fit(
    X_seq, X_seq,
    epochs=50,
    batch_size=64,
    validation_split=0.1,
    shuffle=True
)

# ===== Save model =====
model.save("lstm_autoencoder.h5")

# ===== Plot training loss =====
plt.figure(figsize=(8,4))
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='val')
plt.title("LSTM Autoencoder Training Loss")
plt.legend()
plt.show()
