import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = sns.load_dataset("penguins")

print("Missing values per column before cleaning:")
print(df.isnull().sum())

plt.figure(figsize=(8, 5))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Penguin Dataset Missing Values Heatmap")
plt.show()

df = df.dropna(how="all")

for col in ["sex", "island"]:
  if col in df.columns:
    df[col] = df[col].fillna(df[col].mode()[0])

num_cols = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
for col in num_cols:
  if col in df.columns:
    df[col] = df[col].interpolate(method="linear")
    df[col] = df[col].bfill()
    df[col] = df[col].ffill()

print("\nMissing values per column after cleaning:")
print(df.isnull().sum())