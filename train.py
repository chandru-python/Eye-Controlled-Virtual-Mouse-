import cv2
import pyautogui
import numpy as np
import dlib
from scipy.spatial import distance
import time

# Configuration
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.01  # Reduce pause for faster actions
screen_width, screen_height = pyautogui.size()

# Initialize camera
cap = cv2.VideoCapture(0)

# Initialize dlib face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Eye aspect ratio calculation
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# Mouse movement smoothing
alpha = 0.4  
prev_eye_pos = np.array([screen_width / 2, screen_height / 2])

# Blink detection variables
blink_start_time = None
blink_times = []
last_action_time = 0

# Timing thresholds
blink_threshold = 0.22
left_click_min_time = 0.5
left_click_max_time = 1.0
double_blink_window = 3.0
long_blink_time = 1.0
cooldown_time = 0.5  # Reduced cooldown for faster interactions

# Scrolling control
scroll_smooth_factor = 0.05  # Faster response time
base_scroll_speed = 20  # Increased base speed
scroll_multiplier = 2.0  # Scroll acceleration
last_scroll_time = time.time()

# Frame control
frame_skip = 1  # Process every frame
frame_count = 0

def move_mouse(eye_x, eye_y, frame_shape):
    global prev_eye_pos, last_scroll_time
    x_screen = screen_width * (1 - (eye_x / frame_shape[1]))  # Invert X-axis
    y_screen = screen_height * (eye_y / frame_shape[0])

    # Apply smoothing
    new_eye_pos = np.array([x_screen, y_screen])
    smoothed_pos = alpha * new_eye_pos + (1 - alpha) * prev_eye_pos
    prev_eye_pos[:] = smoothed_pos  
    
    # Move mouse instantly without delay
    pyautogui.moveTo(smoothed_pos[0], smoothed_pos[1], duration=0.01)

    # Fast and continuous scrolling
    current_time = time.time()
    if current_time - last_scroll_time > scroll_smooth_factor:
        distance_from_center = abs(smoothed_pos[1] - screen_height / 2) / (screen_height / 2)
        dynamic_scroll_speed = int(base_scroll_speed + (distance_from_center * scroll_multiplier * base_scroll_speed))

        if smoothed_pos[1] < screen_height * 0.3:  # Top 30% -> Scroll Up
            pyautogui.scroll(dynamic_scroll_speed)
        elif smoothed_pos[1] > screen_height * 0.7:  # Bottom 30% -> Scroll Down
            pyautogui.scroll(-dynamic_scroll_speed)
            
        last_scroll_time = current_time  

# Set OpenCV window
cv2.namedWindow("Eyeball Tracker", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Eyeball Tracker", 800, 600)

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image.")
        break

    frame_count += 1
    if frame_count % frame_skip != 0:
        continue  

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)
        left_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(36, 42)]
        right_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(42, 48)]

        # Draw landmarks
        cv2.polylines(frame, [np.array(left_eye, np.int32)], True, (0, 255, 0), 2)
        cv2.polylines(frame, [np.array(right_eye, np.int32)], True, (0, 255, 0), 2)

        # Cursor movement based on eye position
        left_eye_center = np.mean(left_eye, axis=0)
        right_eye_center = np.mean(right_eye, axis=0)
        eye_midpoint = ((left_eye_center[0] + right_eye_center[0]) // 2, 
                        (left_eye_center[1] + right_eye_center[1]) // 2)

        move_mouse(eye_midpoint[0], eye_midpoint[1], frame.shape)

        # Blink detection logic
        left_EAR = eye_aspect_ratio(left_eye)
        right_EAR = eye_aspect_ratio(right_eye)
        blink_detected = left_EAR < blink_threshold and right_EAR < blink_threshold
        current_time = time.time()

        if blink_detected:
            if blink_start_time is None:
                blink_start_time = current_time
        else:
            if blink_start_time is not None:
                blink_duration = current_time - blink_start_time
                blink_start_time = None  

                # Left Click (Blink 0.5 - 1 sec)
                if left_click_min_time <= blink_duration < left_click_max_time:
                    if current_time - last_action_time > cooldown_time:
                        pyautogui.click()
                        print("Left click triggered")
                        last_action_time = current_time
                        blink_times.clear()  

                # Right Click (Blink more than 1 sec)
                elif blink_duration >= long_blink_time:
                    if current_time - last_action_time > cooldown_time:
                        pyautogui.rightClick()
                        print("Right click triggered")
                        last_action_time = current_time
                        blink_times.clear()  

                else:
                    blink_times.append(current_time)
                    blink_times = [t for t in blink_times if current_time - t <= double_blink_window]

                    # Double Click (Two blinks within 3 sec)
                    if len(blink_times) == 2 and (current_time - blink_times[0]) <= double_blink_window:
                        if current_time - last_action_time > cooldown_time:
                            pyautogui.doubleClick()
                            print("Double click triggered")
                            last_action_time = current_time
                            blink_times.clear()  

    # Show output
    cv2.imshow("Eyeball Tracker", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
