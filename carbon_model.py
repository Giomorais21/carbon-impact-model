import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Calculate avoided emissions
df["avoided_emissions"] = df["waste_tons"] * df["avoided_emission_factor"]

# Calculate transport emissions
df["transport_emissions"] = (
    df["waste_tons"] * df["distance_km"] * df["emission_factor_transport"]
)

# Net carbon impact
df["net_impact"] = df["avoided_emissions"] - df["transport_emissions"]

# Save detailed results
df.to_csv("results.csv", index=False)


# Aggregated analysis
summary = df.groupby("transport_mode")["net_impact"].sum().reset_index()
summary = summary.sort_values("net_impact")

summary.to_csv("summary_by_transport.csv", index=False)

# Create modern dashboard-style visualization
plt.figure(figsize=(8, 5))

colors = ["#d62728" if x < 0 else "#2ca02c" for x in summary["net_impact"]]

bars = plt.barh(summary["transport_mode"], summary["net_impact"], color=colors)

plt.axvline(0, linewidth=1)

plt.title("Net Carbon Impact by Transport Mode", fontsize=14)
plt.xlabel("Net Impact (tCO₂)")
plt.ylabel("")

# Add value labels
for i, v in enumerate(summary["net_impact"]):
    plt.text(v, i, f"{v:.2f}", va='center')

plt.tight_layout()
plt.savefig("impact_chart.png")

print("Analysis complete. Files generated.")
