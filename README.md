# Carbon Impact Model

## 📌 Project Objective

This project simulates a structured carbon impact analysis to evaluate waste management scenarios and quantify net environmental impact considering transportation variables.

The goal is to demonstrate applied data analytics techniques, including feature engineering, metric modeling and aggregated insight extraction.

---

## 🌍 Business Context

Environmental decision-making requires evaluating more than just avoided emissions.

Key analytical questions addressed:

- Does reuse always compensate transport emissions?
- How does transportation mode influence environmental viability?
- At what point does distance eliminate environmental benefit?

This project models these dynamics using structured environmental data.

---

## 📁 Dataset

The dataset (`data.csv`) contains fictional but structured records including:

- Waste type
- Quantity (tons)
- Destination type (reuse vs disposal)
- Transport mode
- Distance (km)
- Emission factors
- Avoided emission factors

The dataset simulates real-world environmental analytics scenarios.

---

## ⚙️ Analytical Methodology

### 1️⃣ Feature Engineering

New analytical variables were derived:

- **Avoided Emissions**
- **Transport Emissions**
- **Net Carbon Impact**

```
avoided_emissions = waste_tons × avoided_emission_factor
transport_emissions = waste_tons × distance_km × emission_factor_transport
net_impact = avoided_emissions − transport_emissions
```

---

### 2️⃣ Aggregated Analysis

The model performs grouped analysis by transport mode to identify systemic environmental patterns.

This step transforms operational data into executive-level insights.

---

## 📈 Key Insights

- Air transport can eliminate environmental gains from reuse in long-distance scenarios.
- Maritime transport tends to preserve positive net impact due to lower emission intensity.
- Distance is a critical variable influencing environmental feasibility.
- Disposal scenarios generate exclusively negative environmental outcomes.

This demonstrates how data modeling supports evidence-based decision-making.

---

## 🛠 Tools & Technologies

- Python  
- Pandas  
- GitHub Actions (CI pipeline)  
- Automated artifact generation  

---

## 🔄 Pipeline Structure

The project includes:

- Data ingestion
- Transformation logic
- Automated execution via GitHub Actions
- Results export (`results.csv`)
- Aggregated summary generation

This simulates a basic analytical data pipeline.

---

## 🌟 Disclaimer

This project is a structured demonstration of data analytics applied to environmental modeling concepts.  
All datasets are fictional and created exclusively for portfolio purposes.

---

## ▶ How to Run

```bash
pip install pandas
python carbon_model.py
```
