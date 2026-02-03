from flask import Flask, jsonify
from routes import register_routes

app = Flask(__name__)

# Register all API routes
register_routes(app)

@app.route("/")
def home():
    return jsonify({
        "status": "Backend running",
        "project": "Intelligent Transportation Management System"
    })

if __name__ == "__main__":
    app.run(debug=True)
