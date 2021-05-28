from imageai.Detection import ObjectDetection


# checks what the object in the image is and classifies it into categories
def detection(image):
    # locates the objects in the image
    detector = ObjectDetection() # instance of the ObjectDetection class that allows to start detecting objects in image
    detector.setModelTypeAsYOLOv3() # sets the model type of the object detection instance to the YOLOv3 model
    detector.setModelPath('yolo.h5') # accepts a string which must be the path to the model file
                                     # and corresponds to the model type for your object detection instance
    detector.loadModel() # loads the model from the path into the object detection instance

    # performs object detection task after the model as loaded
    # input_image is the path to image file which the user wants to detect
    # output_image_path is the file path to which the detected image will be saved
    # minimum_percentage_probability is used to determine the integrity of the detection results
        # lowering the value shows more objects while increasing the value ensures objects with the highest accuracy are detected
        # the default value is 50
    detections = detector.detectObjectsFromImage(input_image= image, output_image_path= "imagenew.jpg", minimum_percentage_probability= 50)
    print(detections)

    # classifies the object in the image into some category
    # classifies into "person"
    p = 0
    for detect in detections:
        if detect['name'] == 'person':
            p = p + 1
    if p > 0:
        print("The category is: person")
        name = 'person'
    else:
        # classifies into "vehicle"
        v = 0
        vehicles = ['bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'skateboard']
        for detect in detections:
            for vehicle in vehicles:
                if detect['name'] == vehicle:
                    v = v + 1
        if v > 0:
            print("The category is: vehicles")
            name = 'vehicle'
        else:
            # classifies into "animal"
            a = 0
            animals = ['bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe']
            for detect in detections:
                for animal in animals:
                    if detect['name'] == animal:
                        a = a + 1
            if a > 0:
                print("The category is: animals")
                name = 'animal'
            else:
                # classifies into "food"
                f = 0
                food = ['banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake']
                for detect in detections:
                    for foods in food:
                        if detect['name'] == foods:
                            f = f + 1
                if f > 0:
                    print("The category is: food")
                    name = 'food'
                else:
                    # if the object isn't a person, a vehicle, an animal or food, it is a "thing"
                    name = 'thing'

    return name
