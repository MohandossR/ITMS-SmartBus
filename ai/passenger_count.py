import cv2
from ultralytics import YOLO
from collections import deque

model = YOLO("yolov8n.pt")
TOTAL_SEATS = 40


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

count_buffer = deque(maxlen=10)
MAX_PASSENGERS = 20

while True:
    ret, frame = cap.read()
    if not ret:
        print("Frame not received")
        break

    frame = cv2.resize(frame, (640, 480))

    results = model(frame, conf=0.4, classes=[0], verbose=False)

    person_count = 0
    for r in results:
        for box in r.boxes:
            person_count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)

    count_buffer.append(person_count)
    stable_count = int(sum(count_buffer) / len(count_buffer))
    vacant_seats = TOTAL_SEATS - stable_count
    if vacant_seats < 0:
        vacant_seats = 0


    status = "NORMAL"
    if stable_count > MAX_PASSENGERS:
        status = "OVERCROWDED ⚠️"

    cv2.putText(frame, f"Passengers: {stable_count}", (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.1, (255,255,255), 3)
    cv2.putText(frame, status, (20,80),
                cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0,0,255), 3)
    cv2.putText(frame, f"Vacant Seats: {vacant_seats}", (20,120),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,255), 3)


    cv2.imshow("Passenger Monitoring (Live)", frame)

    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
