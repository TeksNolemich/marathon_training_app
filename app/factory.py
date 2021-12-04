
from flask import Flask
from flask_cors import CORS
# blueprints
from app.errors.handlers import errors
from app.marathon_calendar import marathon_calendar

def create_app():
    app = Flask(__name__)

    app.register_blueprint(errors)
    app.register_blueprint(marathon_calendar)
    CORS(app)

    
    return app