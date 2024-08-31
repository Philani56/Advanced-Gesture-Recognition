import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

# Initialize video capture
cap = cv2.VideoCapture(0)

def count_fingers(hand_landmarks):
    """Count the number of fingers that are up."""
    landmarks = hand_landmarks.landmark
    finger_tips = [
        mp_hands.HandLandmark.THUMB_TIP,
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP
    ]
    finger_pips = [
        mp_hands.HandLandmark.THUMB_IP,
        mp_hands.HandLandmark.INDEX_FINGER_PIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_PIP,
        mp_hands.HandLandmark.RING_FINGER_PIP,
        mp_hands.HandLandmark.PINKY_PIP
    ]
    
    count = 0
    for tip, pip in zip(finger_tips, finger_pips):
        tip_y = landmarks[tip].y
        pip_y = landmarks[pip].y
        if tip_y < pip_y:  # Check if the fingertip is higher than the proximal joint
            count += 1
    
    return count

def detect_gesture(hand_landmarks):
    """Detect specific gestures based on landmarks."""
    landmarks = hand_landmarks.landmark
    thumb_tip_y = landmarks[mp_hands.HandLandmark.THUMB_TIP].y
    thumb_ip_y = landmarks[mp_hands.HandLandmark.THUMB_IP].y
    index_tip_y = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip_y = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip_y = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip_y = landmarks[mp_hands.HandLandmark.PINKY_TIP].y
    
    thumb_is_up = thumb_tip_y < thumb_ip_y
    index_is_up = index_tip_y < landmarks[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
    middle_is_up = middle_tip_y < landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
    ring_is_up = ring_tip_y < landmarks[mp_hands.HandLandmark.RING_FINGER_PIP].y
    pinky_is_up = pinky_tip_y < landmarks[mp_hands.HandLandmark.PINKY_PIP].y

    if thumb_is_up and not (index_is_up or middle_is_up or ring_is_up or pinky_is_up):
        return "Thumbs Up"
    elif index_is_up and middle_is_up and not (ring_is_up or pinky_is_up):
        return "Peace Sign"
    elif not (thumb_is_up or index_is_up or middle_is_up or ring_is_up or pinky_is_up):
        return "Closed Fist"
    else:
        return "Unknown Gesture"

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break
    
    # Flip the frame horizontally and convert to RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame
    results = hands.process(rgb_frame)
    
    num_hands = 0
    finger_counts = []
    gestures = []
    
    if results.multi_hand_landmarks:
        num_hands = len(results.multi_hand_landmarks)
        for hand_landmarks in results.multi_hand_landmarks:
            # Count fingers
            finger_count = count_fingers(hand_landmarks)
            finger_counts.append(finger_count)
            
            # Detect gesture
            gesture = detect_gesture(hand_landmarks)
            gestures.append(gesture)
            
            # Draw landmarks and connections
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    # Display the results
    for i, (count, gesture) in enumerate(zip(finger_counts, gestures)):
        cv2.putText(frame, f'Hand {i+1} Fingers: {count}', 
                    (10, 70 + 80*i), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, f'Hand {i+1} Gesture: {gesture}', 
                    (10, 110 + 80*i), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
    
    cv2.putText(frame, f'Number of Hands: {num_hands}', 
                (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    # Display the frame
    cv2.imshow("Finger Counting and Gesture Recognition", frame)
    
    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
