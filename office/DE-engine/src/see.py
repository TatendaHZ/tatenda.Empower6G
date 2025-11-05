import pandas as pd

df = pd.read_csv(r"/home/generic/tatenda.Empower6G/office/DE-engine/src/four_days_metrics.csv")

print("✅ Shape (rows, columns):", df.shape)
print("\n📌 Number of numeric features:", df.select_dtypes(include=['number']).shape[1])
print("\n❌ Missing values per column:")
print(df.isna().sum())

# Basic stats
print("\n📊 Descriptive Stats:")
print(df.describe())

# Check for constant columns
const_cols = [c for c in df.columns if df[c].nunique() == 1]
print("\n⚠️ Constant columns:", const_cols)
