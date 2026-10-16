# 🏠 House Price Prediction Using Machine Learning

## 📌 Project Overview

This project predicts house prices based on different property features using Machine Learning regression algorithms. It demonstrates an end-to-end ML workflow, including data preprocessing, exploratory data analysis, model training, evaluation, and deployment using Streamlit.

## 🎯 Objectives

- Predict house prices using relevant property features.
- Perform data cleaning and exploratory data analysis (EDA).
- Train and compare multiple Machine Learning regression models.
- Evaluate model performance using standard regression metrics.
- Build an interactive web application for house price prediction.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Model Serialization:** Joblib
- **Web Application:** Streamlit
- **Development Environment:** Visual Studio Code

## 🤖 Machine Learning Algorithms

The project explores the following regression algorithms:

1. **Linear Regression** — establishes a baseline relationship between house features and prices.
2. **Random Forest Regressor** — combines multiple decision trees to predict house prices.
3. **Gradient Boosting Regressor** — builds an ensemble of trees sequentially to improve predictions.

Hyperparameter tuning using GridSearchCV can be used to identify suitable model settings.

## 📊 Dataset

The dataset contains information about residential properties, including features such as:

- Overall Quality
- Above-Ground Living Area
- Number of Bedrooms
- Full and Half Bathrooms
- Year Built
- Garage Capacity
- Total Basement Area

**Target Variable:** `SalePrice`

The model uses selected property features to estimate the selling price.

## ⚙️ Project Workflow

1. Project setup and virtual environment creation.
2. Dataset collection and loading.
3. Data exploration and cleaning.
4. Exploratory Data Analysis (EDA).
5. Feature selection and target identification.
6. Training and testing data split.
7. Model training using regression algorithms.
8. Model evaluation using MAE, RMSE, and R² score.
9. Model comparison and hyperparameter tuning.
10. Saving the trained model using Joblib.
11. Developing an interactive Streamlit application.
12. Testing the application with different property inputs.

## 📁 Project Structure

```text
House Price Prediction/
│
├── data/
│   └── house_prices.csv
│
├── models/
│   └── house_price_model.pkl
│
├── notebooks/
│   └── house_price_prediction.ipynb
│
├── train.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

*The structure above is an example; adjust the filenames to match the actual files in your repository.*

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/House-Price-Prediction.git
```

### 2. Navigate to the project directory

```bash
cd House-Price-Prediction
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install the dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal to use the application.

## 📈 Model Evaluation

The models are evaluated using the following metrics:

- **Mean Absolute Error (MAE):** Measures the average absolute difference between actual and predicted prices.
- **Root Mean Squared Error (RMSE):** Measures prediction error while penalizing larger errors more heavily.
- **R² Score:** Measures model performance relative to a mean-prediction baseline.

Actual evaluation results depend on the dataset, preprocessing, and model configuration.

## 💡 Key Learnings

- Working with real-world datasets using Pandas and NumPy.
- Performing data cleaning and exploratory data analysis.
- Understanding supervised learning and regression algorithms.
- Evaluating and comparing Machine Learning models.
- Applying hyperparameter tuning and cross-validation.
- Saving trained models and integrating them into a web application.

## 🔮 Future Improvements

- Train the model on real estate data from Indian cities.
- Incorporate location, property age, and nearby amenities.
- Experiment with advanced gradient-boosting algorithms.
- Improve the user interface and input validation.
- Deploy the application to a cloud hosting platform.

## 👨‍💻 Author

**Manish Kumar**

B.Tech CSE (Artificial Intelligence and Machine Learning)

GitHub: https://github.com/mannii0105
