# Fixed Streamlit code for Waste Heat Recovery Simulator with corrected function signature

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title
st.title("Waste Heat Recovery Simulator")

# Sidebar Inputs for three cases
st.sidebar.header("Input Parameters")

def get_case_inputs(case_name):
    st.sidebar.subheader(case_name)
    exhaust_air_used = st.sidebar.slider(f"{case_name} - % of Exhaust Air Used", 0, 100, 50)
    exhaust_temp = st.sidebar.slider(f"{case_name} - Exhaust Temperature (°C)", 100, 600, 300)
    recovery_efficiency = st.sidebar.slider(f"{case_name} - Recovery System Efficiency (%)", 0, 100, 70)
    base_energy = st.sidebar.slider(f"{case_name} - Base Energy Consumption (kWh/ton)", 500, 2000, 1000)
    return exhaust_air_used, exhaust_temp, recovery_efficiency, base_energy

case1 = get_case_inputs("Case 1")
case2 = get_case_inputs("Case 2")
case3 = get_case_inputs("Case 3")

# Constants
electrical_cost_per_kwh = 10  # INR
thermal_cost_per_kwh = 1.2    # INR

# Calculation function
def calculate_savings(exhaust_air_used, exhaust_temp, recovery_efficiency, base_energy, cost_per_kwh):
    usable_energy_fraction = (exhaust_air_used / 100) * (recovery_efficiency / 100)
    energy_saved = base_energy * usable_energy_fraction
    cost_saved = energy_saved * cost_per_kwh
    return energy_saved, cost_saved

# Calculate for each case
energy1, cost1 = calculate_savings(*case1, electrical_cost_per_kwh)
energy2, cost2 = calculate_savings(*case2, electrical_cost_per_kwh)
energy3, cost3 = calculate_savings(*case3, electrical_cost_per_kwh)

# Display Results Side by Side
st.subheader("Simulation Results")
col1, col2 = st.columns(2)
with col1:
    st.metric("Case 1 - Energy Saved (kWh/ton)", f"{energy1:.2f}")
    st.metric("Case 2 - Energy Saved (kWh/ton)", f"{energy2:.2f}")
    st.metric("Case 3 - Energy Saved (kWh/ton)", f"{energy3:.2f}")
with col2:
    st.metric("Case 1 - Cost Saved (INR/ton)", f"{cost1:.2f}")
    st.metric("Case 2 - Cost Saved (INR/ton)", f"{cost2:.2f}")
    st.metric("Case 3 - Cost Saved (INR/ton)", f"{cost3:.2f}")

# Visualization: Combo Line Chart
st.subheader("Waste Heat Recovery Impact")

fig, ax1 = plt.subplots()

# Energy Saved Line (Left Axis)
ax1.set_xlabel("Cases")
ax1.set_ylabel("Energy Saved (kWh/ton)", color='tab:blue')
ax1.plot(["Case 1", "Case 2", "Case 3"], [energy1, energy2, energy3], marker='o', color='tab:blue', label='Energy Saved')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Cost Saved Line (Right Axis)
ax2 = ax1.twinx()
ax2.set_ylabel("Cost Saved (INR/ton)", color='tab:green')
ax2.plot(["Case 1", "Case 2", "Case 3"], [cost1, cost2, cost3], marker='s', color='tab:green', label='Cost Saved')
ax2.tick_params(axis='y', labelcolor='tab:green')

fig.tight_layout()
st.pyplot(fig)
