from flask import request, jsonify
from models import Vehicle, vehicle_history
from alerts import check_speed_alert

def register_routes(app):

    @app.route("/vehicle", methods=["POST"])
    def receive_vehicle_data():
        data = request.get_json()

        vehicle = Vehicle(
            vehicle_id=data.get("vehicle_id", "UNKNOWN"),
            speed=data.get("speed", 0),
            latitude=data.get("latitude", 0.0),
            longitude=data.get("longitude", 0.0)
        )

        # Store vehicle data
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

    @app.route("/vehicles/view", methods=["GET"])
    def view_vehicles_html():
        html = """
        <html>
        <head>
            <title>Vehicle Records</title>
            <style>
                table { border-collapse: collapse; width: 100%; }
                th, td { border: 1px solid black; padding: 8px; text-align: center; }
                th { background-color: #4CAF50; color: white; }
                tr:nth-child(even) { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <h2>All Vehicle Records</h2>
            <table>
                <tr>
                    <th>Vehicle ID</th>
                    <th>Speed</th>
                    <th>Latitude</th>
                    <th>Longitude</th>
                    <th>Timestamp</th>
                </tr>
        """
        for v in vehicle_history:
            html += f"""
                <tr>
                    <td>{v.vehicle_id}</td>
                    <td>{v.speed}</td>
                    <td>{v.latitude}</td>
                    <td>{v.longitude}</td>
                    <td>{v.timestamp}</td>
                </tr>
            """
        html += """
            </table>
        </body>
        </html>
        """
        return html
