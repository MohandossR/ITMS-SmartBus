from flask import Flask, jsonify
from routes import register_routes
from ai_status_routes import register_ai_routes


app = Flask(__name__)

register_routes(app)
register_ai_routes(app)

@app.route("/")
def home():
    return jsonify({
        "status": "Backend running",
        "project": "Intelligent Transportation Management System"
    })

if __name__ == "__main__":
    app.run(debug=True)
