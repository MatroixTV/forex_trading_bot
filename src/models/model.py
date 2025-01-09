import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


class TradingModel:
    def __init__(self, model=None):
        self.model = model or RandomForestClassifier()  # Default model can be RandomForest

    def preprocess_data(self, df):
        # Preprocess the data (scale and prepare features)
        features = df[['High', 'Low', 'Close', 'RSI']]  # Add all necessary columns here
        scaler = StandardScaler()
        features_scaled = scaler.fit_transform(features)
        labels = df['Buy_Signal']  # Target labels

        return train_test_split(features_scaled, labels, test_size=0.2, random_state=42)

    def train_model(self, df):
        X_train, X_test, y_train, y_test = self.preprocess_data(df)

        # Train model
        self.model.fit(X_train, y_train)

        # Test the model
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        print(f"Model trained with accuracy: {accuracy}")

    def predict(self, df):
        # Use trained model to predict signals
        features = df[['High', 'Low', 'Close', 'RSI']]  # Add all necessary columns here
        return self.model.predict(features)
