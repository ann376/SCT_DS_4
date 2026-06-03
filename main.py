import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("US_Accidents_March23.csv", nrows=50000)
print("===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# -------------------------
# Weather Conditions
# -------------------------
plt.figure(figsize=(12,6))

df['Weather_Condition'].value_counts().head(10).plot(
    kind='bar'
)

plt.title("Top 10 Weather Conditions During Accidents")
plt.xlabel("Weather Condition")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("weather_conditions.png")
plt.show()

# -------------------------
# Accidents by Severity
# -------------------------
plt.figure(figsize=(8,5))

sns.countplot(data=df, x='Severity')

plt.title("Accident Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("severity_distribution.png")
plt.show()

# -------------------------
# Traffic Signal Analysis
# -------------------------
plt.figure(figsize=(6,5))

sns.countplot(data=df, x='Traffic_Signal')

plt.title("Traffic Signal Presence")
plt.xlabel("Traffic Signal")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("traffic_signal.png")
plt.show()

# -------------------------
# Day vs Night Accidents
# -------------------------
plt.figure(figsize=(6,5))

sns.countplot(data=df, x='Sunrise_Sunset')

plt.title("Accidents by Time of Day")
plt.xlabel("Day/Night")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("day_night_accidents.png")
plt.show()

# -------------------------
# Accident Hotspots
# -------------------------
plt.figure(figsize=(10,6))

plt.scatter(
    df['Start_Lng'],
    df['Start_Lat'],
    alpha=0.1,
    s=1
)

plt.title("Accident Hotspots")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.tight_layout()
plt.savefig("accident_hotspots.png")
plt.show()

print("\nAnalysis Completed Successfully!")