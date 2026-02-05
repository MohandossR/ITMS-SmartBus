from flask import request, jsonify

# In-memory AI status
ai_status = {}

def register_ai_routes(app):

    @app.route("/ai/status", methods=["POST"])
    def receive_ai_status():
        data = request.get_json()

        ai_status.update({
            "driver_status": data.get("driver_status"),
            "attention_score": data.get("attention_score"),
            "passenger_count": data.get("passenger_count"),
            "seat_vacancy": data.get("seat_vacancy"),
            "fire_detected": data.get("fire_detected"),
            "dangerous_driving": data.get("dangerous_driving"),
            "decisions": data.get("decisions", [])
        })

        return jsonify({
            "status": "AI status updated",
            "ai_status": ai_status
        })

    @app.route("/ai/status", methods=["GET"])
    def get_ai_status():
        return jsonify(ai_status)
