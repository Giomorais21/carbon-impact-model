import pandas as pd

# Sample dataset (fictional data)
data = {
    "waste_tons": [10, 5, 8],
    "transport_mode": ["road", "air", "maritime"],
    "emission_factor_transport": [0.12, 0.6, 0.04],  # tCO2 per ton
    "avoided_emission_factor": [0.5, 0.5, 0.5]  # tCO2 avoided per ton
}

df = pd.DataFrame(data)

# Calculate avoided emissions
df["avoided_emissions"] = df["waste_tons"] * df["avoided_emission_factor"]

# Calculate transport emissions
df["transport_emissions"] = df["waste_tons"] * df["emission_factor_transport"]

# Net carbon impact
df["net_impact"] = df["avoided_emissions"] - df["transport_emissions"]

print(df)


