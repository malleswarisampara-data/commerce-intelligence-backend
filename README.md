# Commerce Intelligence — Render Backend

This is a starter Flask API for the Netlify Commerce Intelligence frontend.

## API endpoints
- `GET /` — health check
- `GET /api/overview` — sales summary and monthly sales
- `GET /api/sales-forecast?periods=3` — simple baseline sales forecast (1–12 months)
- `GET /api/customers` — customer counts and top customers
- `GET /api/data-warehouse` — dataset columns, row count, and first 10 rows

## Deploy on Render
1. Upload the contents of this folder to the root of a GitHub repository.
2. In Render, choose **New + → Web Service** and connect that repository.
3. Render can read `render.yaml`; if configuring manually use:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
4. After deployment, test `/`, then each `/api/...` endpoint.
5. Put your actual Render URL into your Netlify frontend JavaScript as the API base URL.

## Important
- The included CSV is illustrative sample data, not real business data.
- Replace `data/sales_data.csv` with your project dataset or adapt the column names in `analytics/`.
- This starter backend does not automatically change the Netlify frontend. The frontend JavaScript must call these API endpoints and render their returned data.
- CORS currently permits `https://unique-gecko-b33533.netlify.app`. If you use another Netlify domain, update the allowed origin in `app.py`.
- The forecasting endpoint uses a simple average of the latest three monthly totals; it is a baseline, not an advanced prediction model.
- A bundled CSV is read-only deployment data. For online uploads or persistent user data, add a hosted database/storage solution.
