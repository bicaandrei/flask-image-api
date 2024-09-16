from flask import Flask
from controllers.imageTaggingController import image_tagging_controller_blueprint

def create_app():
    app = Flask(__name__)

    app.register_blueprint(image_tagging_controller_blueprint)

    return app
