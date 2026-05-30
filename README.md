# Flight Price Manipulation Detector
### Exposing How Indian Airlines Secretly Spike Prices on 300,000+ Flight Tickets

---

## Project Overview

Ever booked a flight and noticed the price jumped by thousands overnight?
It's not your imagination — it's called **dynamic pricing**, and this project
proves it with real data.

I analyzed **300,153 actual flight ticket records** across 6 major Indian airlines
including IndiGo, Vistara, Air India, SpiceJet, AirAsia and GO FIRST — covering
routes between 6 major Indian cities.

The analysis exposes exactly **when prices spike, which airlines manipulate the most,
what time of day is cheapest to fly**, and builds a **Machine Learning model that
predicts flight prices with 98% accuracy** — so you never overpay again.

---

## Key Findings That Will Shock You

| Finding | Result |
| Price spike in last 7 days | **+37.2% more expensive!** |
| Cheapest airline (Economy) | **AirAsia** |
| Most expensive airline (Economy) | **Vistara** |
| Cheapest time to book | **Late Night flights** |
| Most expensive time | **Night flights** |
| Direct flights vs connecting | **Direct flights are cheaper!** |
| Business vs Economy gap | **Business costs 699% more!** |
| ML model accuracy | **R² = 0.98 (98% accurate)** |

---

## Dataset

| Detail | Info |
| Source | Kaggle — Flight Price Prediction |
| Total Tickets Analyzed | **300,153 flight records** |
| Airlines | Vistara, Air India, Indigo, GO FIRST, AirAsia, SpiceJet |
| Cities | Delhi, Mumbai, Bangalore, Kolkata, Hyderabad, Chennai |
| Features | Airline, Route, Departure Time, Stops, Class, Duration, Days Left, Price |
| Missing Values | Zero — clean dataset |

---

## Tech Stack

| Tool | Usage |
| Python | Core programming |
| Pandas | Data manipulation (300k+ rows) |
| Matplotlib & Seaborn | 7 visualizations |
| Scikit-learn | Random Forest ML model |
| LabelEncoder | Categorical feature encoding |

---

## Project Structure

```
flight-price-manipulation-detector/
│
├── main.py            ← run this to execute full pipeline
├── data_loading.py    ← load and explore 300k records
├── eda_analysis.py    ← 5 EDA graphs and visualizations
├── insights.py        ← 6 key findings with statistics
├── ml_model.py        ← Random Forest model (R²=0.98)
├── data/
│   └── Clean_Dataset.csv
├── graphs/            ← all 7 generated visualizations
└── README.md
```

---

## Visualizations Generated

1. **Price vs Days Left** — scatter showing economy vs business behavior
2. **Average Price by Airline** — who charges most across 300k tickets
3. **Price Spike Near Departure** — the manipulation proof graph 🚨
4. **Economy vs Business by Airline** — class price comparison
5. **Cheapest Time to Fly** — best departure slot analysis
6. **Feature Importance** — what factors drive price most
7. **Actual vs Predicted Price** — ML model accuracy graph

---

## Machine Learning Model

- **Algorithm:** Random Forest Regressor
- **Dataset size:** 300,153 records
- **Training set:** 240,122 records (80%)
- **Testing set:** 60,031 records (20%)
- **R² Score:** 0.98 — predicts 98% of price variation
- **Mean Absolute Error:** Rs 1,091 only!
- **Top 3 price factors:** Class > Duration > Days Left

---

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/flight-price-manipulation-detector

# 2. Install dependencies
pip install pandas matplotlib seaborn scikit-learn

# 3. Add dataset to data/ folder
# Download Clean_Dataset.csv from Kaggle

# 4. Run full pipeline
python main.py
```

---

## Money Saving Tips — Backed by Data

- **Book 30+ days in advance** — saves up to 37% vs last minute booking
- **Choose Late Night flights** — consistently cheapest across all airlines
- **Fly AirAsia for budget travel** — lowest average Economy price
- **Direct flights save money** — surprisingly cheaper than connecting flights
- **Avoid Night departure slots** — most expensive time across all airlines

---

## Connect

Feel free to reach out for any questions or collaboration!

