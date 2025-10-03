import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title
st.title("Waste Heat Recovery Simulator")

# Sidebar Inputs for three cases
st.sidebar.header("Input Parameters")

st.sidebar.subheader("Case 1")
exhaust_air_used1 = st.sidebar.slider("Exhaust Air Used (%) - Case 1", 0, 100, 50)
exhaust_temp1 = st.sidebar.slider("Exhaust Temperature (°C) - Case 1", 100, 600, 300)
recovery_efficiency1 = st.sidebar.slider("Recovery Efficiency (%) - Case 1", 0, 100, 70)
base_energy1 = st.sidebar.slider("Base Energy Consumption (kWh/ton) - Case 1", 500, 2000, 1000)

st.sidebar.subheader("Case 2")
exhaust_air_used2 = st.sidebar.slider("Exhaust Air Used (%) - Case 2", 0, 100, 60)
exhaust_temp2 = st.sidebar.slider("Exhaust Temperature (°C) - Case 2", 100, 600, 350)
recovery_efficiency2 = st.sidebar.slider("Recovery Efficiency (%) - Case 2", 0, 100, 75)
base_energy2 = st.sidebar.slider("Base Energy Consumption (kWh/ton) - Case 2", 500, 2000, 1200)

st.sidebar.subheader("Case 3")
exhaust_air_used3 = st.sidebar.slider("Exhaust Air Used (%) - Case 3", 0, 100, 40)
exhaust_temp3 = st.sidebar.slider("Exhaust Temperature (°C) - Case 3", 100, 600, 250)
recovery_efficiency3 = st.sidebar.slider("Recovery Efficiency (%) - Case 3", 0, 100, 65)
base_energy3 = st.sidebar.slider("Base Energy Consumption (kWh/ton) - Case 3", 500, 2000, 900)

# Fixed thermal energy cost
thermal_energy_cost = 1.2

# Calculation function
def calculate_savings(exhaust_air_used, exhaust_temp, recovery_efficiency, base_energy, cost_per_kwh):
    usable_energy_fraction = (exhaust_air_used / 100) * (recovery_efficiency / 100)
    energy_saved = base_energy * usable_energy_fraction
    cost_saved = energy_saved * cost_per_kwh
    return energy_saved, cost_saved

# Calculate for each case
energy1, cost1 = calculate_savings(exhaust_air_used1, exhaust_temp1, recovery_efficiency1, base_energy1, thermal_energy_cost)
energy2, cost2 = calculate_savings(exhaust_air_used2, exhaust_temp2, recovery_efficiency2, base_energy2, thermal_energy_cost)
energy3, cost3 = calculate_savings(exhaust_air_used3, exhaust_temp3, recovery_efficiency3, base_energy3, thermal_energy_cost)

# Display Results
st.subheader("Simulation Results")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Case 1")
    st.markdown(f"**Input Parameters:**")
    st.markdown(f"- Exhaust Air Used: {exhaust_air_used1}%")
    st.markdown(f"- Exhaust Temperature: {exhaust_temp1}°C")
    st.markdown(f"- Recovery Efficiency: {recovery_efficiency1}%")
    st.markdown(f"- Base Energy: {base_energy1} kWh/ton")
    st.markdown(f"**Output:**")
    st.metric("Energy Saved (kWh/ton)", f"{energy1:.2f}")
    st.metric("Cost Saved (INR/ton)", f"{cost1:.2f}")

with col2:
    st.markdown("### Case 2")
    st.markdown(f"**Input Parameters:**")
    st.markdown(f"- Exhaust Air Used: {exhaust_air_used2}%")
    st.markdown(f"- Exhaust Temperature: {exhaust_temp2}°C")
    st.markdown(f"- Recovery Efficiency: {recovery_efficiency2}%")
    st.markdown(f"- Base Energy: {base_energy2} kWh/ton")
    st.markdown(f"**Output:**")
    st.metric("Energy Saved (kWh/ton)", f"{energy2:.2f}")
    st.metric("Cost Saved (INR/ton)", f"{cost2:.2f}")

with col3:
    st.markdown("### Case 3")
    st.markdown(f"**Input Parameters:**")
    st.markdown(f"- Exhaust Air Used: {exhaust_air_used3}%")
    st.markdown(f"- Exhaust Temperature: {exhaust_temp3}°C")
    st.markdown(f"- Recovery Efficiency: {recovery_efficiency3}%")
    st.markdown(f"- Base Energy: {base_energy3} kWh/ton")
    st.markdown(f"**Output:**")
    st.metric("Energy Saved (kWh/ton)", f"{energy3:.2f}")
    st.metric("Cost Saved (INR/ton)", f"{cost3:.2f}")

# Bar Chart Visualization
labels = ['Case 1', 'Case 2', 'Case 3']
energy_values = [energy1, energy2, energy3]
cost_values = [cost1, cost2, cost3]

x = np.arange(len(labels))  # label locations
width = 0.35  # width of the bars

fig, ax1 = plt.subplots()
bar1 = ax1.bar(x - width/2, energy_values, width, label='Energy Saved (kWh/ton)', color='orange')
ax2 = ax1.twinx()
bar2 = ax2.bar(x + width/2, cost_values, width, label='Cost Saved (INR/ton)', color='green')

ax1.set_xlabel('Cases')
ax1.set_ylabel('Energy Saved (kWh/ton)', color='orange')
ax2.set_ylabel('Cost Saved (INR/ton)', color='green')
ax1.set_title('Waste Heat Recovery Impact')
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=2)

st.pyplot(fig)
