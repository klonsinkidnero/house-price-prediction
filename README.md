# 🏡 House Price Prediction using Machine Learning

## 💼 Business Impact

This application helps reduce uncertainty when estimating house prices by providing fast, data-driven predictions based on key property characteristics.

Potential use cases include:

- Assisting home buyers with budgeting
- Supporting homeowners in estimating property value
- Helping real estate professionals make faster pricing decisions
- Demonstrating how Machine Learning can solve real-world business problems

## 📌 Overview

This project is a Machine Learning web application that predicts the selling price of residential houses based on their characteristics.

The application was built to help users reduce uncertainty when estimating property values by providing data-driven price predictions. It can assist prospective home buyers, homeowners, and real estate professionals in making more informed budgeting and purchasing decisions.

The prediction model is deployed through a user-friendly Streamlit web application.

---

## 🚀 Features

- Predicts house prices instantly
- Interactive web interface built with Streamlit
- Professional and responsive user interface
- Input validation to reduce user errors
- Graceful error handling using `try/except`
- Organized input sections for improved user experience
- Uses a trained Gradient Boosting Machine Learning model

---

## 🧠 Machine Learning Workflow

The project follows a complete end-to-end Machine Learning pipeline:

1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Model Selection
7. Model Serialization using Joblib
8. Web Application Deployment with Streamlit

---

## 📊 Model Performance

After comparing multiple Machine Learning algorithms, **Gradient Boosting Regressor** achieved the best performance.

| Metric   |  Score |
| -------- | -----: |
| MAE      | 16,085 |
| RMSE     | 26,047 |
| R² Score | 0.9115 |

The model was selected because it achieved the highest R² score while maintaining the lowest prediction errors.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- VS Code
- Jupyter Notebook

---

## 📂 Project Structure

```
house_pricing/
│
├── data/
├── images/
├── models/
│   ├── house_price_model.pkl
│   └── features.pkl
│
├── notebook/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_training.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ▶️ Running the Project

Clone the repository

```bash
git clone https://github.com/yourusername/house-price-prediction.git
```

Move into the project folder

```bash
cd house-price-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---


## 🎯 What I Learned

Through this project I gained practical experience in:

- Cleaning real-world datasets
- Handling missing values
- Feature engineering
- Comparing Machine Learning algorithms
- Model evaluation using MAE, RMSE and R²
- Saving trained models with Joblib
- Deploying Machine Learning models using Streamlit
- Designing user-friendly interfaces
- Writing production-ready Python code

---

## 🔮 Future Improvements

Given more time, I plan to:

- Add more user input features for improved prediction accuracy
- Collect user feedback to improve the interface
- Continue feature engineering to improve model performance
- Deploy the application publicly
- Add data visualizations and prediction explanations
- Integrate location-based features

---

## 👨‍💻 Author

**ADEYEMI Oluwanifemi John**

Computer Science Graduate

Machine Learning & Data Analytics Enthusiast

GitHub: _(https://github.com/klonsinkidnero)_

LinkedIn: _()_

---

## 📄 License

This project is intended for educational and portfolio purposes.
