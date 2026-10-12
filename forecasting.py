import pandas as pd

def forecast_sales(df, periods=3):
    """Simple baseline forecast: average of the latest three available months."""
    data = df.dropna(subset=["Order_Date", "Sales"]).copy()
    if data.empty:
        return []

    monthly = data.set_index("Order_Date")["Sales"].resample("MS").sum()
    if monthly.empty:
        return []

    baseline = float(monthly.tail(3).mean())
    last_month = monthly.index.max()
    forecast = []
    for i in range(1, periods + 1):
        future_month = last_month + pd.DateOffset(months=i)
        forecast.append({
            "month": future_month.strftime("%Y-%m"),
            "forecast_sales": round(baseline, 2)
        })
    return forecast
