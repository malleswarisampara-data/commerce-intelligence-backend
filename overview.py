from flask import Blueprint, jsonify
from analytics.sales_analysis import load_sales_data, analyze_sales

overview_bp = Blueprint("overview", __name__)

@overview_bp.get("/api/overview")
def overview():
    try:
        df = load_sales_data()
        return jsonify({"status": "success", **analyze_sales(df)})
    except Exception as exc:
        return jsonify({"status": "error", "message": str(exc)}), 500
