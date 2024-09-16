import os

IMAGE_UPLOAD_FOLDER = '../src/images/untagged'

def save_image(image):
    
    if not os.path.exists(IMAGE_UPLOAD_FOLDER):
        os.makedirs(IMAGE_UPLOAD_FOLDER)

    filename = image.filename
    image_path = os.path.join(IMAGE_UPLOAD_FOLDER, filename)

    if os.path.exists(image_path):
        return

    filename = image.filename
    image_path = os.path.join(IMAGE_UPLOAD_FOLDER, filename)
    image.save(image_path)