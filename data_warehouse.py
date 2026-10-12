from flask import Blueprint, jsonify
from analytics.sales_analysis import load_sales_data

warehouse_bp = Blueprint("warehouse", __name__)

@warehouse_bp.get("/api/data-warehouse")
def data_warehouse():
    try:
        df = load_sales_data()
        return jsonify({
            "status": "success",
            "rows": int(len(df)),
            "columns": list(df.columns),
            "preview": df.head(10).where(df.notna(), None).to_dict(orient="records")
        })
    except Exception as exc:
        return jsonify({"status": "error", "message": str(exc)}), 500
