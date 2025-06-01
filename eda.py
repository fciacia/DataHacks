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

# Set style for better visualizations
plt.style.use('seaborn')
sns.set_palette("husl")

# Load data once and use it throughout the script
try:
    df = pd.read_csv('hunger.csv')
    print("Data loaded successfully!")
    print("Number of rows:", len(df))
    print("Number of columns:", len(df.columns))
    print("\nColumns in the dataset:")
    print(df.columns.tolist())
except FileNotFoundError:
    print("Error: 'hunger.csv' file not found. Please make sure the file is in the same directory as this script.")
    exit()
except Exception as e:
    print(f"Error loading data: {str(e)}")
    exit()

# === Feature lists with exact names ===
# Make sure these column names exactly match your dataset
availability_features = ['Production_tonnes_sum', 'Yield_kg_per_ha_mean']
access_features = [
    'Prevalence of undernourishment (percent) (3-year average)',
    'Percent of arable land equipped for irrigation (percent) (3-year average)'
]
utilization_features = [
    'Average protein supply (g/cap/day) (3-year average)',
    'Average dietary energy supply adequacy (percent) (3-year average)'
]
stability_features = ['Temperature Change (°C)']

targets = ['Crop_Yield_Prediction', 'Food_Security_Index', 'Hunger_Risk_Score']

# Verify all features exist in the dataset
all_features = availability_features + access_features + utilization_features + stability_features + targets
missing_features = [col for col in all_features if col not in df.columns]
if missing_features:
    print("\nWarning: The following features are not in your dataset:")
    print(missing_features)
    print("\nAvailable columns in your dataset:")
    print(df.columns.tolist())
    exit()

# Create a binary flag for undernourishment above median
df['High_Undernourishment'] = df['Prevalence of undernourishment (percent) (3-year average)'].apply(
    lambda x: 'Yes' if x > df['Prevalence of undernourishment (percent) (3-year average)'].median() else 'No'
)

# Categorical features excluding Area and Year for countplots
categorical_features = ['Year', 'High_Undernourishment']

# --- 1. Scatter + Regression plots per pillar ---
def scatter_regression_plots(df, features, target, pillar_name):
    print(f"\nScatter plots for {target} vs {pillar_name} features:")
    for feature in features:
        plt.figure(figsize=(7,5))
        sns.regplot(data=df, x=feature, y=target, scatter_kws={'alpha':0.5})
        plt.title(f"{target} vs {feature} ({pillar_name})")
        plt.xlabel(feature)
        plt.ylabel(target)
        plt.show()

scatter_regression_plots(df, availability_features, 'Crop_Yield_Prediction', 'Availability')
scatter_regression_plots(df, access_features, 'Food_Security_Index', 'Access')
scatter_regression_plots(df, utilization_features, 'Hunger_Risk_Score', 'Utilization')
scatter_regression_plots(df, stability_features, 'Hunger_Risk_Score', 'Stability')

# --- 2. Multiple Linear Regression and evaluation ---
def multi_linear_regression(df, feature_cols, target_col):
    df_clean = df[feature_cols + [target_col]].dropna()
    X = df_clean[feature_cols].values
    y = df_clean[target_col].values

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    mse = mean_squared_error(y, y_pred)
    print(f"Linear Regression for predicting {target_col} using {feature_cols}")
    print(f"Coefficients: {model.coef_}")
    print(f"Intercept: {model.intercept_}")
    print(f"Mean Squared Error: {mse:.4f}")

    # Predicted vs Actual plot
    plt.figure(figsize=(7,5))
    plt.scatter(y, y_pred, alpha=0.6)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
    plt.xlabel("Actual " + target_col)
    plt.ylabel("Predicted " + target_col)
    plt.title(f"Predicted vs Actual for {target_col}")
    plt.show()

    # Residual plot
    residuals = y - y_pred
    plt.figure(figsize=(7,5))
    plt.scatter(y_pred, residuals, alpha=0.6)
    plt.axhline(0, color='r', linestyle='--')
    plt.xlabel("Predicted " + target_col)
    plt.ylabel("Residuals")
    plt.title(f"Residuals Plot for {target_col}")
    plt.show()

# Regressions per pillar features
multi_linear_regression(df, availability_features, 'Crop_Yield_Prediction')
multi_linear_regression(df, access_features, 'Food_Security_Index')
multi_linear_regression(df, utilization_features, 'Hunger_Risk_Score')

# --- 3. Combined regression using all pillar features ---
all_features = availability_features + access_features + utilization_features + stability_features
print("\n--- Multiple Linear Regression using all pillar features combined ---")
for target in targets:
    multi_linear_regression(df, all_features, target)

