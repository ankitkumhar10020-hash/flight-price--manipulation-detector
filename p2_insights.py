# ================================================
# Flight Price Manipulation Detector
# File 3: Key Insights & Findings
# Author: [Your Name]
# ================================================

import pandas as pd


def generate_insights(df):
    """Print all key insights from the analysis"""

    print("=" * 55)
    print("KEY INSIGHTS — Flight Price Manipulation Detector")
    print("=" * 55)

    # insight 1 — last minute price spike
    early       = df[df['days_left'] >= 30]['price'].mean()
    last_minute = df[df['days_left'] <= 7]['price'].mean()
    spike       = ((last_minute - early) / early) * 100
    print(f"\nInsight 1: Last Minute Price Spike")
    print(f"   30+ days before  -> Avg Price: Rs {early:,.0f}")
    print(f"   7 days before    -> Avg Price: Rs {last_minute:,.0f}")
    print(f"   Price increases by {spike:.1f}% near departure!")

    # insight 2 — cheapest vs expensive airline
    eco_prices  = df[df['class'] == 'Economy'].groupby('airline')['price'].mean()
    cheapest    = eco_prices.idxmin()
    expensive   = eco_prices.idxmax()
    print(f"\nInsight 2: Airline Price Comparison (Economy)")
    print(f"   Cheapest airline    = {cheapest} (Rs {eco_prices[cheapest]:,.0f})")
    print(f"   Most expensive      = {expensive} (Rs {eco_prices[expensive]:,.0f})")

    # insight 3 — best departure time
    time_prices    = df.groupby('departure_time')['price'].mean()
    cheapest_time  = time_prices.idxmin()
    expensive_time = time_prices.idxmax()
    print(f"\nInsight 3: Best Time to Book")
    print(f"   Cheapest departure time  = {cheapest_time} (Rs {time_prices[cheapest_time]:,.0f})")
    print(f"   Expensive departure time = {expensive_time} (Rs {time_prices[expensive_time]:,.0f})")

    # insight 4 — stops vs price
    print(f"\nInsight 4: How Stops Affect Price")
    print(df.groupby('stops')['price'].mean().round(0).to_string())

    # insight 5 — business vs economy premium
    eco = df[df['class'] == 'Economy']['price'].mean()
    biz = df[df['class'] == 'Business']['price'].mean()
    premium = ((biz - eco) / eco) * 100
    print(f"\nInsight 5: Business Class Premium")
    print(f"   Economy avg  -> Rs {eco:,.0f}")
    print(f"   Business avg -> Rs {biz:,.0f}")
    print(f"   Business costs {premium:.1f}% more than Economy!")

    # insight 6 — best route
    route_price = df.groupby(['source_city', 'destination_city'])['price']\
                    .mean().reset_index()
    cheapest_route = route_price.loc[route_price['price'].idxmin()]
    print(f"\nInsight 6: Cheapest Route")
    print(f"   {cheapest_route['source_city']} -> "
          f"{cheapest_route['destination_city']} "
          f"(Rs {cheapest_route['price']:,.0f} avg)")

    print("\n✅ Insights complete!")


if __name__ == "__main__":
    df = pd.read_csv("data/Clean_Dataset.csv")
    df.drop(columns=['Unnamed: 0'], inplace=True)
    generate_insights(df)
