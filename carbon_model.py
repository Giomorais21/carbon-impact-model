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
summary.to_csv("summary_by_transport.csv", index=False)

# Create visualization
plt.figure()
summary.plot(kind="bar", x="transport_mode", y="net_impact", legend=False)
plt.title("Net Carbon Impact by Transport Mode")
plt.xlabel("Transport Mode")
plt.ylabel("Net Impact (tCO2)")
plt.tight_layout()
plt.savefig("impact_chart.png")

print("Analysis complete. Files generated.")
