from flask import Blueprint, jsonify
from analytics.sales_analysis import load_sales_data
from analytics.customer_analysis import analyze_customers

customers_bp = Blueprint("customers", __name__)

@customers_bp.get("/api/customers")
def customers():
    try:
        df = load_sales_data()
        return jsonify({"status": "success", **analyze_customers(df)})
    except Exception as exc:
        return jsonify({"status": "error", "message": str(exc)}), 500
