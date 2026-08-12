import cv2
import mediapipe as mp
import numpy as np

# Load pre-trained MediaPipe Hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Open pre-recorded video
cap = cv2.VideoCapture("D:\STTC\Frames\A_class_1_231.avi")  # Replace "recorded_video.mp4" with your video file

# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video_with_frame.mp4', fourcc, 30.0, (640, 480))  # Adjust resolution as necessary

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Break the loop when the video ends
    
    # Convert the frame to RGB and process it with MediaPipe Hands
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            if hand_landmarks is not None and hand_landmarks.landmark:
                # Extract bounding box coordinates for the hand
                bounding_box = cv2.boundingRect(np.array([[lm.x, lm.y] for lm in hand_landmarks.landmark]))
                x, y, w, h = bounding_box
                
                # Draw a rectangle around the hand
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 4)
    
    # Write the frame with the overlayed rectangle to the output video
    out.write(frame)

    # Display the frame
    cv2.imshow('frame', frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
