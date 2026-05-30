# ================================================
# Flight Price Manipulation Detector
# File 4: Machine Learning Model
# Author: [Your Name]
# ================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import os

os.makedirs("graphs", exist_ok=True)


def encode_features(df):
    """Encode categorical columns for ML"""
    ml_df = df.copy()
    le    = LabelEncoder()
    cat_cols = ['airline', 'source_city', 'destination_city',
                'departure_time', 'arrival_time', 'stops', 'class']
    for col in cat_cols:
        ml_df[col] = le.fit_transform(ml_df[col])
    return ml_df


def train_model(df):
    """Train Random Forest to predict flight prices"""

    print("=" * 55)
    print("ML MODEL — Flight Price Prediction")
    print("=" * 55)

    ml_df = encode_features(df)

    features = [
        'airline', 'source_city', 'destination_city',
        'departure_time', 'arrival_time', 'stops',
        'class', 'duration', 'days_left'
    ]
    target = 'price'

    X = ml_df[features]
    y = ml_df[target]

    # 80/20 train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    print(f"\nTraining size : {X_train.shape[0]} rows")
    print(f"Testing size  : {X_test.shape[0]} rows")
    print("\nTraining Random Forest model... (may take 1-2 mins)")

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    r2  = r2_score(y_test, predictions)

    print(f"\nModel Results:")
    print(f"  Mean Absolute Error : Rs {mae:,.0f}")
    print(f"  R² Score            : {r2:.2f}")
    print(f"  Accuracy            : {r2*100:.1f}%")

    # --- GRAPH 6: Feature Importance ---
    feat_imp = pd.DataFrame({
        'Feature':    features,
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=False)

    plt.figure(figsize=(10, 5))
    sns.barplot(data=feat_imp, x='Importance', y='Feature',
                hue='Feature', palette='viridis', legend=False)
    plt.title('What Factors Affect Flight Price Most?', fontsize=14)
    plt.tight_layout()
    plt.savefig('graphs/graph6_feature_importance.png', dpi=150)
    plt.close()
    print("\nGraph 6 saved: Feature Importance")

    print("\nTop 3 price factors:")
    print(feat_imp.head(3).to_string(index=False))

    # --- GRAPH 7: Actual vs Predicted ---
    plt.figure(figsize=(12, 5))
    plt.plot(y_test.values[:80], label='Actual Price',
             color='blue', linewidth=2)
    plt.plot(predictions[:80],  label='Predicted Price',
             color='red', linewidth=2, linestyle='--')
    plt.title('Actual vs Predicted Flight Price', fontsize=14)
    plt.xlabel('Data Points')
    plt.ylabel('Price (Rs)')
    plt.legend()
    plt.tight_layout()
    plt.savefig('graphs/graph7_actual_vs_predicted.png', dpi=150)
    plt.close()
    print("Graph 7 saved: Actual vs Predicted")

    print("\n✅ ML Model complete!")
    return model


if __name__ == "__main__":
    df = pd.read_csv("data/Clean_Dataset.csv")
    df.drop(columns=['Unnamed: 0'], inplace=True)
    train_model(df)
