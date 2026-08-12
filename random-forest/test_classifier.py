import cv2
import mediapipe as mp
import numpy as np
import pickle
from sklearn.metrics import accuracy_score

# Load the sign-to-text model
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

# Load the test dataset with ground truth labels
test_data = pickle.load(open('./test_data.p', 'rb'))  # Should contain images and their corresponding labels

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Lists to store the ground truth and predictions
y_true = []
y_pred = []

# Loop through the test dataset
for item in test_data:
    frame = item['image']  # The test image
    expected_character = item['label']  # The expected sign character

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        data_aux = []
        x_ = []
        y_ = []

        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

        # Predict the sign
        prediction = model.predict([np.asarray(data_aux)])
        predicted_character = labels_dict[int(prediction[0])]

        # Store ground truth and prediction
        y_true.append(expected_character)
        y_pred.append(predicted_character)

# Calculate accuracy
accuracy = accuracy_score(y_true, y_pred)
print(f"Accuracy of the sign-to-text pipeline: {accuracy * 100:.2f}%")
