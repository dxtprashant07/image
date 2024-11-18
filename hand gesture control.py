import cv2
import mediapipe as mp
import pyautogui
x1  = y1= x2 = y2= 0
webcam =  cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands()
drawing_box = mp.solutions.drawing_utils

while True :
    _, image = webcam.read()
    frame_height, frame_width = image.shape[:2]
    #cv2.imshow("window", image)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = hands.process(rgb)
    hand1 = output.multi_hand_landmarks
    if hand1 :
        for hand in hand1:
            drawing_box.draw_landmarks(image,hand)

            landmarks = hand.landmark
            for id, landmarks in enumerate(landmarks):
                x = int(landmarks.x*frame_width)
                y = int(landmarks.y*frame_height)
                if id == 8 :
                    cv2.circle(img = image,center=(x,y),radius=8,color=(0,255,255),thickness=2)
                    x1 =  x
                    y1 = y
                if id == 4  :
                    cv2.circle(img = image,center=(x,y),radius=8,color=(0,255,0),thickness=2)
                    x2 = x
                    y2 = y
        dist = ((x2-x1)**2 + (y2-y1)**2)**0.5//4
        cv2.line(image, (x1,y1),(x2,y2),(255,0,0),thickness=4)
        if dist > 50 :
            pyautogui.press('volumeup')
        else:
            pyautogui.press('volumedown')


               
    
    cv2.imshow("window", image)
    if cv2.waitKey(1) & 0xff == ord('s'):
        break

cv2.destroyAllWindows()