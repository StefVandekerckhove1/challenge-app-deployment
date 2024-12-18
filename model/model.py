# Importing functions from modules
from sklearn.model_selection import train_test_split
import xgboost as xgb
import numpy as np
import pandas as pd
from joblib import dump


# 1.1 preprocess data and load into pandas dataframe
df=pd.read_csv("C:\\Users\\vande\\challenge-app-deployment\\preprocessing\\data\\real_estate_belgium.csv")

# 2.1 Keep column features which have high correlation coefficients
df = df[["Municipality", "Price", "Living_Area", "Number_of_Rooms", "Fully_Equipped_Kitchen", "Terrace_Area","Garden_Area","Type_of_Property"]]

# 3.1 Extract feature and target arrays
X, y = df.drop('Price', axis=1), df[['Price']]

# 3.2 Extract text features
cats = X.select_dtypes(exclude=np.number).columns.tolist()

# 3.3 Convert to Pandas category
for col in cats:
   X[col] = X[col].astype('category')
X.dtypes

# 3.4 split dataset into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=1)

# 5.1 Create XGBoost regression matrices
dtrain_reg = xgb.DMatrix(X_train, y_train, enable_categorical=True)
dtest_reg = xgb.DMatrix(X_test, y_test, enable_categorical=True)

# 6.3 Validation Sets During Training
params = {"objective": "reg:squarederror", "tree_method": "hist", "device":"cuda"}
n = 10000

evals = [(dtrain_reg, "train"), (dtest_reg, "validation")]

model = xgb.train(
   params=params,
   dtrain=dtrain_reg,
   num_boost_round=n,
   evals=evals,
   verbose_eval=10,
   # Activate early stopping
   early_stopping_rounds = 50

)
dump(model, 'real_estate_model.joblib')


