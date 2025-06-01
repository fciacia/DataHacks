import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, classification_report
import joblib

# Load the data
df = pd.read_csv('cleaned_data.csv')

class ModelTrainer:
    def __init__(self):
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.model = None
        self.scaler = StandardScaler()

    def prepare_data(self, target_column, feature_columns=None):
        """Prepare data for modeling"""
        if feature_columns is None:
            # Use all columns except target
            feature_columns = [col for col in df.columns if col != target_column]

        self.X = df[feature_columns]
        self.y = df[target_column]

        # Split the data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42
        )

        # Scale the features
        self.X_train = self.scaler.fit_transform(self.X_train)
        self.X_test = self.scaler.transform(self.X_test)

    def train_model(self, model):
        """Train the model"""
        self.model = model
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        """Evaluate the model"""
        # Make predictions
        y_pred = self.model.predict(self.X_test)

        # Calculate metrics
        mse = mean_squared_error(self.y_test, y_pred)
        r2 = r2_score(self.y_test, y_pred)

        print("Model Performance Metrics:")
        print(f"Mean Squared Error: {mse:.4f}")
        print(f"R² Score: {r2:.4f}")

        # Cross-validation
        cv_scores = cross_val_score(self.model, self.X, self.y, cv=5)
        print(f"\nCross-validation scores: {cv_scores}")
        print(f"Average CV score: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

    def save_model(self, filename='trained_model.joblib'):
        """Save the trained model"""
        joblib.dump(self.model, filename)
        print(f"Model saved as {filename}")

if __name__ == "__main__":
    # Example usage
    trainer = ModelTrainer()
    
    # Replace 'target_column' with your actual target variable name
    trainer.prepare_data(target_column='your_target_column')
    
    # Import and initialize your chosen model
    # Example with Random Forest:
    # from sklearn.ensemble import RandomForestRegressor
    # model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    # Train and evaluate the model
    # trainer.train_model(model)
    # trainer.evaluate_model()
    # trainer.save_model() 