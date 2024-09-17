from flask import Flask
from flask_cors import CORS
from controllers.imageTaggingController import image_tagging_controller_blueprint

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:5173"], supports_credentials=True)

    app.register_blueprint(image_tagging_controller_blueprint)

    return app
