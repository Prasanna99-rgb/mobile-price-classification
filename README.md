# 📱 Mobile Price Classification

A Machine Learning web application that predicts the **price category of a mobile phone** based on its technical specifications. This project uses a trained **Support Vector Classifier (SVC)** model and is deployed using Streamlit.

---

## 🚀 Live Demo

🔗 **Try the Application Here:**

https://mobile-price-classification-tw5rxbsawmugzvgxy674bm.streamlit.app/

---

## 📌 Project Overview

The objective of this project is to classify mobile phones into different price categories based on their hardware and software specifications.

The model analyzes various mobile features such as battery capacity, RAM, processor cores, camera specifications, screen dimensions, connectivity options, and more to predict the corresponding mobile price range.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Pickle

---

## 📊 Features Used for Prediction

| Feature       | Description          |
| ------------- | -------------------- |
| battery_power | Battery Capacity     |
| blue          | Bluetooth Support    |
| clock_speed   | Processor Speed      |
| dual_sim      | Dual SIM Support     |
| fc            | Front Camera MP      |
| four_g        | 4G Support           |
| int_memory    | Internal Memory      |
| m_dep         | Mobile Depth         |
| mobile_wt     | Mobile Weight        |
| n_cores       | Number of CPU Cores  |
| pc            | Primary Camera MP    |
| px_height     | Pixel Height         |
| px_width      | Pixel Width          |
| ram           | RAM Capacity         |
| sc_h          | Screen Height        |
| sc_w          | Screen Width         |
| talk_time     | Battery Talk Time    |
| three_g       | 3G Support           |
| touch_screen  | Touch Screen Support |
| wifi          | WiFi Support         |

---

## 🎯 Target Variable

The model predicts one of the following price categories:

| Class | Price Category |
| ----- | -------------- |
| 0     | Low Cost       |
| 1     | Medium Cost    |
| 2     | High Cost      |
| 3     | Very High Cost |

---

## 📂 Project Structure

```bash
Mobile-Price-Classification/
│
├── app.py
├── Best.pkl
├── requirements.txt
├── README.md
└── mobile_price_classification.ipynb
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Prasanna99-rgb/mobile-price-classification.git
cd mobile-price-classification
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📈 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Selection
5. Model Training
6. Model Evaluation
7. Model Deployment using Streamlit

---

## 📋 Requirements

```txt
streamlit
pandas
numpy
scikit-learn
```

---

## 👨‍💻 Author

**Prasanna Deshmane**

GitHub: https://github.com/Prasanna99-rgb

LinkedIn: https://www.linkedin.com/in/prasanna-deshmane-80a419205

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
It helps support the project and encourages further development.

---

### Made with ❤️ using Python, Scikit-Learn and Streamlit
