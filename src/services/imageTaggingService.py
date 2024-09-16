from imageai.Detection import ObjectDetection
import os

def get_image_tags(image_filename):
    execution_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath( os.path.join(execution_path , "../yolov3.pt"))
    detector.loadModel()
    image_name = image_filename.split('.')[0]
    image_type = image_filename.split('.')[1]
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "images/untagged/" + image_filename), output_image_path=os.path.join(execution_path , "images/tagged/" + image_name + "Tagged." + image_type), minimum_percentage_probability=30)
    tags_set = set()
    for eachObject in detections:
        tags_set.add(eachObject['name'])
    return tags_set
