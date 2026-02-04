from flask import request, jsonify, render_template
from models import Vehicle, vehicle_history
from alerts import check_speed_alert

# Store latest AI status (live)
latest_ai_status = {
    "driver_status": "UNKNOWN",
    "attention_score": 0,
    "passenger_count": 0,
    "seat_vacancy": 0,
    "fire_detected": False,
    "dangerous_driving": False,
    "decisions": []
}


def register_routes(app):

    # =====================================================
    # 🔹 HOME / DASHBOARD
    # =====================================================
    @app.route("/")
    @app.route("/dashboard")
    def dashboard():
        return render_template(
            "index.html",
            ai=latest_ai_status
        )

    # =====================================================
    # 🔹 DRIVER MONITOR PAGE
    # =====================================================
    @app.route("/driver")
    def driver_page():
        return render_template("driver.html", ai=latest_ai_status)

    # =====================================================
    # 🔹 PASSENGER MONITOR PAGE
    # =====================================================
    @app.route("/passenger")
    def passenger_page():
        return render_template("passenger.html", ai=latest_ai_status)

    # =====================================================
    # 🔹 VEHICLE DATA (API)
    # =====================================================
    @app.route("/vehicle", methods=["POST"])
    def receive_vehicle_data():
        data = request.get_json()

        vehicle = Vehicle(
            vehicle_id=data.get("vehicle_id", "UNKNOWN"),
            speed=data.get("speed", 0),
            latitude=data.get("latitude", 0.0),
            longitude=data.get("longitude", 0.0)
        )

        vehicle_history.append(vehicle)
        alert_result = check_speed_alert(vehicle)

        return jsonify({
            "vehicle": vehicle.to_dict(),
            "alert": alert_result,
            "total_records": len(vehicle_history)
        })

    @app.route("/vehicles", methods=["GET"])
    def get_all_vehicles():
        return jsonify({
            "count": len(vehicle_history),
            "vehicles": [v.to_dict() for v in vehicle_history]
        })

    # =====================================================
    # 🔹 VEHICLE HISTORY PAGE (HTML)
    # =====================================================
    @app.route("/vehicles/view")
    def view_vehicles_html():
        return render_template(
            "vehicle.html",
            vehicles=vehicle_history
        )

    # =====================================================
    # 🔹 AI STATUS API (FROM AI MODULES)
    # =====================================================
    @app.route("/ai/status", methods=["POST"])
    def receive_ai_status():
        global latest_ai_status
        latest_ai_status = request.get_json()
        return jsonify({
            "status": "AI status updated",
            "ai_status": latest_ai_status
        })
    

    @app.route("/ai/status", methods=["GET"])
    def get_ai_status():
        return jsonify(latest_ai_status)
    
    @app.route("/vehicle-monitor")
    def vehicle_monitor_page():
        return render_template("vehicle_monitor.html", ai=latest_ai_status)