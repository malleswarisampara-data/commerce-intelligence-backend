from .overview import overview_bp
from .customers import customers_bp
from .sales_forecast import sales_forecast_bp
from .data_warehouse import data_warehouse_bp


def register_routes(app):
    app.register_blueprint(overview_bp)
    app.register_blueprint(customers_bp)
    app.register_blueprint(sales_forecast_bp)
    app.register_blueprint(data_warehouse_bp)
