# ================================================
# Flight Price Manipulation Detector
# File 2: EDA & Visualizations
# Author: [Your Name]
# ================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (12, 5)
os.makedirs("graphs", exist_ok=True)


def run_eda(df):
    """Generate all EDA visualizations"""

    print("=" * 55)
    print("Running EDA & Generating Graphs...")
    print("=" * 55)

    # --- GRAPH 1: Price vs Days Left ---
    plt.figure()
    sample = df.sample(5000, random_state=42)
    sns.scatterplot(data=sample, x='days_left', y='price',
                    hue='class', alpha=0.5, palette='Set1')
    plt.title('Flight Price vs Days Left Before Departure', fontsize=14)
    plt.xlabel('Days Left to Departure')
    plt.ylabel('Price (Rs)')
    plt.tight_layout()
    plt.savefig('graphs/graph1_price_vs_days.png', dpi=150)
    plt.close()
    print("Graph 1 saved: Price vs Days Left")

    # --- GRAPH 2: Average Price by Airline ---
    plt.figure()
    airline_price = df.groupby('airline')['price'].mean()\
                      .sort_values(ascending=False).reset_index()
    sns.barplot(data=airline_price, x='price', y='airline',
                hue='airline', palette='viridis', legend=False)
    plt.title('Average Price by Airline', fontsize=14)
    plt.xlabel('Average Price (Rs)')
    plt.tight_layout()
    plt.savefig('graphs/graph2_airline_price.png', dpi=150)
    plt.close()
    print("Graph 2 saved: Airline Price Comparison")

    # --- GRAPH 3: Price Spike as Departure Approaches ---
    plt.figure()
    days_price = df.groupby('days_left')['price'].mean().reset_index()
    sns.lineplot(data=days_price, x='days_left', y='price',
                 color='red', linewidth=2)
    plt.title('How Price Changes as Departure Approaches', fontsize=14)
    plt.xlabel('Days Left')
    plt.ylabel('Average Price (Rs)')
    plt.gca().invert_xaxis()
    plt.tight_layout()
    plt.savefig('graphs/graph3_price_spike.png', dpi=150)
    plt.close()
    print("Graph 3 saved: Price Spike Near Departure")

    # --- GRAPH 4: Economy vs Business by Airline ---
    plt.figure()
    sns.barplot(data=df, x='airline', y='price',
                hue='class', palette='Set2')
    plt.title('Economy vs Business Price by Airline', fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('graphs/graph4_economy_vs_business.png', dpi=150)
    plt.close()
    print("Graph 4 saved: Economy vs Business")

    # --- GRAPH 5: Cheapest Departure Time ---
    plt.figure()
    time_price = df.groupby('departure_time')['price'].mean()\
                   .sort_values().reset_index()
    sns.barplot(data=time_price, x='departure_time', y='price',
                hue='departure_time', palette='coolwarm', legend=False)
    plt.title('Cheapest Time to Fly', fontsize=14)
    plt.xlabel('Departure Time')
    plt.ylabel('Average Price (Rs)')
    plt.tight_layout()
    plt.savefig('graphs/graph5_cheapest_time.png', dpi=150)
    plt.close()
    print("Graph 5 saved: Cheapest Departure Time")

    print("\n✅ All EDA graphs saved in graphs/ folder!")


if __name__ == "__main__":
    df = pd.read_csv("data/Clean_Dataset.csv")
    df.drop(columns=['Unnamed: 0'], inplace=True)
    run_eda(df)
