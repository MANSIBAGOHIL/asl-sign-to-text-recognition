import os

def rename_images(directory):
    # Get all files in the directory
    files = os.listdir(directory)
    # Counter for unique names
    count = 1
    # Get the folder name
    folder_name = os.path.basename(directory)
    # Iterate through each file
    for file in files:
        # Check if it's a file (not a directory)
        if os.path.isfile(os.path.join(directory, file)):
            # Split the file name and extension
            name, ext = os.path.splitext(file)
            # Construct new name with unique number and folder prefix
            new_name = f"{name}_{count}{ext}"
            # Rename the file
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            # Increment counter
            count += 1

# List of directories
directories = [r"D:\Computer Vision\ASL_ICT\Mansiba\X"]

# Rename images in each directory
for directory in directories:
    rename_images(directory)
