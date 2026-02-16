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

print(df)
