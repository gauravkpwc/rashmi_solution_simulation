import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title
st.title("Waste Heat Recovery Simulator")

# Sidebar Inputs for three cases
st.sidebar.header("Input Parameters")

def case_inputs(case_name):
    st.sidebar.subheader(case_name)
    exhaust_air_used = st.sidebar.slider(f"% of Exhaust Air Used ({case_name})", 0, 100, 50)
    exhaust_temp = st.sidebar.slider(f"Exhaust Temperature (°C) ({case_name})", 100, 600, 300)
    recovery_efficiency = st.sidebar.slider(f"Recovery System Efficiency (%) ({case_name})", 0, 100, 70)
    base_energy = st.sidebar.slider(f"Base Energy Consumption (kWh/ton) ({case_name})", 500, 2000, 1000)
    return exhaust_air_used, exhaust_temp, recovery_efficiency, base_energy

case1 = case_inputs("Case 1")
case2 = case_inputs("Case 2")
case3 = case_inputs("Case 3")

# Common cost values
electrical_cost_per_kwh = st.sidebar.slider("Electrical Energy Cost (INR/kWh)", 5, 15, 10)
thermal_cost_per_kwh = 1.2

# Function to calculate energy and cost saved
def calculate_savings(exhaust_air_used, recovery_efficiency, base_energy, cost_per_kwh):
    usable_energy_fraction = (exhaust_air_used / 100) * (recovery_efficiency / 100)
    energy_saved = base_energy * usable_energy_fraction
    cost_saved = energy_saved * cost_per_kwh
    return energy_saved, cost_saved

# Calculate for each case
energy1, cost1 = calculate_savings(*case1, electrical_cost_per_kwh)
energy2, cost2 = calculate_savings(*case2, electrical_cost_per_kwh)
energy3, cost3 = calculate_savings(*case3, electrical_cost_per_kwh)

# Display results side by side
st.subheader("Simulation Results")
col1, col2 = st.columns(2)
with col1:
    st.metric("Energy Saved (kWh/ton)", f"{energy1:.2f} (Case 1)")
    st.metric("Energy Saved (kWh/ton)", f"{energy2:.2f} (Case 2)")
    st.metric("Energy Saved (kWh/ton)", f"{energy3:.2f} (Case 3)")
with col2:
    st.metric("Cost Saved (INR/ton)", f"{cost1:.2f} (Case 1)")
    st.metric("Cost Saved (INR/ton)", f"{cost2:.2f} (Case 2)")
    st.metric("Cost Saved (INR/ton)", f"{cost3:.2f} (Case 3)")

# Visualization: Combo Line Chart
fig, ax1 = plt.subplots()

cases = ["Case 1", "Case 2", "Case 3"]
energy_values = [energy1, energy2, energy3]
cost_values = [cost1, cost2, cost3]

ax1.set_xlabel("Cases")
ax1.set_ylabel("Energy Saved (kWh/ton)", color='tab:blue')
ax1.plot(cases, energy_values, marker='o', color='tab:blue', label='Energy Saved')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel("Cost Saved (INR/ton)", color='tab:green')
ax2.plot(cases, cost_values, marker='s', color='tab:green', label='Cost Saved')
ax2.tick_params(axis='y', labelcolor='tab:green')

fig.tight_layout()
plt.title("Waste Heat Recovery Impact Across Cases")
st.pyplot(fig)
