import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model(df):
    model = LinearRegression()
    X = df[['month']]
    y = df['sales']
    model.fit(X, y)
    return model

def predict_next_month(model, last_month):
    next_month = [[last_month + 1]]
    return model.predict(next_month)[0]
