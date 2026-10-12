from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "sales_data.csv"

def load_sales_data():
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at {DATA_PATH}. Add data/sales_data.csv to the project."
        )
    df = pd.read_csv(DATA_PATH)
    required = {"Order_ID", "Customer_ID", "Order_Date", "Sales"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(
            "Dataset is missing required columns: " + ", ".join(sorted(missing))
        )
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
    df = df.dropna(subset=["Order_Date", "Sales"])
    return df

def analyze_sales(df):
    sales = pd.to_numeric(df["Sales"], errors="coerce").dropna()
    monthly = (
        df.dropna(subset=["Order_Date", "Sales"])
          .assign(Month=lambda x: x["Order_Date"].dt.to_period("M").astype(str))
          .groupby("Month", as_index=False)["Sales"].sum()
          .to_dict(orient="records")
    )
    return {
        "total_sales": round(float(sales.sum()), 2) if not sales.empty else 0,
        "average_order_value": round(float(sales.mean()), 2) if not sales.empty else 0,
        "minimum_sale": round(float(sales.min()), 2) if not sales.empty else 0,
        "maximum_sale": round(float(sales.max()), 2) if not sales.empty else 0,
        "total_orders": int(df["Order_ID"].nunique()),
        "total_customers": int(df["Customer_ID"].nunique()),
        "monthly_sales": monthly
    }