# --- 4. Pairwise regression plots between targets ---
print("\n--- Pairwise regression plots between targets ---")
target_pairs = [
    ('Crop_Yield_Prediction', 'Food_Security_Index'),
    ('Food_Security_Index', 'Hunger_Risk_Score'),
    ('Crop_Yield_Prediction', 'Hunger_Risk_Score')
]

for x_target, y_target in target_pairs:
    plt.figure(figsize=(7,5))
    sns.regplot(data=df, x=x_target, y=y_target, scatter_kws={'alpha':0.5})
    plt.title(f'{y_target} vs {x_target}')
    plt.xlabel(x_target)
    plt.ylabel(y_target)
    plt.show()

# --- 5a. Countplot for categorical features (only High_Undernourishment) ---
for cat in ['High_Undernourishment']:
    plt.figure(figsize=(10,6))
    sns.countplot(data=df, x=cat)
    plt.title(f'Distribution of {cat}')
    plt.xlabel(cat)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# --- 5b. Grouped mean lineplots for targets by categorical features ---
for cat in categorical_features:
    for target in targets:
        grouped = df.groupby(cat)[target].mean().reset_index()
        plt.figure(figsize=(10,6))
        sns.lineplot(data=grouped, x=cat, y=target, marker='o')
        plt.title(f'Average {target} by {cat}')
        plt.xlabel(cat)
        plt.ylabel(f'Average {target}')
        plt.xticks(rotation=45)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

# --- 5c. Stacked barplots of binned Hunger Risk Score by Year ---
df['Hunger_Risk_Level'] = pd.qcut(df['Hunger_Risk_Score'], q=3, labels=['Low', 'Medium', 'High'])

pivot_df = df.pivot_table(index='Year', columns='Hunger_Risk_Level', aggfunc='size', fill_value=0)

pivot_df.plot(kind='bar', stacked=True, figsize=(12,7), colormap='viridis')
plt.title('Stacked Barplot of Hunger Risk Level by Year')
plt.ylabel('Count')
plt.xlabel('Year')
plt.xticks(rotation=45)
plt.legend(title='Hunger Risk Level')
plt.tight_layout()
plt.show()

# --- 6. Dataset Info Summary ---
print("Dataset Info:")
print(df.info())

# --- 7. Correlation Heatmap (last) ---
plt.figure(figsize=(12,10))
sns.heatmap(df[availability_features + access_features + utilization_features + stability_features + targets].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap of Features and Targets")
plt.show()

"""# Machine Learning"""

# Fill missing numeric features with median
for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:
        median_val = df[col].median()
        df[col].fillna(median_val, inplace=True)

# Create categorical Hunger Risk by binning Hunger_Risk_Score
bins = [0, 4, 7, 10]  # adjust thresholds as needed
labels = ['Low', 'Medium', 'High']
df['Hunger_Risk_Category'] = pd.cut(df['Hunger_Risk_Score'], bins=bins, labels=labels, include_lowest=True)

# Drop rows where category is NaN (due to missing Hunger_Risk_Score)
df = df.dropna(subset=['Hunger_Risk_Category'])

# Encode 'Area' (country)
le = LabelEncoder()
df['Area_enc'] = le.fit_transform(df['Area'])

# Prepare features and target
X = df.drop(columns=['Hunger_Risk_Score', 'Hunger_Risk_Category', 'Area'])
y = df['Hunger_Risk_Category']

# Fill missing in features (if any left)
for col in X.columns:
    if X[col].dtype in ['float64', 'int64']:
        X[col].fillna(X[col].median(), inplace=True)

# Split train/test (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
print("Classification Report:\n")
print(classification_report(y_test, y_pred))

# Function to predict Hunger Risk Category by country name
def predict_hunger_category(country_name):
    if country_name not in le.classes_:
        print(f"Country '{country_name}' not found in dataset.")
        return None

    country_code = le.transform([country_name])[0]
    country_data = df[df['Area'] == country_name]
    latest_year = country_data['Year'].max()
    latest_data = country_data[country_data['Year'] == latest_year]

    X_input = latest_data.drop(columns=['Hunger_Risk_Score', 'Hunger_Risk_Category', 'Area'])
    pred = clf.predict(X_input)
    # If multiple rows, take most common prediction
    from collections import Counter
    pred_mode = Counter(pred).most_common(1)[0][0]

    print(f"Predicted Hunger Risk Category for {country_name} in {latest_year}: {pred_mode}")
    return pred_mode

# Example usage
country_input = input("Enter country name to predict Hunger Risk Category: ")
predict_hunger_category(country_input)