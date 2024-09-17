from imageai.Detection import ObjectDetection
import os

IMAGE_UNTAGGED_FOLDER = 'images/untagged/'
IMAGE_TAGGING_UPLOAD_FOLDER = 'images/tagged/'

def get_image_tags(image_filename):
    
    EXECUTION_PATH = os.getcwd()
    
    untagged_image_path = os.path.join(EXECUTION_PATH, IMAGE_UNTAGGED_FOLDER, image_filename)
    tagged_image_path = os.path.join(EXECUTION_PATH, IMAGE_TAGGING_UPLOAD_FOLDER, image_filename)
    
    if not os.path.exists(untagged_image_path):
        raise FileNotFoundError(f"Image path '{untagged_image_path}' is not found or a valid file.")
    
    if not os.path.exists(os.path.join(EXECUTION_PATH, IMAGE_TAGGING_UPLOAD_FOLDER)):
        os.makedirs(os.path.join(EXECUTION_PATH, IMAGE_TAGGING_UPLOAD_FOLDER))
    
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(EXECUTION_PATH, "yolov3.pt"))
    detector.loadModel()

    image_name = image_filename.split('.')[0]
    image_type = image_filename.split('.')[1]
    output_image_path = os.path.join(EXECUTION_PATH, IMAGE_TAGGING_UPLOAD_FOLDER, image_name + "Tagged." + image_type)
    
    detections = detector.detectObjectsFromImage(input_image=untagged_image_path, output_image_path=output_image_path, minimum_percentage_probability=30)
    
    tags_set = set()
    for eachObject in detections:
        tags_set.add(eachObject['name'])
    
    return tags_set
