from ultralytics import YOLO
import cv2
from deep_sort_realtime.deepsort_tracker import DeepSort
from emergency_alert import send_emergency_alert
import time

def start_vision_detection():
    model = YOLO("yolov8n.pt")  # Use a light model for real-time
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    tracker = DeepSort()

    print("[VISION] Advanced behavior detection started...")
    follow_time_threshold = 10  # seconds
    follow_counter = {}  # Track how long a person is following
    last_alert_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)[0]
        person_detections = []

        for box in results.boxes:
            cls = int(box.cls[0])
            if cls == 0:  # Class 0 = person
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                person_detections.append(([x1, y1, x2 - x1, y2 - y1], conf, 'person'))

        tracks = tracker.update_tracks(person_detections, frame=frame)

        current_time = time.time()

        for track in tracks:
            if not track.is_confirmed():
                continue

            track_id = track.track_id
            bbox = track.to_ltrb()

            if track_id not in follow_counter:
                follow_counter[track_id] = current_time
            elif current_time - follow_counter[track_id] > follow_time_threshold:
                if current_time - last_alert_time > 60:
                    print(f"[ALERT] Person {track_id} following too long. Sending alert...")
                    send_emergency_alert()
                    last_alert_time = current_time

            x1, y1, x2, y2 = map(int, bbox)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"ID: {track_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        cv2.imshow("SafeWalk Behavior Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()