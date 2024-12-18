import pandas as pd
import numpy as np
from typing import Dict
import xgboost as xgb

def preprocess(input_data: Dict) -> pd.DataFrame:
    """
    Preprocess input data for the model.

    Args:
    input_data (Dict): Input data containing house features.

    Returns:
    pd.DataFrame: Preprocessed data ready for prediction.

    Raises:
    ValueError: If required data is missing or invalid.
    """
    # Required fields
    required_fields = ["Municipality", 
                    "Living_Area", 
                    "Number_of_Rooms", 
                    "Fully_Equipped_Kitchen", 
                    "Terrace_Area", 
                    "Garden_Area", 
                    "Type_of_Property"]

    # Check for missing fields
    missing = [field for field in required_fields if field not in input_data]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")

    # Fill missing optional fields and preprocess
    df = pd.DataFrame([input_data])

    # Extract text features
    cats = df.select_dtypes(exclude=np.number).columns.tolist()

    # Convert to Pandas category
    for col in cats:
        df[col] = df[col].astype('category')

    # df.fill(0, inplace=True)
    df = xgb.DMatrix(df, label = None, enable_categorical = True)

    return df