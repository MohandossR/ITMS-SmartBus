<<<<<<< HEAD
from flask import Flask
from routes import register_routes

app = Flask(__name__)

# Register all routes defined in routes.py
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask
from routes import register_routes

app = Flask(__name__)

# Register all routes defined in routes.py
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> frontend-dev
