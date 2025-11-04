import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("progress_log.csv")

# Sort by date to ensure chronological plotting
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Plot progress
plt.figure(figsize=(8, 5))
plt.plot(df["date"], df["completion"], marker="o", linestyle="-", color="royalblue")
plt.title("📈 Python Learning Progress Tracker")
plt.xlabel("Date")
plt.ylabel("Completion (%)")
plt.ylim(0, 110)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
