import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import os

# Set basic style for visualizations
sns.set_theme()

# === Feature lists with exact names ===
availability_features = ['Production_tonnes_sum', 'Yield_kg_per_ha_mean', 'FSI_Availability']
access_features = [
    'Prevalence of undernourishment (percent) (3-year average)',
    'Percent of arable land equipped for irrigation (percent) (3-year average)',
    'FSI_Access'
]
utilization_features = [
    'Average protein supply (g/cap/day) (3-year average)',
    'Average dietary energy supply adequacy (percent) (3-year average)',
    'FSI_Utilization'
]
stability_features = ['Temperature Change (°C)', 'FSI_Stability']
targets = ['Crop_Yield_Prediction', 'Food_Security_Index', 'Hunger_Risk_Score']

# Load and prepare data
print("Loading data...")
df = pd.read_csv('hunger.csv')
print("Data loaded successfully!")

# Print basic statistics and information
print("\n=== Dataset Overview ===")
print(f"Number of records: {len(df)}")
print(f"Number of features: {len(df.columns)}")
print("\n=== Missing Values ===")
missing = df.isnull().sum()
print(missing[missing > 0])

# Calculate and print correlations with target variables
print("\n=== Key Correlations with Target Variables ===")
features = availability_features + access_features + utilization_features + stability_features
for target in targets:
    print(f"\nCorrelations with {target}:")
    correlations = df[features].corrwith(df[target]).sort_values(ascending=False)
    print(correlations.head())  # Top 5 positive correlations

# Print key statistics for model training
print("\n=== Feature Statistics for Model Training ===")
print("\nFeature Ranges (min, max):")
for feature in features:
    if df[feature].dtype in ['int64', 'float64']:
        print(f"{feature}: ({df[feature].min():.2f}, {df[feature].max():.2f})")

# Optional: Generate correlation heatmap (most important for feature selection)
plt.figure(figsize=(12,10))
sns.heatmap(df[features + targets].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap of Features and Targets")
plt.tight_layout()
plt.show()

print("\n=== Recommendations for Model Training ===")
# Identify highly correlated features
corr_matrix = df[features].corr()
high_corr_pairs = []
for i in range(len(features)):
    for j in range(i+1, len(features)):
        if abs(corr_matrix.iloc[i,j]) > 0.8:  # Threshold for high correlation
            high_corr_pairs.append((features[i], features[j], corr_matrix.iloc[i,j]))

if high_corr_pairs:
    print("\nHighly correlated features (potential for dimensionality reduction):")
    for f1, f2, corr in high_corr_pairs:
        print(f"{f1} & {f2}: {corr:.2f}")

# Check for skewness
print("\nFeatures with high skewness (might need transformation):")
for feature in features:
    if df[feature].dtype in ['int64', 'float64']:
        skew = df[feature].skew()
        if abs(skew) > 1:  # Threshold for high skewness
            print(f"{feature}: {skew:.2f}")

# Machine Learning Part
print("\n=== Preparing for Model Training ===")
# Create categorical Hunger Risk by binning Hunger_Risk_Score
bins = [0, 4, 7, 10]  # adjust thresholds as needed
labels = ['Low', 'Medium', 'High']
df['Hunger_Risk_Category'] = pd.cut(df['Hunger_Risk_Score'], bins=bins, labels=labels, include_lowest=True)

# Encode categorical variables
le = LabelEncoder()
df['Area_enc'] = le.fit_transform(df['Area'])

# Prepare features and target
X = df[features]
y = df['Hunger_Risk_Category']

# Handle missing values
for col in X.columns:
    if X[col].dtype in ['float64', 'int64']:
        X[col].fillna(X[col].median(), inplace=True)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nFeature matrix shape:", X.shape)
print("Number of classes:", len(y.unique()))
print("\nClass distribution:")
print(y.value_counts(normalize=True))