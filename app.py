import zipfile
import streamlit as st
import pandas as pd
import joblib

# ==========================================
# LOAD MODEL
# ==========================================
with zipfile.ZipFile("house_price_pipeline.zip", "r") as zip_ref:
    zip_ref.extract("house_price_pipeline.pkl", ".")
model = joblib.load("house_price_pipeline.pkl")
schema = joblib.load("input_schema.pkl")

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="House Price AI | AMIR SEDGHI",
    page_icon="🏠",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================
st.markdown("""
<style>

.stApp {
    background-color: #0b1120;
    color: #e2e8f0;
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

header[data-testid="stHeader"] {
    background-color: transparent;
}

h1, h2, h3 {
    color: #f8fafc !important;
}

p, label {
    color: #cbd5e1;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, #172554, #1d4ed8);
    padding: 40px;
    border-radius: 24px;
    border: 1px solid #3b82f6;
    margin-bottom: 30px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    color: white;
}

.hero-subtitle {
    font-size: 17px;
    color: #bfdbfe;
    margin-top: 10px;
}

/* Sections */
div[data-testid="stExpander"] {
    background: #111c31;
    border: 1px solid #263b5b;
    border-radius: 16px;
    margin-bottom: 12px;
}

/* Form */
div[data-testid="stForm"] {
    background: #0f1a2e;
    border: 1px solid #263b5b;
    border-radius: 20px;
    padding: 25px;
}

/* Inputs */
div[data-baseweb="select"] > div {
    background-color: #172338;
    border-color: #334155;
}

div[data-testid="stNumberInput"] input {
    background-color: #172338;
    color: white;
    border-radius: 10px;
}

/* Buttons */
div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(90deg, #2563eb, #3b82f6);
    color: white;
    border: none;
    border-radius: 12px;
    height: 55px;
    font-size: 17px;
    font-weight: bold;
    transition: 0.3s;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background: linear-gradient(90deg, #1d4ed8, #60a5fa);
    transform: translateY(-2px);
}

/* Prediction Metric */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #142440, #172554);
    padding: 30px;
    border: 1px solid #3b82f6;
    border-radius: 20px;
}

div[data-testid="stMetricLabel"] {
    color: #bfdbfe !important;
}

div[data-testid="stMetricValue"] {
    color: #60a5fa !important;
    font-size: 42px;
    font-weight: 800;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0f172a;
    border-right: 1px solid #1e293b;
}

/* Footer */
.footer {
    text-align: center;
    padding: 35px 10px 15px 10px;
    margin-top: 40px;
}

.footer-label {
    font-size: 11px;
    letter-spacing: 4px;
    color: #64748b;
}

.footer-name {
    font-size: 25px;
    font-weight: 800;
    letter-spacing: 3px;
    color: #60a5fa;
    margin-top: 8px;
}

.footer-desc {
    font-size: 12px;
    color: #64748b;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:

    st.markdown("## 🏠 House Price AI")

    st.markdown("---")

    st.markdown("### About")

    st.write("""
    An intelligent house price
    prediction application powered
    by Machine Learning.
    """)

    st.markdown("---")

    st.markdown("### Model Information")

    st.write("**Algorithm:** Random Forest")
    st.write("**Dataset:** Ames Housing")
    st.write("**Developer:** AMIR SEDGHI")


# ==========================================
# HEADER
# ==========================================
st.markdown("""
<div class="hero">
<div class="hero-title">
🏡 House Price Predictor
</div>
<div class="hero-subtitle">
Smart Real Estate Valuation Platform
<br>
Estimate house prices using Machine Learning.
</div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# FEATURE GROUPS
# ==========================================
groups = {

    "🏡 General Information": [
        "MS SubClass", "MS Zoning", "Bldg Type",
        "House Style", "Neighborhood", "Street",
        "Alley", "Lot Shape", "Land Contour",
        "Lot Config", "Land Slope", "Condition1",
        "Condition2", "Utilities"
    ],

    "📐 Land & Area": [
        "Lot Frontage", "Lot Area",
        "Gr Liv Area", "1st Flr SF",
        "2nd Flr SF", "Low Qual Fin SF",
        "BsmtFin SF 1", "BsmtFin SF 2",
        "Bsmt Unf SF", "Total Bsmt SF"
    ],

    "🧱 Quality & Condition": [
        "Overall Qual", "Overall Cond",
        "Exter Qual", "Exter Cond",
        "Bsmt Qual", "Bsmt Cond",
        "Kitchen Qual", "Heating QC",
        "Garage Qual", "Garage Cond"
    ],

    "🛏️ Rooms & Facilities": [
        "Bedroom AbvGr", "Full Bath",
        "Half Bath", "Bsmt Full Bath",
        "Bsmt Half Bath", "TotRms AbvGrd",
        "Kitchen AbvGr", "Fireplaces",
        "Garage Cars", "Garage Area"
    ],

    "📅 Construction & Age": [
        "Year Built", "Year Remod/Add",
        "Garage Yr Blt", "Mo Sold",
        "Yr Sold"
    ],

    "🚗 Garage & Exterior": [
        "Garage Type", "Garage Finish",
        "Paved Drive", "Roof Style",
        "Roof Matl", "Exterior 1st",
        "Exterior 2nd", "Foundation"
    ]
}

# ==========================================
# GROUP REMAINING FEATURES
# ==========================================
assigned = []

for features in groups.values():
    assigned.extend(features)

groups["⚙️ Other Details"] = [
    feature for feature in schema
    if feature not in assigned
]

# ==========================================
# INPUT FORM
# ==========================================
st.markdown("## 📋 Property Information")

st.write(
    "Enter the property details below. "
    "Open each section to customize the house information."
)

user_data = {}

with st.form("prediction_form"):

    for group_name, features in groups.items():

        available_features = [
            feature for feature in features
            if feature in schema
        ]

        if not available_features:
            continue

        with st.expander(group_name, expanded=False):

            columns = st.columns(3)

            for i, feature in enumerate(available_features):

                info = schema[feature]

                with columns[i % 3]:

                    if info["type"] == "categorical":

                        options = info["options"]

                        if not options:
                            options = ["None"]

                        user_data[feature] = st.selectbox(
                            feature,
                            options=options
                        )

                    else:

                        user_data[feature] = st.number_input(
                            feature,
                            value=float(info["default"])
                        )

    st.markdown("---")

    submitted = st.form_submit_button(
        "🔍  PREDICT HOUSE PRICE",
        use_container_width=True
    )

# ==========================================
# PREDICTION RESULT
# ==========================================
if submitted:

    input_df = pd.DataFrame([user_data])

    prediction = model.predict(input_df)[0]

    st.markdown("---")

    st.markdown("## 💰 Prediction Result")

    st.metric(
        label="Estimated Property Value",
        value=f"${prediction:,.0f}"
    )

    st.success(
        "The house price has been estimated successfully."
    )

    st.caption(
        "This prediction is an estimate generated by a "
        "Machine Learning model and is not a professional appraisal."
    )


# ==========================================
# DEVELOPER FOOTER
# ==========================================
st.markdown("""
<div style="
    background-color: #111c31;
    border: 1px solid #3b82f6;
    border-radius: 18px;
    padding: 30px;
    margin-top: 50px;
    text-align: center;
">

<div style="
    font-size: 12px;
    letter-spacing: 4px;
    color: #94a3b8;
">
DEVELOPED BY
</div>

<div style="
    font-size: 26px;
    font-weight: 800;
    letter-spacing: 3px;
    color: #60a5fa;
    margin-top: 10px;
">
AMIR SEDGHI
</div>

<div style="
    font-size: 12px;
    color: #64748b;
    margin-top: 12px;
">
HOUSE PRICE AI • MACHINE LEARNING PROJECT
</div>

</div>
""", unsafe_allow_html=True)
