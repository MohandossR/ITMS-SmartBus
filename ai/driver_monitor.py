import cv2
import time
import requests
import json

def update_shared_state(status, attention_score, fire_detected):
    try:
        with open("ai/shared_state.json", "r+") as f:
            try:
                data = json.load(f)
            except:
                data = {}

            data["driver_status"] = status
            data["attention_score"] = attention_score
            data["fire_detected"] = fire_detected

            f.seek(0)
            json.dump(data, f)
            f.truncate()
    except:
        pass



last_face_time = time.time()
DANGER_TIME = 1.5  
danger_alert = False

alert_time = 0
drowsy_time = 0
danger_time = 0
last_update = time.time()

distraction_start = None
DISTRACTION_TIME = 2.0
distracted = False




face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

eye_closed_start = None
DROWSY_TIME = 2.0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    now = time.time()
    delta = now - last_update
    last_update = now


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    current_time = time.time()

    danger_alert = False
    status = "ALERT"

    if len(faces) == 0:
        if current_time - last_face_time > DANGER_TIME:
            danger_alert = True
    else:
        last_face_time = current_time


    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        face_center_y = y + h // 2

        if face_center_y > frame.shape[0] * 0.65:
            if distraction_start is None:
                distraction_start = time.time()
            elif time.time() - distraction_start >= DISTRACTION_TIME:
                distracted = True
        else:
            distraction_start = None
            distracted = False


        if not danger_alert:  # only check drowsy if not dangerous
            if len(eyes) == 0:
                if eye_closed_start is None:
                    eye_closed_start = time.time()
                elif time.time() - eye_closed_start >= DROWSY_TIME:
                    status = "DROWSY ⚠️"
            else:
                eye_closed_start = None

        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

    if danger_alert:
        status = "DANGEROUS DRIVING ⚠️"
    elif distracted:
        status = "DRIVER DISTRACTED 📱"


    if status == "ALERT":
        alert_time += delta
    elif "DROWSY" in status:
        drowsy_time += delta
    else:
        danger_time += delta


    if status == "ALERT":
        color = (0,255,0)
    elif "DROWSY" in status:
            color = (0,165,255)
    elif "DISTRACTED" in status:
        color = (255, 0, 255)

    else:
        color = (0,0,255)
    cv2.putText(frame, status, (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.1, color, 3)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_fire = (0, 50, 50)
    upper_fire = (35, 255, 255)

    fire_mask = cv2.inRange(hsv, lower_fire, upper_fire)
    fire_pixels = cv2.countNonZero(fire_mask)

    if fire_pixels > 1500:
        cv2.putText(frame, "FIRE / SMOKE DETECTED 🔥",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (0, 0, 255),
            3)

    
    total_time = alert_time + drowsy_time + danger_time
    attention_score = int((alert_time / total_time) * 100) if total_time > 0 else 100

    fire_detected = fire_pixels > 1500

    update_shared_state(
        status=status,
        attention_score=attention_score,
        fire_detected=fire_detected
    )


    cv2.putText(frame, f"Driver Attention: {attention_score}%",
        (20,80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,
        (255,255,0),
        3)


    cv2.imshow("Driver Monitoring (Live)", frame)

    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
