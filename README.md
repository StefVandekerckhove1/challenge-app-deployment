# challenge-app-deployment

- **Repository**: `challenge-app-deployment`
- **Type of Challenge**: `Learning`
- **Duration**: `5 days`
- **Deadline**: `18/12/2024 17:00`
- **Presentation**: `20/12/2024 10:30`
- **Team Challenge**: Solo

## Description
Welcome on the ImmoEliza price predictor app for real estate!

This app uses Streamlit as user platform for price price prediction of belgian real estate.
The prediction is based on the usage of a xgboost regression model trained with data from 6000 properties on ImmoWeb.

## Installation instructions
This app requires the installation of following packages:
- pandas
- numpy
- joblib
- streamlit
- typing

## Usage guide
To use the app you need to run the app.py file available in the repository.
This will lead you to the streamlit platform on which you can enter following features:
- Municipality
- Number of bedrooms
- Livable space (m²)
- Garden area (m²)
- Terrace area (m²)
- Fully Equipped Kitchen? (Yes/No)
- House or Appartment?

After entering all features, hit the predict button and your price will appear!

## Visuals

![image](https://github.com/user-attachments/assets/829b3b1e-3e20-47db-9a8b-5dda5db661c2)

![image](https://github.com/user-attachments/assets/11fcfc7d-9b14-4ae0-8e3a-8664661802a8)

## Evaluation Criteria

| Criteria       | Indicator                                                | Yes/No |
| -------------- | -------------------------------------------------------- | ------ |
| 1. Is complete | Your app works.                                          | [ ]    |
|                | README is polished and informative.                     | [ ]    |
|                | Your model is trained and produces predictions.          | [ ]    |
| 2. Is good     | Repository is clean and organized.                       | [ ]    |
|                | Typing and docstrings are used throughout.               | [ ]    |
|                | The app is clean, user-friendly, and visually appealing. | [ ]    |
|                | Code adheres to OOP principles.                          | [ ]    |

## Resources

- [Streamlit Documentation](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app)
- [Deploying ML Models with Streamlit](https://towardsdatascience.com/deploying-ml-models-using-streamlit-5d6212453bdd)
