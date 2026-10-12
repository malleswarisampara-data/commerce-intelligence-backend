from flask import Blueprint, jsonify, request
from analytics.sales_analysis import load_sales_data
from analytics.forecasting import forecast_sales

forecast_bp = Blueprint("forecast", __name__)

@forecast_bp.get("/api/sales-forecast")
def sales_forecast():
    try:
        periods = request.args.get("periods", default=3, type=int)
        periods = max(1, min(periods, 12))
        result = forecast_sales(load_sales_data(), periods=periods)
        return jsonify({"status": "success", "forecast": result})
    except Exception as exc:
        return jsonify({"status": "error", "message": str(exc)}), 500
