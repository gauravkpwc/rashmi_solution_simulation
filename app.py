import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title
st.title("Waste Heat Recovery Simulator")

# Sidebar Inputs
st.sidebar.header("Input Parameters")
exhaust_air_used = st.sidebar.slider("% of Exhaust Air Used", 0, 100, 50)
exhaust_temp = st.sidebar.slider("Exhaust Temperature (°C)", 100, 600, 300)
recovery_efficiency = st.sidebar.slider("Recovery System Efficiency (%)", 0, 100, 70)
base_energy = st.sidebar.slider("Base Energy Consumption (kWh/ton)", 500, 2000, 1000)
cost_per_kwh = st.sidebar.slider("Energy Cost (INR/kWh)", 5, 15, 10)

# Calculations
usable_energy_fraction = (exhaust_air_used / 100) * (recovery_efficiency / 100)
energy_saved = base_energy * usable_energy_fraction
cost_saved = energy_saved * cost_per_kwh

# Results
st.subheader("Simulation Results")
st.metric("Estimated Energy Saved (kWh/ton)", f"{energy_saved:.2f}")
st.metric("Estimated Cost Saved (INR/ton)", f"{cost_saved:.2f}")

# Visualization
labels = ['Energy Saved (kWh/ton)', 'Cost Saved (INR/ton)']
values = [energy_saved, cost_saved]
colors = ['orange', 'green']

fig, ax = plt.subplots()
ax.bar(labels, values, color=colors)
ax.set_title("Waste Heat Recovery Impact")
ax.set_ylabel("Value")
st.pyplot(fig)
