import cv2
import time

def start_vision_detection():
    # Load pre-trained Haarcascade for full body detection
    body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

    cap = cv2.VideoCapture(0)

    print("[INFO] Starting SafeWalk Vision Detection...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to grab frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        bodies = body_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw rectangles around detected bodies
        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # Here you can add: trigger alert or sound, etc.
            cv2.putText(frame, "Person Detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("SafeWalk - Vision Mode", frame)

        # Press 'q' to quit the vision window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] Vision Detection Stopped.")