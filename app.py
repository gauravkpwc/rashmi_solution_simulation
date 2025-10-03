import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

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

# Get inputs for each case
case1 = get_case_inputs("Case 1")
case2 = get_case_inputs("Case 2")
case3 = get_case_inputs("Case 3")

# Fixed cost values
electrical_cost_per_kwh = 10
thermal_cost_per_kwh = 1.2

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

# Prepare data for table
data = {
    "Case 1": {
        "Exhaust Air Used (%)": case1[0],
        "Exhaust Temperature (°C)": case1[1],
        "Recovery Efficiency (%)": case1[2],
        "Base Energy (kWh/ton)": case1[3],
        "Energy Saved (kWh/ton)": energy1,
        "Cost Saved (INR/ton)": cost1
    },
    "Case 2": {
        "Exhaust Air Used (%)": case2[0],
        "Exhaust Temperature (°C)": case2[1],
        "Recovery Efficiency (%)": case2[2],
        "Base Energy (kWh/ton)": case2[3],
        "Energy Saved (kWh/ton)": energy2,
        "Cost Saved (INR/ton)": cost2
    },
    "Case 3": {
        "Exhaust Air Used (%)": case3[0],
        "Exhaust Temperature (°C)": case3[1],
        "Recovery Efficiency (%)": case3[2],
        "Base Energy (kWh/ton)": case3[3],
        "Energy Saved (kWh/ton)": energy3,
        "Cost Saved (INR/ton)": cost3
    }
}

# Create DataFrame and transpose
df = pd.DataFrame(data)
df = df.round(1).transpose()

# Display table with black font
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
