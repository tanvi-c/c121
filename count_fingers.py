import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence = 0.8, min_tracking_confidence = 0.5)

tipIds = [4, 8, 12, 16, 20]

def countFingers(image, hand_landmarks, handNo = 0):
    
    if hand_landmarks:
        landmarks = hand_landmarks[handNo].landmark
        fingers = []
        
        for lm_index in tipIds:
            finger_tip_y = landmarks[lm_index].y
            finger_bottom_y = landmarks[lm_index - 2].y
            
            if lm_index !=4:
                if finger_tip_y < finger_bottom_y:
                    fingers.append(1)
                    print("Finger with ID ", lm_index, " is closed")
                        
                if finger_tip_y > finger_bottom_y:
                    fingers.append(0)
                    print("Finger with ID ", lm_index, "is closed")
                    
        totalFingers = fingers.count(1)
        text = f'Fingers: {totalFingers}'
        cv2.putText(image, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        
        
def drawHandLandmarks(image, hand_landmarks):
    
    if hand_landmarks:
        for landmarks in hand_landmarks:
            mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)


while True:
    success, image = cap.read()

    cv2.imshow("Media Controller", image)

    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()

