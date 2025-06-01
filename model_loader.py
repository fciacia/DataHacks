import joblib
import pandas as pd
import streamlit as st

class ModelLoader:
    def __init__(self):
        self.fsi_model = None
        self.risk_model = None
        self.yield_model = None
        
    def load_models(self):
        """Load all trained models"""
        try:
            self.fsi_model = joblib.load('models/fsi_model.joblib')
            self.risk_model = joblib.load('models/risk_model.joblib')
            self.yield_model = joblib.load('models/yield_model.joblib')
            return True
        except Exception as e:
            st.error(f"Error loading models: {str(e)}")
            return False
            
    def predict_fsi(self, data):
        """Make Food Security Index predictions"""
        if self.fsi_model is not None:
            try:
                return self.fsi_model.predict(data)
            except Exception as e:
                st.error(f"Error making FSI prediction: {str(e)}")
        return None
        
    def predict_risk(self, data):
        """Make Hunger Risk predictions"""
        if self.risk_model is not None:
            try:
                return self.risk_model.predict(data)
            except Exception as e:
                st.error(f"Error making risk prediction: {str(e)}")
        return None
        
    def predict_yield(self, data):
        """Make Crop Yield predictions"""
        if self.yield_model is not None:
            try:
                return self.yield_model.predict(data)
            except Exception as e:
                st.error(f"Error making yield prediction: {str(e)}")
        return None 