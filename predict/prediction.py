from joblib import load
import pandas as pd
from typing import Dict
from preprocessing.cleaning_data import preprocess
import numpy as np

def predict(input_data: Dict) -> float:
    """
     Predict house price using preprocessed data.
    
    Args:
        input_data (Dict): Raw input data.
        
    Returns:
        float: Predicted house price.
    """
    # Load the saved model
    model = load("real_estate_model.joblib")

    # Preprocess data
    preprocessed_data = preprocess(input_data)
    
    # Predict price
    predicted_price = model.predict(preprocessed_data)[0]
    return round(predicted_price, 2)