# 🏠 House Price Predictor

An AI-powered web application that predicts house prices using Machine Learning.

## 📌 Project Overview

House Price Predictor is a machine learning project built with Python and Streamlit. It uses a Random Forest Regressor to estimate house prices based on various property features.

The application provides an interactive interface where users can enter property information and receive an estimated price.

## ✨ Features

- Predict house prices using Machine Learning
- Interactive web interface built with Streamlit
- Automated data preprocessing
- Handles missing values
- Supports categorical and numerical features
- Random Forest Regression model

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## 📊 Model Performance

| Metric | Result |
|---|---:|
| R² Score | 0.910 |
| MAE | $15,122 |
| RMSE | $23,118 |

*Evaluation results are based on the test dataset.*

## 🚀 Installation & Usage

1. Clone the repository:

```bash
git clone https://github.com/amir13895/HousePricePredictor.git
```

2. Navigate to the project directory:

```bash
cd HousePricePredictor
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
streamlit run app.py
```

## 📁 Project Structure

```text
HousePricePredictor/
├── app.py
├── house_price_pipeline.zip
├── input_schema.pkl
├── model_training.ipynb
└── requirements.txt
```

## 👨‍💻 Author

**Amir Sedghi**

Machine Learning & Python Developer

---

⭐ If you find this project interesting, consider giving it a star!
