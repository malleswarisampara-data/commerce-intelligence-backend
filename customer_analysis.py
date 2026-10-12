def analyze_customers(df):
    customer_count = int(df["Customer_ID"].nunique())
    per_customer = (
        df.groupby("Customer_ID", as_index=False)
          .agg(orders=("Order_ID", "nunique"), total_spend=("Sales", "sum"))
          .sort_values("total_spend", ascending=False)
    )
    top_customers = [
        {
            "customer_id": str(row["Customer_ID"]),
            "orders": int(row["orders"]),
            "total_spend": round(float(row["total_spend"]), 2)
        }
        for _, row in per_customer.head(10).iterrows()
    ]
    return {
        "total_customers": customer_count,
        "repeat_customers": int((per_customer["orders"] > 1).sum()),
        "top_customers": top_customers
    }
