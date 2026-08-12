import cv2
import os

# Define the mode and directory
mode = 'testingData'
directory = 'dataSet/' + mode + '/'

# Create a dictionary to map key presses to folder names
key_to_folder = {
    ord('a'): 'A',
    ord('b'): 'B',
    ord('c'): 'C',
    ord('d'): 'D',
    ord('e'): 'E',
    ord('f'): 'F',
    ord('g'): 'G',
    ord('h'): 'H',
    ord('i'): 'I',
    ord('j'): 'J',
    ord('k'): 'K',
    ord('l'): 'L',
    ord('m'): 'M',
    ord('n'): 'N',
    ord('o'): 'O',
    ord('p'): 'P',
    ord('q'): 'Q',
    ord('r'): 'R',
    ord('s'): 'S',
    ord('t'): 'T',
    ord('u'): 'U',
    ord('v'): 'V',
    ord('w'): 'W',
    ord('x'): 'X',
    ord('y'): 'Y',
    ord('z'): 'Z'
}

# Function to process images and generate ROI
def process_image(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    blur = cv2.GaussianBlur(gray, (5, 5), 2)
    
    # Apply adaptive thresholding
    th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    
    # Apply Otsu's thresholding
    _, processed_image = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    return processed_image

# Process images and generate ROI
for key in key_to_folder:
    folder = key_to_folder[key]
    files_in_folder = os.listdir(os.path.join(directory, folder))
    
    for file_name in files_in_folder:
        image_path = os.path.join(directory, folder, file_name)
        image = cv2.imread(image_path)
        
        if image is not None:
            roi = process_image(image)
            cv2.imwrite(image_path, roi)

print("ROI generation completed.")
