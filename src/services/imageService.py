import os

IMAGE_UPLOAD_FOLDER = 'images/untagged'

def save_image(image):
    
    EXECUTION_PATH = os.getcwd()
    
    untagged_image_path = os.path.join(EXECUTION_PATH, IMAGE_UPLOAD_FOLDER)
    
    if not os.path.exists(untagged_image_path):
        os.makedirs(untagged_image_path)
    
    filename = image.filename
    image_path = os.path.join(untagged_image_path, filename)
    
    if os.path.exists(image_path):
        return
    
    image.save(image_path)
