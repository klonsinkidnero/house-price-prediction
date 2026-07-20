import streamlit as st
import joblib
import pandas as pd 
try:
    # Load the trained model
    model = joblib.load("./models/house_price_model.pkl")

    #load the feature list
    feature_names = joblib.load("./models/features.pkl")

except Exception as e:
    st.error(f"Could not load model: {e}")
    st.stop()

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state= 'expanded'
)
st.sidebar.title("🏡 About This Project")
st.title("🏡 House Price Prediction")

st.sidebar.write("""
This application predicts house prices using
a trained Gradient Boosting Machine Learning model.
""")
st.sidebar.divider()
st.sidebar.subheader("Model Information")

st.sidebar.write("""
Model:
Gradient Boosting Regressor

Features:
211 Engineered Features

Evaluation:

Average Prediction Error (MAE)

16,085

Average diffrence in root mean sqaure erro(RMSE) 
    
26,047

Accuracy score(r2) 
91.15%
""")
st.sidebar.divider()
st.sidebar.subheader("Developer")
st.sidebar.write("""
Developer

ADEYEMI OLUWANIFEMI

Machine Learning Engineer

Built using:

• Python

• Pandas

• Scikit-Learn

• Streamlit
""")

st.caption(
    "Estimate a home's selling price using a trained Machine Learning model."
)
with st.expander("📖 How to Use This Application"):

    st.write("""
    1. Enter the details of the house.
    2. Fill in all required fields.
    3. Click **Predict House Price**.
    4. View the estimated selling price.
    """)

st.markdown("""
This application predicts the selling price of a house using a trained
Gradient Boosting Machine Learning model.

Enter the property details below and click **Predict House Price**.
""")


with st.form("prediction form"):
    Property_quality, construction, Garage = st.columns(3)
    with Property_quality:
        st.subheader("🏠 Property Details")
        overall_qual = st.number_input(
            "Overall Quality (1-10)",
            min_value=1,
            max_value=10,
            value=5,
            help="Rate the overall material and finish quality of the house."
        )

        gr_liv_area = st.number_input(
            "Above Ground Living Area (sq ft)",
            min_value=100,
            value=1500
        )

    with construction:
        st.subheader('🏗 Construction')
        total_bsmt_sf = st.number_input(
            "Total Basement Area (sq ft)",
            min_value=0,
            value=800
        )

        year_built = st.number_input(
            "Year Built",
            min_value=1800,
            max_value=2026,
            value=2000
        )

    with Garage:
        st.subheader("🚗 Garage")
        garage_cars = st.number_input(
            "Garage Capacity (cars)",
            min_value=0,
            max_value=5,
            value=2
        )

               
    
    predict = st.form_submit_button('🏠 Predict House Price')

    if predict:
        house_data = pd.DataFrame(
        0,
        index=[0],
        columns=feature_names
        )
        house_data.loc[0, "overallqual"] = overall_qual
        house_data.loc[0, "grlivarea"] = gr_liv_area
        house_data.loc[0, "garagecars"] = garage_cars
        house_data.loc[0, "yearbuilt"] = year_built
        house_data.loc[0, "totalbsmtsf"] = total_bsmt_sf
        
        try:
            prediction = model.predict(house_data)
            price = prediction[0]

            st.metric(
            label="Estimated House Price",
            value=f"${price:,.2f}"
            )
            st.info(
            "This prediction is an estimate generated "
            "by a machine learning model and should "
            "not replace a professional property valuation."
            )
        
        except Exception as e:
            st.error(f"prediction failed check your input or try again later ")
        
    
