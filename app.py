import streamlit as st
import pickle
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Mobile Price Classification",
    page_icon="📱",
    layout="wide"
)

# Load Model
model = pickle.load(open("Best_model.pkl", "rb"))

# Title
st.title("📱 Mobile Price Classification App")
st.markdown("Predict the mobile price range based on specifications.")

# Sidebar Inputs
st.sidebar.header("Enter Mobile Specifications")

battery_power = st.sidebar.number_input("Battery Power", min_value=500, max_value=2500, value=1500)
blue = st.sidebar.selectbox("Bluetooth", [0, 1])
clock_speed = st.sidebar.number_input("Clock Speed", min_value=0.5, max_value=5.0, value=2.0)
dual_sim = st.sidebar.selectbox("Dual SIM", [0, 1])
fc = st.sidebar.number_input("Front Camera (MP)", min_value=0, max_value=25, value=5)
four_g = st.sidebar.selectbox("4G Support", [0, 1])
int_memory = st.sidebar.number_input("Internal Memory (GB)", min_value=2, max_value=128, value=32)
m_dep = st.sidebar.number_input("Mobile Depth", min_value=0.1, max_value=1.0, value=0.5)
mobile_wt = st.sidebar.number_input("Mobile Weight (g)", min_value=80, max_value=250, value=150)
n_cores = st.sidebar.number_input("Number of Cores", min_value=1, max_value=8, value=4)
pc = st.sidebar.number_input("Primary Camera (MP)", min_value=0, max_value=50, value=12)
px_height = st.sidebar.number_input("Pixel Height", min_value=0, max_value=3000, value=1000)
px_width = st.sidebar.number_input("Pixel Width", min_value=0, max_value=3000, value=1500)
ram = st.sidebar.number_input("RAM (MB)", min_value=256, max_value=8000, value=4000)
sc_h = st.sidebar.number_input("Screen Height", min_value=5, max_value=25, value=15)
sc_w = st.sidebar.number_input("Screen Width", min_value=1, max_value=20, value=8)
talk_time = st.sidebar.number_input("Talk Time (Hours)", min_value=2, max_value=30, value=15)
three_g = st.sidebar.selectbox("3G Support", [0, 1])
touch_screen = st.sidebar.selectbox("Touch Screen", [0, 1])
wifi = st.sidebar.selectbox("WiFi", [0, 1])

# Create DataFrame
input_data = pd.DataFrame({
    'battery_power': [battery_power],
    'blue': [blue],
    'clock_speed': [clock_speed],
    'dual_sim': [dual_sim],
    'fc': [fc],
    'four_g': [four_g],
    'int_memory': [int_memory],
    'm_dep': [m_dep],
    'mobile_wt': [mobile_wt],
    'n_cores': [n_cores],
    'pc': [pc],
    'px_height': [px_height],
    'px_width': [px_width],
    'ram': [ram],
    'sc_h': [sc_h],
    'sc_w': [sc_w],
    'talk_time': [talk_time],
    'three_g': [three_g],
    'touch_screen': [touch_screen],
    'wifi': [wifi]
})

# Prediction
if st.button("Predict Price Range"):
    prediction = model.predict(input_data)[0]

    price_ranges = {
        0: "Low Cost",
        1: "Medium Cost",
        2: "High Cost",
        3: "Very High Cost"
    }

    st.success(f"Predicted Price Range: {price_ranges[prediction]}")

    st.subheader("Input Specifications")
    st.dataframe(input_data)
