# Basic test for prediction function
# testmodel.py

import pandas as pd
from src.predict import load_model, load_selected_features, make_prediction
from src.config import MODEL_PATH, FEATURES_PATH

def test_model(input_csv_path):
    """
    Load the model and selected features, read test data, and print predictions.

    Parameters:
    - input_csv_path (str): path to the CSV file containing test data.
    """
    # Step 1: Load the trained model
    model = load_model(MODEL_PATH)
    print("✅ Model loaded successfully.")

    # Step 2: Load the selected feature names
    selected_features = load_selected_features(FEATURES_PATH)
    print(f"✅ Selected features: {selected_features}")

    # Step 3: Load and prepare input data
    input_df = pd.read_csv(input_csv_path)

    # Check if all selected features are present
    missing = set(selected_features) - set(input_df.columns)
    if missing:
        raise ValueError(f"Missing columns in input data: {missing}")

    # Step 4: Make predictions
    predictions = make_prediction(input_df, model, selected_features)

    # Step 5: Output results
    for i, pred in enumerate(predictions, start=1):
        print(f"Prediction {i}: ₹{pred:,.2f}")

if __name__ == "__main__":
    # You can change this to point to any CSV with your test input
    input_csv = "data/sample_input.csv"
    test_model(input_csv)
