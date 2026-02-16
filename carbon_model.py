import pandas as pd

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

# Save results to CSV
df.to_csv("results.csv", index=False)

print("Results file generated successfully")

# Aggregated analysis by transport mode
summary = df.groupby("transport_mode")["net_impact"].sum().reset_index()

summary.to_csv("summary_by_transport.csv", index=False)

print("\nSummary by transport mode:")
print(summary)
