import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Title
st.title("Waste Heat Recovery Simulator")

# Sidebar Inputs for three cases
st.sidebar.header("Input Parameters")

def get_case_inputs(case_name):
    st.sidebar.subheader(case_name)
    exhaust_air_used = st.sidebar.slider(f"{case_name} - % of Exhaust Air Used", 0, 100, 50)
    exhaust_temp = st.sidebar.slider(f"{case_name} - Exhaust Temperature (°C)", 100, 600, 300)
    recovery_efficiency = st.sidebar.slider(f"{case_name} - Recovery Efficiency (%)", 0, 100, 70)
    base_energy = st.sidebar.slider(f"{case_name} - Base Energy Consumption (kWh/ton)", 500, 2000, 1000)
    return exhaust_air_used, exhaust_temp, recovery_efficiency, base_energy

case1 = get_case_inputs("Case 1")
case2 = get_case_inputs("Case 2")
case3 = get_case_inputs("Case 3")

# Constants
thermal_cost_per_kwh = 1.2

# Calculation function
def calculate_savings(exhaust_air_used, exhaust_temp, recovery_efficiency, base_energy, cost_per_kwh):
    usable_energy_fraction = (exhaust_air_used / 100) * (recovery_efficiency / 100)
    energy_saved = base_energy * usable_energy_fraction
    cost_saved = energy_saved * cost_per_kwh
    return energy_saved, cost_saved

# Calculate for each case
energy1, cost1 = calculate_savings(*case1, thermal_cost_per_kwh)
energy2, cost2 = calculate_savings(*case2, thermal_cost_per_kwh)
energy3, cost3 = calculate_savings(*case3, thermal_cost_per_kwh)

# Prepare data for table
data = {
    "Case 1": [case1[0], case1[1], case1[2], case1[3], energy1, cost1],
    "Case 2": [case2[0], case2[1], case2[2], case2[3], energy2, cost2],
    "Case 3": [case3[0], case3[1], case3[2], case3[3], energy3, cost3]
}
index = ["Exhaust Air Used (%)", "Exhaust Temperature (°C)", "Recovery Efficiency (%)", 
         "Base Energy (kWh/ton)", "Energy Saved (kWh/ton)", "Cost Saved (INR/ton)"]
df = pd.DataFrame(data, index=index)

# Display transposed table with black font
st.subheader("Simulation Summary")
st.markdown(
    df.style.set_properties(**{'color': 'black'}).set_table_attributes('style="width:100%"').to_html(),
    unsafe_allow_html=True
)

# Bar chart for cost saved
st.subheader("Cost Saved Comparison")
cases = ["Case 1", "Case 2", "Case 3"]
costs = [cost1, cost2, cost3]
colors = ['#FD5108', '#FE7C39', '#FFAA72']

fig, ax = plt.subplots()
bars = ax.bar(cases, costs, color=colors)
ax.set_ylabel("Cost Saved (INR/ton)")
ax.set_title("Cost Savings by Case")
st.pyplot(fig)
