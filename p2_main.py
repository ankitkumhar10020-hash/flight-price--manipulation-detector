# ================================================
# Flight Price Manipulation Detector
# main.py — Run complete project pipeline
# Author: [Your Name]
# ================================================

from p2_data_loading import load_data
from p2_eda_analysis import run_eda
from p2_insights import generate_insights
from p2_ml_model import train_model

if __name__ == "__main__":

    print("\n" + "=" * 55)
    print("   FLIGHT PRICE MANIPULATION DETECTOR")
    print("   Exposing Dynamic Pricing in Indian Airlines")
    print("=" * 55 + "\n")

    # step 1 — load data
    df = load_data()

    # step 2 — EDA
    run_eda(df)

    # step 3 — insights
    generate_insights(df)

    # step 4 — ML model
    train_model(df)

    print("\n" + "=" * 55)
    print("  PROJECT COMPLETE! Check graphs/ folder")
    print("=" * 55 + "\n")
