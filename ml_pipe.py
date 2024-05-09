import pickle
from catboost import CatBoostClassifier
with open("catboost_model.pkl", "rb") as f:
    loaded_model = pickle.load(f)

def predict(loan_data):
    prediction = loaded_model.predict(loan_data)
    return prediction