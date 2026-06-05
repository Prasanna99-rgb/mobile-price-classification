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
model = pickle.load(open("Best.pkl", "rb"))

# Title
st.title("📱 Mobile Price Classification")
st.markdown("Predict the price range of a mobile phone based on its specifications.")

st.sidebar.header("Enter Mobile Specifications")

# Input Fields
battery_power = st.sidebar.number_input("Battery Power", 500, 3000, 1500)
blue = st.sidebar.selectbox("Bluetooth", [0, 1])
clock_speed = st.sidebar.number_input("Clock Speed", 0.5, 5.0, 2.0)
dual_sim = st.sidebar.selectbox("Dual SIM", [0, 1])
fc = st.sidebar.number_input("Front Camera (MP)", 0, 25, 5)
four_g = st.sidebar.selectbox("4G Support", [0, 1])
int_memory = st.sidebar.number_input("Internal Memory (GB)", 2, 256, 32)
m_dep = st.sidebar.number_input("Mobile Depth", 0.1, 1.0, 0.5)
mobile_wt = st.sidebar.number_input("Mobile Weight (g)", 80, 250, 150)
n_cores = st.sidebar.number_input("Number of Cores", 1, 16, 4)
pc = st.sidebar.number_input("Primary Camera (MP)", 0, 64, 12)
px_height = st.sidebar.number_input("Pixel Height", 0, 4000, 1000)
px_width = st.sidebar.number_input("Pixel Width", 0, 4000, 1500)
ram = st.sidebar.number_input("RAM (MB)", 256, 8000, 4000)
sc_h = st.sidebar.number_input("Screen Height", 5, 25, 12)
sc_w = st.sidebar.number_input("Screen Width", 1, 20, 6)
talk_time = st.sidebar.number_input("Talk Time (hrs)", 1, 30, 10)
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

# prediction
if st.button("Predict Price Range"):

    prediction = int(model.predict(input_data)[0])

    price_ranges = {
        0: "₹0 - ₹10,000",
        1: "₹10,000 - ₹20,000",
        2: "₹20,000 - ₹30,000",
        3: "₹30,000+"
    }

    st.metric(
        label="Estimated Mobile Price",
        value=price_ranges[prediction]
    )

# Footer
st.markdown("---")
st.markdown("Developed by **Prasanna99-rgb** 🚀")
