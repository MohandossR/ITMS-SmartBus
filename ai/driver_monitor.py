import cv2
import time

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

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    status = "ALERT"

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)

        if len(eyes) == 0:
            if eye_closed_start is None:
                eye_closed_start = time.time()
            elif time.time() - eye_closed_start >= DROWSY_TIME:
                status = "DROWSY ⚠️"
        else:
            eye_closed_start = None

        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

    color = (0,255,0) if status=="ALERT" else (0,0,255)
    cv2.putText(frame, status, (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.1, color, 3)

    cv2.imshow("Driver Monitoring (Live)", frame)

    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
