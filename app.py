import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

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
exhaust_air_used3 = st.sidebar.slider("Exhaust Air Used (%) - Case 3", 0, 100, 70)
exhaust_temp3 = st.sidebar.slider("Exhaust Temperature (°C) - Case 3", 100, 600, 400)
recovery_efficiency3 = st.sidebar.slider("Recovery Efficiency (%) - Case 3", 0, 100, 80)
base_energy3 = st.sidebar.slider("Base Energy Consumption (kWh/ton) - Case 3", 500, 2000, 1500)

# Fixed thermal energy cost
thermal_cost_per_kwh = 1.2

# Calculation function
def calculate_savings(exhaust_air_used, exhaust_temp, recovery_efficiency, base_energy, cost_per_kwh):
    usable_energy_fraction = (exhaust_air_used / 100) * (recovery_efficiency / 100)
    energy_saved = base_energy * usable_energy_fraction
    cost_saved = energy_saved * cost_per_kwh
    return energy_saved, cost_saved

# Calculate for each case
energy1, cost1 = calculate_savings(exhaust_air_used1, exhaust_temp1, recovery_efficiency1, base_energy1, thermal_cost_per_kwh)
energy2, cost2 = calculate_savings(exhaust_air_used2, exhaust_temp2, recovery_efficiency2, base_energy2, thermal_cost_per_kwh)
energy3, cost3 = calculate_savings(exhaust_air_used3, exhaust_temp3, recovery_efficiency3, base_energy3, thermal_cost_per_kwh)

# Create DataFrame
data = {
    "Case 1": [exhaust_air_used1, exhaust_temp1, recovery_efficiency1, base_energy1, round(energy1, 1), round(cost1, 1)],
    "Case 2": [exhaust_air_used2, exhaust_temp2, recovery_efficiency2, base_energy2, round(energy2, 1), round(cost2, 1)],
    "Case 3": [exhaust_air_used3, exhaust_temp3, recovery_efficiency3, base_energy3, round(energy3, 1), round(cost3, 1)]
}
index = ["Exhaust Air Used (%)", "Exhaust Temperature (°C)", "Recovery Efficiency (%)", "Base Energy (kWh/ton)", "Energy Saved (kWh/ton)", "Cost Saved (INR/ton)"]
df = pd.DataFrame(data, index=index)

# Display transposed table with black font
st.subheader("Simulation Summary")
st.dataframe(df.style.set_properties(**{'color': 'black'}))

# Bar chart for cost saved
st.subheader("Cost Saved Comparison")
fig, ax = plt.subplots()
cases = ['Case 1', 'Case 2', 'Case 3']
costs = [cost1, cost2, cost3]
colors = ['#FD5108', '#FE7C39', '#FFAA72']
ax.bar(cases, costs, color=colors)
ax.set_ylabel("Cost Saved (INR/ton)")
ax.set_title("Cost Saved Across Cases")
st.pyplot(fig)
