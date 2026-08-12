from moviepy.editor import VideoFileClip, ImageClip
from moviepy.video.io.bindings import mplfig_to_npimage
import numpy as np

# Load the video clip
video_clip = VideoFileClip("D:\Computer Vision\ASL_ICT\Aryavardhan\A\A_class_1_231.avi")

# Load the frame image with transparent background
frame_image = ImageClip("frame_image.png", transparent=True)

# Define a region where you want to place the frame (e.g., coordinates of the hand)
hand_region = {'x': 100, 'y': 100, 'width': 200, 'height': 200}

# Define a function to overlay the frame onto the hand region
def overlay_frame_on_hand_frame(video_frame):
    # Convert the video frame to numpy array
    frame_np = video_frame.to_RGB().astype(np.uint8)
    
    # Convert frame image to numpy array
    frame_image_np = frame_image.to_RGB().astype(np.uint8)
    
    # Overlay frame image onto the hand region of the video frame
    frame_np[hand_region['y']:hand_region['y']+hand_region['height'], 
             hand_region['x']:hand_region['x']+hand_region['width']] = frame_image_np
    
    return frame_np

# Apply the overlay function to each frame of the video clip
final_clip = video_clip.fl_image(overlay_frame_on_hand_frame)

# Write the final video clip to a file
final_clip.write_videofile("output_video_with_frame.mp4", codec="libx264", fps=video_clip.fps)
