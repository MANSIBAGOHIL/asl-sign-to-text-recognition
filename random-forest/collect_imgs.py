import cv2
import os

# Function to get annotation from a frame
def get_annotation_from(frame):
    # Placeholder function, replace with your actual implementation
    # This function should return detection_result and annotation
    return detection_result, annotation

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 1
dataset_size = 100
start_class_number = 36
  # Change this to the desired starting class number

# Open camera for capturing images
cap = cv2.VideoCapture(0)  # Use camera index 0, change it as necessary

# Loop over the classes
for j in range(start_class_number, start_class_number + number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()  # Capture a frame from the camera
        if not ret:  # Check if frame was captured successfully
            print("! No frame")
            break

        # Display a message on the frame
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        
        # Check for 'Q' key press to break out of the loop
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()  # Capture a frame from the camera
        if not ret:  # Check if frame was captured successfully
            print("! No frame")
            break

        cv2.imshow('frame', frame)
        cv2.waitKey(25)

        # Save the frame as an image
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
