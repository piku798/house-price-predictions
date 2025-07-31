# Code for training the ML model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SelectKBest, f_regression
import joblib

# Load the cleaned dataset
df = pd.read_csv('C:/Users/nnaya/Desktop/JOB/project/house-price-predictions/house-price-predictions/data/processed/cleaned_data.csv')

# Features and target
X = df.drop("medhouseval", axis=1)
y = df["medhouseval"]

# Feature selection
selector = SelectKBest(score_func=f_regression, k=3)
X_selected = selector.fit_transform(X, y)

# Get selected feature names
mask = selector.get_support()
selected_features = X.columns[mask]
print("Selected Features:", list(selected_features))

# Recreate X with selected columns
X = X[selected_features]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'house_price_model.pkl')
print("Model saved as house_price_model.pkl")

# Save selected feature names
joblib.dump(list(selected_features), 'selected_features.pkl')
print("Selected features saved as selected_features.pkl")
