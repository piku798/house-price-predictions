# Load trained model and make predictions
# src/predict.py

import pickle
import pandas as pd
import numpy as np

def load_model(model_path):
    """Load the trained model from .pkl file."""
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def load_selected_features(features_path):
    """Load selected feature names from a .pkl file."""
    with open(features_path, 'rb') as file:
        selected_features = pickle.load(file)
    return selected_features

def make_prediction(input_data, model, selected_features):
    """
    Predict using the model on only selected features.

    Parameters:
    - input_data: pd.DataFrame with all input features
    - model: Trained model
    - selected_features: List of selected feature names

    Returns:
    - np.ndarray of predictions
    """
    if not isinstance(input_data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame")
    
    # Filter and reorder columns based on selected features
    input_data_filtered = input_data[selected_features]
    
    return model.predict(input_data_filtered)
