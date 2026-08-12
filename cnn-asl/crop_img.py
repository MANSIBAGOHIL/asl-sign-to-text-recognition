import cv2

def crop_hand(image_path, crop_coords):
    # Load the image
    image = cv2.imread(image_path)
    
    # Crop the image using the specified coordinates
    cropped_image = image[crop_coords[0]:crop_coords[1], crop_coords[2]:crop_coords[3]]
    
    return cropped_image

# Example usage
image_path = r"D:\STTC\dataSet\trainingData\A\A_0_1_1.jpg"
crop_coords = [220, 260, 450, 480]  # Specify the cropping coordinates [y1, y2, x1, x2]
cropped_image = crop_hand(image_path, crop_coords)

# Display the cropped image
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
