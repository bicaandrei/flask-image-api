from flask import Blueprint, request, jsonify
from services.imageService import save_image
from services.imageTaggingService import get_image_tags

image_tagging_controller_blueprint = Blueprint('image', __name__)

@image_tagging_controller_blueprint.route('/images/', methods =["POST"])
def tag_image():

    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image']

    try:
        save_image(image)
        tags = get_image_tags(image.filename)
        if tags:
            return jsonify({"message": "Image tagged successfully", "tags": list(tags)}), 200 
        else:
            return jsonify({"error": "Image could not be tagged!" }), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
