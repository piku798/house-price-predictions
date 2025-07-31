# Utility/helper functions
# src/utilities.py

import pickle
from sklearn.model_selection import train_test_split

def save_model(model, path):
    """
    Save a trained model to a file using pickle.
    
    Parameters:
    - model: trained model object
    - path: file path to save the model
    """
    with open(path, 'wb') as file:
        pickle.dump(model, file)
    print(f"✅ Model saved to: {path}")

def load_model(path):
    """
    Load a trained model from a pickle file.
    
    Parameters:
    - path: path to the saved model file (.pkl)
    
    Returns:
    - model object
    """
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model

def save_selected_features(features_list, path):
    """
    Save selected feature names to a pickle file.
    
    Parameters:
    - features_list: list of selected feature names
    - path: file path to save the list
    """
    with open(path, 'wb') as file:
        pickle.dump(features_list, file)
    print(f"✅ Selected features saved to: {path}")

def load_selected_features(path):
    """
    Load selected feature names from a pickle file.
    
    Parameters:
    - path: path to the saved selected feature list
    
    Returns:
    - list of selected features
    """
    with open(path, 'rb') as file:
        features = pickle.load(file)
    return features

def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets.
    
    Parameters:
    - X: Features (DataFrame)
    - y: Target (Series)
    - test_size: float (default=0.2)
    - random_state: int (default=42)
    
    Returns:
    - X_train, X_test, y_train, y_test
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
