from flask import Flask, jsonify
from flask_cors import CORS
from routes import register_routes

app = Flask(__name__)

# Allow requests from the deployed Netlify frontend.
CORS(app, resources={r"/api/*": {"origins": [
    "https://unique-gecko-b33533.netlify.app"
]}})

register_routes(app)

@app.get("/")
def health():
    return jsonify({
        "status": "success",
        "message": "Commerce Intelligence backend is running."
    })

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
